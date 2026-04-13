import pytest
from fastapi.testclient import TestClient
from sqlmodel import Session, SQLModel, create_engine, select
from sqlmodel.pool import StaticPool

from app.core.database import db
from app.main import app
from app.modules.suppliers.models import State, Supplier

# Usar banco in-memory SQLite ultrarrápido para testes isolados
testing_engine = create_engine('sqlite://', connect_args={'check_same_thread': False}, poolclass=StaticPool)


@pytest.fixture
def states():
    states = [
        State(name='Amazonas', uf='AM', base_cost_per_kwl=250),
        State(name='Pará', uf='PA', base_cost_per_kwl=250),
    ]
    return states


@pytest.fixture
def supplier():
    return Supplier(
        name='Amazonas Green Energy',
        cost_kwh_gd=95,
        is_active=True,
        type='distributed_generation',
    )


@pytest.fixture(name='session')
def session_fixture(states, supplier):
    # 1. Cria as tabelas do zero na memória
    SQLModel.metadata.create_all(testing_engine)

    with Session(testing_engine) as session:
        # 2. Popula os dados via os dicts do seed para que o banco não esteja vazio
        for state in states:
            session.add(state)

        states = session.exec(select(State).where(State.uf.in_(['AM', 'PA']))).all()
        supplier.states = states
        session.add(supplier)

        session.commit()

    with Session(testing_engine) as session:
        yield session

    # 3. Limpa tudo após terminar a run (teoricamente memory morre instantaneo, mas é boa prática)
    SQLModel.metadata.drop_all(testing_engine)


@pytest.fixture(name='test_client', autouse=True)
def client_fixture(session: Session):
    def get_session_override():
        return session

    # Sobreescreve a injeção de dependência original "db.get_session_conn" pelo mock acima
    app.dependency_overrides[db.get_session_conn] = get_session_override

    with TestClient(app) as client:
        yield client

    app.dependency_overrides.clear()
