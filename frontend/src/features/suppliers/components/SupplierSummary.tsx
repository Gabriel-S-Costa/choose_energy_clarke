import React from "react";
import type { SupplierResponse } from "@/features/suppliers/types";
import { convertToBRL } from "@/utils/formatters";
import { typeLabels } from "@/utils/constants";

interface SupplierSummaryProps {
  data: SupplierResponse;
}

export const SupplierSummary: React.FC<SupplierSummaryProps> = ({ data }) => {
  return (
    <div className="grid grid-cols-1 md:grid-cols-3 gap-4 mb-8">
      <div className="bg-white p-5 rounded-2xl border border-slate-200 shadow-sm flex flex-col justify-center">
        <h4 className="text-xs font-semibold text-slate-500 uppercase tracking-wide">
          Custo Base (Sem desconto)
        </h4>
        <p className="mt-2 text-2xl font-bold text-slate-800">
          {convertToBRL(data.state_base_cost || 0)}
        </p>
      </div>
      <div className="bg-white p-5 rounded-2xl border border-slate-200 shadow-sm flex flex-col justify-center">
        <h4 className="text-xs font-semibold text-slate-500 uppercase tracking-wide mb-3">
          Modalidades Encontradas
        </h4>
        <div className="flex flex-wrap gap-2">
          {data.available_types.map((t) => (
            <span
              key={t}
              className="px-2.5 py-1 bg-slate-100 text-slate-700 text-xs font-bold rounded-md uppercase"
            >
              {typeLabels[t] || t.replace("_", " ")}
            </span>
          ))}
        </div>
      </div>
      <div className="bg-white p-5 rounded-2xl border border-emerald-200 shadow-sm bg-emerald-50/30 flex flex-col justify-center">
        <h4 className="text-xs font-semibold text-emerald-800 uppercase tracking-wide mb-3">
          Potencial de Economia
        </h4>
        <div className="flex flex-col space-y-2">
          {Object.entries(data.estimated_savings_per_type).map(([type, savings]) => (
            <div key={type} className="flex justify-between items-center text-sm">
              <span className="text-slate-600 font-medium">
                {typeLabels[type] || type.replace("_", " ")}:
              </span>
              <span className="font-bold text-emerald-600">
                {convertToBRL(savings)}
              </span>
            </div>
          ))}
        </div>
      </div>
    </div>
  );
};
