import random

from sqlmodel import Session, select

from app.core.database import db
from app.modules.suppliers.enums import SupplierTypes
from app.modules.suppliers.models import State, Supplier

STATES_DATA = [
    {'name': 'Acre', 'uf': 'AC'},
    {'name': 'Alagoas', 'uf': 'AL'},
    {'name': 'Amapá', 'uf': 'AP'},
    {'name': 'Amazonas', 'uf': 'AM'},
    {'name': 'Bahia', 'uf': 'BA'},
    {'name': 'Ceará', 'uf': 'CE'},
    {'name': 'Distrito Federal', 'uf': 'DF'},
    {'name': 'Espírito Santo', 'uf': 'ES'},
    {'name': 'Goiás', 'uf': 'GO'},
    {'name': 'Maranhão', 'uf': 'MA'},
    {'name': 'Mato Grosso', 'uf': 'MT'},
    {'name': 'Mato Grosso do Sul', 'uf': 'MS'},
    {'name': 'Minas Gerais', 'uf': 'MG'},
    {'name': 'Pará', 'uf': 'PA'},
    {'name': 'Paraíba', 'uf': 'PB'},
    {'name': 'Paraná', 'uf': 'PR'},
    {'name': 'Pernambuco', 'uf': 'PE'},
    {'name': 'Piauí', 'uf': 'PI'},
    {'name': 'Rio de Janeiro', 'uf': 'RJ'},
    {'name': 'Rio Grande do Norte', 'uf': 'RN'},
    {'name': 'Rio Grande do Sul', 'uf': 'RS'},
    {'name': 'Rondônia', 'uf': 'RO'},
    {'name': 'Roraima', 'uf': 'RR'},
    {'name': 'Santa Catarina', 'uf': 'SC'},
    {'name': 'São Paulo', 'uf': 'SP'},
    {'name': 'Sergipe', 'uf': 'SE'},
    {'name': 'Tocantins', 'uf': 'TO'},
]

SUPPLIERS_DATA = [
    {'name': 'EcoPower Soluções', 'kwl_cost': 82, 'is_active': True, 'type': SupplierTypes.FREE_MARKET, 'state_ufs': ['SP', 'MG', 'RJ']},
    {'name': 'Vento Sul Energia', 'kwl_cost': 75, 'is_active': True, 'type': SupplierTypes.FREE_MARKET, 'state_ufs': ['RS', 'SC', 'PR']},
    {'name': 'BioGen Brasil', 'kwl_cost': 90, 'is_active': True, 'type': SupplierTypes.FREE_MARKET, 'state_ufs': ['SP', 'GO', 'MS']},
    {'name': 'Luz do Sertão', 'kwl_cost': 68, 'is_active': True, 'type': SupplierTypes.DISTRIBUTED_GENERATION, 'state_ufs': ['BA', 'CE', 'PE', 'RN']},
    {'name': 'Amazonas Green Energy', 'kwl_cost': 95, 'is_active': True, 'type': SupplierTypes.DISTRIBUTED_GENERATION, 'state_ufs': ['AM', 'PA']},
    {'name': 'Delta Energia', 'kwl_cost': 88, 'is_active': True, 'type': SupplierTypes.DISTRIBUTED_GENERATION, 'state_ufs': ['SP', 'ES', 'RJ']},
    {
        'name': 'Cerrado Volts',
        'kwl_cost': 80,
        'is_active': False,  # Fornecedor inativo para testar filtros
        'type': SupplierTypes.DISTRIBUTED_GENERATION,
        'state_ufs': ['DF', 'GO', 'TO'],
    },
    {'name': 'Pampa Watts', 'kwl_cost': 77, 'is_active': True, 'type': SupplierTypes.FREE_MARKET, 'state_ufs': ['RS']},
    {'name': 'Norte Luz', 'kwl_cost': 92, 'is_active': True, 'type': SupplierTypes.FREE_MARKET, 'state_ufs': ['RR', 'AP', 'AC']},
    {'name': 'Atlântica Renováveis', 'kwl_cost': 84, 'is_active': True, 'type': SupplierTypes.DISTRIBUTED_GENERATION, 'state_ufs': ['AL', 'SE', 'PB']},
]


def seed_database():
    with Session(db.engine) as session:
        for state in STATES_DATA:
            base_cost_per_kwl = random.randint(100, 1000)
            state = State(name=state['name'], uf=state['uf'], base_cost_per_kwl=base_cost_per_kwl)
            session.add(state)

        for supplier_data in SUPPLIERS_DATA:
            supplier = Supplier(
                name=supplier_data['name'],
                kwl_cost=supplier_data['kwl_cost'],
                is_active=supplier_data['is_active'],
                type=supplier_data['type'],
            )

            supplier_states = supplier_data['state_ufs']
            states = select(State).where(State.uf.in_(supplier_states))
            db_states = session.exec(states).all()

            supplier.states = db_states
            session.add(supplier)

        session.commit()
        print(f'{len(STATES_DATA)} estados processados!')
        print(f'{len(SUPPLIERS_DATA)} fornecedores processados!')


if __name__ == '__main__':
    seed_database()
