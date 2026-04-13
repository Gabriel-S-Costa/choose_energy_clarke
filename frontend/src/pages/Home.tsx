import React, { useState } from "react";
import { SupplierSearchForm } from "@/features/suppliers/components/SupplierSearchForm";
import { SupplierList } from "@/features/suppliers/components/SupplierList";
import { useSuppliers } from "@/features/suppliers/hooks/useSuppliers";

export const Home: React.FC = () => {
  const { supplierResponse, isLoading, error, fetchSuppliers } = useSuppliers();
  const [hasSearched, setHasSearched] = useState(false);

  const handleSearch = (state: string, consumption: number) => {
    setHasSearched(true);
    fetchSuppliers(state, consumption);
  };

  return (
    <div className="min-h-screen bg-slate-50 font-sans selection:bg-emerald-200">

      <header className="bg-emerald-700 text-white pt-16 pb-32 px-4 relative overflow-hidden">
        <div className="absolute inset-0 bg-[url('https://www.transparenttextures.com/patterns/cubes.png')] opacity-10 mix-blend-overlay"></div>
        <div className="max-w-4xl mx-auto text-center relative z-10">
          <h1 className="text-4xl md:text-5xl font-extrabold tracking-tight mb-4 drop-shadow-md">
            Choose your Energy
          </h1>
          <p className="text-emerald-100 text-lg md:text-xl max-w-2xl mx-auto">
            Descubra os melhores fornecedores de energia do Brasil com base no
            seu consumo e localização. Economize de forma inteligente.
          </p>
        </div>
      </header>

      <main className="max-w-5xl mx-auto px-4 sm:px-6 lg:px-8 -mt-16 pb-24 relative z-20">
        <SupplierSearchForm onSearch={handleSearch} isLoading={isLoading} />
        
        {error && (
          <div className="mt-8 p-4 bg-red-50 border-l-4 border-red-500 text-red-700 rounded-md max-w-2xl mx-auto flex items-start shadow-sm">
            <svg className="w-5 h-5 mr-3 mt-0.5 text-red-500 flex-shrink-0" fill="currentColor" viewBox="0 0 20 20" xmlns="http://www.w3.org/2000/svg"><path fillRule="evenodd" d="M10 18a8 8 0 100-16 8 8 0 000 16zM8.707 7.293a1 1 0 00-1.414 1.414L8.586 10l-1.293 1.293a1 1 0 101.414 1.414L10 11.414l1.293 1.293a1 1 0 001.414-1.414L11.414 10l1.293-1.293a1 1 0 00-1.414-1.414L10 8.586 8.707 7.293z" clipRule="evenodd"></path></svg>
            <p>{error}</p>
          </div>
        )}

        <SupplierList
          supplierResponse={supplierResponse}
          isLoading={isLoading}
          hasSearched={hasSearched}
        />
      </main>
    </div>
  );
};
