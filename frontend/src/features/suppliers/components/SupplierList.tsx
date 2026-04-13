import React from "react";
import type { SupplierResponse } from "@/features/suppliers/types";
import { SupplierCard } from "@/features/suppliers/components/SupplierCard";
import { SupplierSummary } from "@/features/suppliers/components/SupplierSummary";

interface SupplierListProps {
  supplierResponse?: SupplierResponse;
  isLoading: boolean;
  hasSearched: boolean;
}

export const SupplierList: React.FC<SupplierListProps> = ({
  supplierResponse,
  isLoading,
  hasSearched,
}) => {
  if (isLoading) {
    return (
      <div className="grid grid-cols-1 md:grid-cols-2 gap-6 mt-12 w-full">
        {[1, 2].map((i) => (
          <div
            key={i}
            className="h-64 bg-slate-100 animate-pulse rounded-2xl border border-slate-200"
          ></div>
        ))}
      </div>
    );
  }

  if (hasSearched && (!supplierResponse || supplierResponse.suppliers.length === 0)) {
    return (
      <div className="mt-12 text-center py-12 bg-slate-50 rounded-2xl border border-slate-200 w-full max-w-2xl mx-auto">
        <svg
          className="mx-auto h-12 w-12 text-slate-400"
          fill="none"
          viewBox="0 0 24 24"
          stroke="currentColor"
          aria-hidden="true"
        >
          <path
            strokeLinecap="round"
            strokeLinejoin="round"
            strokeWidth={1.5}
            d="M9.172 16.172a4 4 0 015.656 0M9 10h.01M15 10h.01M21 12a9 9 0 11-18 0 9 9 0 0118 0z"
          />
        </svg>
        <h3 className="mt-4 text-lg font-medium text-slate-900">
          Nenhum fornecedor encontrado
        </h3>
        <p className="mt-2 text-sm text-slate-500">
          Não encontramos fornecedores para os critérios informados.
        </p>
      </div>
    );
  }

  if (!hasSearched) {
    return null; // Não renderiza nada antes da primeira busca
  }

  if (!supplierResponse) {
    return null;
  }

  return (
    <div className="mt-12 w-full">
      <SupplierSummary data={supplierResponse} />

      <h2 className="text-2xl font-bold text-slate-900 mb-6 border-b border-slate-200 pb-4">
        Fornecedores Disponíveis ({supplierResponse.suppliers.length})
      </h2>
      <div className="grid grid-cols-1 md:grid-cols-2 gap-6">
        {supplierResponse.suppliers.map((supplier) => (
          <SupplierCard key={supplier.code} supplier={supplier} />
        ))}
      </div>
    </div>
  );
};
