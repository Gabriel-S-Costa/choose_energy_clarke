from app.modules.suppliers.models import Supplier
from app.shared.interfaces import ISupplierReporsitory
from app.shared.utils import truncate


class SupplierService:
    def __init__(self, reporitory: ISupplierReporsitory):
        self.reporitory = reporitory

    def get_all_suppliers(self, page: int = 1, size: int = 10) -> tuple[list[Supplier], int]:
        offset = (page - 1) * size
        return self.reporitory.get_all_suppliers(offset=offset, limit=size)

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
                supplier_cost_per_kwl = supplier.cost_kwh_gd
            elif supplier.is_free_market:
                supplier_cost_per_kwl = supplier.cost_kwh_ml
            elif supplier.is_both:
                supplier_cost_per_kwl = supplier.cost_kwh_gd + supplier.cost_kwh_ml

            supplier_type = supplier.type
            offer = self._calculate_offer_costs(consumption, state_base_cost, supplier_type, supplier_cost_per_kwl)
            estimated_savings = self._ordering_estimated_savings(supplier_type, offer['estimated_savings'], estimated_savings_per_type)

            available_types.add(supplier_type)
            offers.append(offer)
            estimated_savings_per_type.update(estimated_savings)

            if offers:
                supp_dict['offers'] = offers
                supplier_results.append(supp_dict)

        return {
            'state_base_cost': state_base_cost,
            'available_types': list(available_types),
            'estimated_savings_per_type': estimated_savings_per_type,
            'suppliers': supplier_results,
        }

    def _calculate_offer_costs(self, consumption: int, state_base_cost: int, supplier_type: str, supplier_cost: int) -> dict:
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

    def _ordering_estimated_savings(self, supplier_type: str, estimated_savings: int, current_savings_dict: dict) -> dict[str, int]:
        current_max = current_savings_dict.get(supplier_type, 0)
        return {supplier_type: max(current_max, estimated_savings)}
