import React from "react";

interface InputProps extends React.InputHTMLAttributes<HTMLInputElement> {
  label: string;
  error?: string;
}

export const Input: React.FC<InputProps> = ({
  label,
  error,
  id,
  className = "",
  ...props
}) => {
  const inputId = id || label.toLowerCase().replace(/\s+/g, "-");

  return (
    <div className={`w-full flex flex-col space-y-1.5 ${className}`}>
      <label
        htmlFor={inputId}
        className="text-sm font-medium text-slate-700 leading-none peer-disabled:cursor-not-allowed peer-disabled:opacity-70"
      >
        {label}
      </label>
      <input
        id={inputId}
        className={`
          flex h-10 w-full rounded-md border bg-white px-3 py-2 text-sm text-slate-900 
          placeholder:text-slate-400 
          focus:outline-none focus:ring-2 focus:ring-emerald-500 focus:border-transparent
          disabled:cursor-not-allowed disabled:opacity-50
          transition-colors
          ${error ? "border-red-500 focus:ring-red-500" : "border-slate-300"}
        `}
        {...props}
      />
      {error && <span className="text-sm text-red-500 mt-1">{error}</span>}
    </div>
  );
};
