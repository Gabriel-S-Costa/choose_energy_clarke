import { useState } from "react";
import type { SupplierResponse } from "@/features/suppliers/types";
import { makeApiRequest } from "@/services/api";

export function useSuppliers() {
  const [supplierResponse, setSupplierResponse] = useState<SupplierResponse>();
  const [isLoading, setIsLoading] = useState(false);
  const [error, setError] = useState<string | null>(null);

  const fetchSuppliers = async (state: string, consumption: number) => {
    setIsLoading(true);
    setError(null);

    try {
      const response_data = await makeApiRequest<SupplierResponse>(`suppliers/search?state=${state}&consumption=${consumption}`);
      setSupplierResponse(response_data);
    } catch (err: any) {
      console.error("Erro ao buscar fornecedores:", err);
      setError(err.response?.data?.message || "Ocorreu um erro ao buscar os fornecedores.");
    } finally {
      setIsLoading(false);
    }
  };

  return { supplierResponse, isLoading, error, fetchSuppliers };
}
