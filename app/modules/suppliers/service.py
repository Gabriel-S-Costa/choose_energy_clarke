from app.modules.suppliers.enums import SupplierTypes
from app.modules.suppliers.models import Supplier
from app.shared.interfaces import ISupplierReporsitory
from app.shared.utils import truncate


class SupplierService:
    def __init__(self, reporitory: ISupplierReporsitory):
        self.reporitory = reporitory

    def get_all_suppliers(self, page: int = 1, size: int = 10) -> tuple[list[Supplier], int]:
        offset = (page - 1) * size
        return self.reporitory.get_all_suppliers(offset=offset, limit=size)

    def get_supplier_by_id(self, id: int) -> Supplier:
        return self.reporitory.get_supplier_by_id(id)

    def search_suppliers(self, query) -> dict:
        state, suppliers = self.reporitory.search_suppliers_by_state(query.uf)
        if not state:
            return {'state_base_cost': 0, 'available_types': [], 'estimated_savings_per_type': {}, 'suppliers': []}

        consumption = query.consumption
        state_base_cost = consumption * state.base_cost_per_kwl

        supplier_results = []
        available_types = set()
        estimated_savings_per_type = {}

        for supplier in suppliers:
            supp_dict = {k: getattr(supplier, k) for k in supplier.__table__.columns.keys()}
            supp_dict['states'] = supplier.states

            offers = []

            if supplier.is_distributed_generation:
                sup_type = SupplierTypes.DISTRIBUTED_GENERATION.value
                dg_offer = self._calculate_costs(consumption, state_base_cost, sup_type, supplier.cost_kwh_gd)
                offers.append(dg_offer)

                available_types.add(sup_type)
                if sup_type not in estimated_savings_per_type or dg_offer['estimated_savings'] > estimated_savings_per_type[sup_type]:
                    estimated_savings_per_type[sup_type] = dg_offer['estimated_savings']

            if supplier.is_free_market:
                sup_type = SupplierTypes.FREE_MARKET.value
                fm_offer = self._calculate_costs(consumption, state_base_cost, sup_type, supplier.cost_kwh_ml)
                offers.append(fm_offer)

                available_types.add(sup_type)
                if sup_type not in estimated_savings_per_type or fm_offer['estimated_savings'] > estimated_savings_per_type[sup_type]:
                    estimated_savings_per_type[sup_type] = fm_offer['estimated_savings']

            supp_dict['offers'] = offers
            if offers:
                supplier_results.append(supp_dict)

        return {
            'state_base_cost': state_base_cost,
            'available_types': list(available_types),
            'estimated_savings_per_type': estimated_savings_per_type,
            'suppliers': supplier_results,
        }

    def _calculate_costs(self, consumption: int, state_base_cost: int, supplier_type: str, supplier_cost: int) -> dict:
        estimated_cost = consumption * supplier_cost
        estimated_savings = state_base_cost - estimated_cost
        percentage_savings = estimated_savings / state_base_cost if state_base_cost else 0.0

        return {
            'type': supplier_type,
            'kwl_cost': supplier_cost,
            'estimated_cost': estimated_cost,
            'estimated_savings': estimated_savings,
            'percentage_savings': truncate(percentage_savings * 100),
        }
