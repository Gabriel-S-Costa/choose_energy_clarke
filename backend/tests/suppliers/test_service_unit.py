from types import SimpleNamespace

from app.modules.suppliers.models import State, Supplier
from app.modules.suppliers.service import SupplierService


class _RepoStub:
    def __init__(self, state: State, suppliers: list[Supplier]):
        self._state = state
        self._suppliers = suppliers

    def search_suppliers_by_state(self, state: str):
        return (self._state, self._suppliers)


def test_search_suppliers_calculates_costs_correctly():
    consumption = 1000
    state = State(name='Amazonas', uf='AM', base_cost_per_kwl=2)

    supplier_gd = Supplier(name='GD Supplier', type='distributed_generation', cost_kwh_gd=1)
    supplier_fm = Supplier(name='FM Supplier', type='free_market', cost_kwh_ml=3)

    repo = _RepoStub(state=state, suppliers=[supplier_gd, supplier_fm])
    service = SupplierService(reporitory=repo)
    query = SimpleNamespace(state='AM', consumption=consumption)

    result = service.search_suppliers(query)

    assert result['state_base_cost'] == consumption * state.base_cost_per_kwl

    suppliers = {s['name']: s for s in result['suppliers']}

    gd_supplier = suppliers.get('GD Supplier')
    assert gd_supplier is not None

    gd_offer = gd_supplier['offers'][0]
    assert gd_offer['kwl_cost'] == 1
    assert gd_offer['estimated_cost'] == consumption * 1
    assert gd_offer['estimated_savings'] == (consumption * state.base_cost_per_kwl) - (consumption * 1)

    fm_supplier = suppliers.get('FM Supplier')
    assert fm_supplier is not None

    fm_offer = fm_supplier['offers'][0]
    assert fm_offer['kwl_cost'] == 3
    assert fm_offer['estimated_cost'] == consumption * 3
    assert fm_offer['estimated_savings'] == (consumption * state.base_cost_per_kwl) - (consumption * 3)
