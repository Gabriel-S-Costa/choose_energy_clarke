import React, { useState } from "react";
import { Input } from "@/components/ui/Input";
import { Select } from "@/components/ui/Select";
import { Button } from "@/components/ui/Button";
import { BR_STATES } from "@/utils/constants";

interface SupplierSearchFormProps {
  onSearch: (state: string, consumption: number) => void;
  isLoading?: boolean;
}

export const SupplierSearchForm: React.FC<SupplierSearchFormProps> = ({
  onSearch,
  isLoading = false,
}) => {
  const [selectedState, setSelectedState] = useState("");
  const [consumption, setConsumption] = useState("");

  const handleAction = (_: FormData) => {
    if (selectedState && consumption) {
      onSearch(selectedState, Number(consumption));
    }
  };

  return (
    <form
      action={handleAction}
      className="bg-white p-6 rounded-2xl shadow-xl shadow-slate-200/50 border border-slate-100 w-full"
    >
      <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-4 items-end">
        <Select
          label="Estado"
          options={BR_STATES}
          value={selectedState}
          onChange={(e) => setSelectedState(e.target.value)}
          required
        />
        <Input
          type="number"
          label="Consumo de Energia Mensal"
          placeholder="Ex: 30000 kWh"
          min="1"
          value={consumption}
          onChange={(e) => setConsumption(e.target.value)}
          required
        />
        <Button
          type="submit"
          className="w-full h-10 px-8"
          isLoading={isLoading}
        >
          Buscar Fornecedores
        </Button>
      </div>
    </form>
  );
};
