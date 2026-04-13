import React from "react";
import type { Supplier } from "@/features/suppliers/types";
import { convertToBRL } from "@/utils/formatters";
import { typeLabels } from "@/utils/constants";

interface SupplierCardProps {
  supplier: Supplier;
}

export const SupplierCard: React.FC<SupplierCardProps> = ({ supplier }) => {
  return (
    <div className="bg-white rounded-2xl border border-slate-200 p-6 flex flex-col hover:shadow-lg transition-all hover:border-emerald-200 overflow-hidden relative group">
      <div className="absolute top-0 left-0 w-full h-1 bg-gradient-to-r from-emerald-400 to-teal-500 opacity-0 group-hover:opacity-100 transition-opacity" />

      <div className="flex items-center justify-between mb-4">
        <div className="flex items-center space-x-4">
          {supplier.logo ? (
            <img
              src={supplier.logo}
              alt={`Logo ${supplier.name}`}
              className="w-12 h-12 rounded-full object-cover border border-slate-100"
            />
          ) : (
            <div className="w-12 h-12 rounded-full bg-emerald-100 text-emerald-600 flex items-center justify-center font-bold text-lg">
              {supplier.name.charAt(0)}
            </div>
          )}
          <div>
            <h3 className="font-semibold text-slate-900 text-lg">
              {supplier.name}
            </h3>
            {supplier.states.map((state) => (
              <span className="text-xs font-medium px-2 py-1 bg-slate-100 text-slate-600 rounded-full mr-1">
                {state}
              </span>
            ))}
          </div>
        </div>
        <div className="flex bg-amber-50 px-2 py-1 rounded-md items-center shadow-sm border border-amber-100">
          <span className="text-amber-500 text-sm font-bold mr-1">★</span>
          <span className="text-amber-700 text-sm font-medium">
            {supplier.avg_rating.toFixed(1)}
          </span>
        </div>
      </div>

      <div className="grid grid-cols-2 gap-4 mt-2">
        <div className="flex flex-col col-span-2">
          <span className="text-xs text-slate-500 mb-1">Clientes Atendidos</span>
          <span className="font-semibold text-slate-900">
            {new Intl.NumberFormat("pt-BR").format(Number(supplier.total_client) || 0)}
          </span>
        </div>
      </div>

      <div className="mt-4 pt-4 border-t border-slate-100 flex flex-col space-y-3">
          <h4 className="text-sm font-bold text-slate-800">Ofertas de Economia</h4>
          {supplier.offers?.map((offer, index) => (
            <div key={index} className="bg-emerald-50 rounded-lg p-3 border border-emeral-100">
              <div className="flex justify-between items-center mb-2">
                <span className="text-xs font-semibold text-emeral-800 uppercase">
                  {typeLabels[offer.type] || offer.type.replace('_', ' ')}
                </span>
                <span className="text-xs font-bold bg-emerald-200 text-emerald-800 px-2 py-0.5 rounded-full">
                  {offer.percentage_savings} %
                </span>
              </div>

              <div className="grid grid-cols-2 gap-2 text-sm mt-2">
                <div className="flex flex-col">
                  <span className="text-xs text-emerald-600">Custo Estimado:</span>
                  <span className="font-semibold text-slate-900">
                    {convertToBRL(offer.estimated_cost) || 0.0}
                  </span>
                </div>
                <div className="flex flex-col">
                  <span className="text-xs text-emerald-600">Economia Estimada:</span>
                  <span className="font-semibold text-slate-900">
                    {convertToBRL(offer.estimated_savings) || 0.0}
                  </span>
                </div>
              </div>
            </div>
          ))}
          {(!supplier.offers || supplier.offers.length === 0) && (
            <div className="text-sm text-slate-500 text-center py-2">
              Nenhuma oferta mapeada no momento.
            </div>
          )}
      </div>
        
      {/* <button className="mt-6 w-full py-2 bg-emerald-50 text-emerald-700 rounded-lg font-medium hover:bg-emerald-100 transition-colors">
        Ver Detalhes
      </button> */}
    </div>
  );
};
