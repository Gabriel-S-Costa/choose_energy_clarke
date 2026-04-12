from app.modules.suppliers.enums import SupplierTypes
from app.modules.suppliers.models import Supplier
from app.shared.interfaces import ISupplierReporsitory


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
            return {
                "state_base_cost": 0,
                "available_types": [],
                "estimated_savings_per_type": {},
                "suppliers": []
            }

        consumption = query.consumption
        state_base_cost = consumption * state.base_cost_per_kwl

        supplier_results = []
        available_types = set()
        estimated_savings_per_type = {}

        for supplier in suppliers:
            supp_dict = {k: getattr(supplier, k) for k in supplier.__table__.columns.keys()}
            supp_dict["states"] = supplier.states
            
            offers = []

            if supplier.cost_kwh_gd is not None and supplier.type in (SupplierTypes.DISTRIBUTED_GENERATION.value, SupplierTypes.BOTH):
                estimated_cost = consumption * supplier.cost_kwh_gd
                estimated_savings = state_base_cost - estimated_cost
                percentage_savings = estimated_savings / state_base_cost if state_base_cost else 0.0
                
                sup_type = SupplierTypes.DISTRIBUTED_GENERATION.value
                offers.append({
                    "type": sup_type,
                    "kwl_cost": supplier.cost_kwh_gd,
                    "estimated_cost": float(estimated_cost),
                    "estimated_savings": float(estimated_savings),
                    "percentage_savings": percentage_savings
                })
                
                available_types.add(sup_type)
                if sup_type not in estimated_savings_per_type or estimated_savings > estimated_savings_per_type[sup_type]:
                    estimated_savings_per_type[sup_type] = estimated_savings

            if supplier.cost_kwh_ml is not None and supplier.type in (SupplierTypes.FREE_MARKET.value, SupplierTypes.BOTH):
                estimated_cost = consumption * supplier.cost_kwh_ml
                estimated_savings = state_base_cost - estimated_cost
                percentage_savings = estimated_savings / state_base_cost if state_base_cost else 0.0
                
                sup_type = SupplierTypes.FREE_MARKET.value
                offers.append({
                    "type": sup_type,
                    "kwl_cost": supplier.cost_kwh_ml,
                    "estimated_cost": float(estimated_cost),
                    "estimated_savings": float(estimated_savings),
                    "percentage_savings": percentage_savings
                })
                
                available_types.add(sup_type)
                if sup_type not in estimated_savings_per_type or estimated_savings > estimated_savings_per_type[sup_type]:
                    estimated_savings_per_type[sup_type] = estimated_savings

            supp_dict["offers"] = offers
            if offers:
                supplier_results.append(supp_dict)

        return {
            "state_base_cost": state_base_cost,
            "available_types": list(available_types),
            "estimated_savings_per_type": estimated_savings_per_type,
            "suppliers": supplier_results
        }