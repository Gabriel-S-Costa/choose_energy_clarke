import React from "react";

interface SelectOption {
  value: string | number;
  label: string;
}

interface SelectProps extends React.SelectHTMLAttributes<HTMLSelectElement> {
  label: string;
  options: SelectOption[];
  error?: string;
}

export const Select: React.FC<SelectProps> = ({
  label,
  options,
  error,
  id,
  className = "",
  ...props
}) => {
  const selectId = id || label.toLowerCase().replace(/\s+/g, "-");

  return (
    <div className={`w-full flex flex-col space-y-1.5 ${className}`}>
      <label
        htmlFor={selectId}
        className="text-sm font-medium text-slate-700 leading-none"
      >
        {label}
      </label>
      <select
        id={selectId}
        className={`
          flex h-10 w-full rounded-md border bg-white px-3 py-2 text-sm text-slate-900 
          focus:outline-none focus:ring-2 focus:ring-emerald-500 focus:border-transparent
          disabled:cursor-not-allowed disabled:opacity-50
          transition-colors
          appearance-none
          ${error ? "border-red-500 focus:ring-red-500" : "border-slate-300"}
        `}
        style={{
          backgroundImage: `url("data:image/svg+xml,%3csvg xmlns='http://www.w3.org/2000/svg' fill='none' viewBox='0 0 20 20'%3e%3cpath stroke='%236b7280' stroke-linecap='round' stroke-linejoin='round' stroke-width='1.5' d='M6 8l4 4 4-4'/%3e%3c/svg%3e")`,
          backgroundPosition: "right 0.5rem center",
          backgroundRepeat: "no-repeat",
          backgroundSize: "1.5em 1.5em",
          paddingRight: "2.5rem",
        }}
        {...props}
      >
        <option value="" disabled hidden>
          Selecione...
        </option>
        {options.map((option) => (
          <option key={option.value} value={option.value}>
            {option.label}
          </option>
        ))}
      </select>
      {error && <span className="text-sm text-red-500 mt-1">{error}</span>}
    </div>
  );
};
