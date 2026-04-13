export interface Offer {
  type: string;
  kwl_cost: number;
  estimated_cost: number;
  estimated_savings: number;
  percentage_savings: number;
}

export interface Supplier {
  code: string;
  name: string;
  type: string;
  total_client: number;
  avg_rating: number;
  is_active: boolean;
  states: string[];
  offers: Offer[];
  logo?: string;
}

export interface SupplierSearchParams {
  state: string;
  consumption: number;
}

export interface EstimatedSavingsPerType {
  [key: string]: number;
}

export interface SupplierResponse {
  state_base_cost: number;
  available_types: string[];
  estimated_savings_per_type: EstimatedSavingsPerType;
  suppliers: Supplier[];
}