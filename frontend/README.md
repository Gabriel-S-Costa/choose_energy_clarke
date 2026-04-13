# Choose Energy Clarke — Frontend

Front-end do desafio Clarke Energia: uma interface em React + TypeScript criada com Vite, para pesquisar e comparar fornecedores de energia e estimar economia por solução.

**Destaques**
- Interface em React + TypeScript
- Build rápida com Vite
- Integração com API para listagem e filtro de fornecedores

## Tecnologias

- React
- TypeScript
- Vite
- Tailwind CSS

> Dependências principais: `react`, `react-dom`, `react-router`, `tailwindcss`.

## Estrutura do projeto (resumo)

```
src/
  App.tsx
  main.tsx
  assets/          # Imagens e recursos estáticos
  components/      # Componentes reutilizáveis (ui/, layout/)
  features/        # Features por domínio (e.g. suppliers/)
  pages/           # Páginas da aplicação
  services/        # Chamadas à API
  utils/           # Funções utilitárias e formatadores
```

## Como rodar (Desenvolvimento)

Instale dependências e execute o servidor de desenvolvimento:

```bash
npm install
npm run dev
```

Abra http://localhost:5173 (ou a URL exibida pelo Vite).

## Build e Preview

Gerar build de produção:

```bash
npm run build
```

Verificar build localmente:

```bash
npm run preview
```

## Scripts úteis

- `npm run dev` — servidor de desenvolvimento
- `npm run build` — compila para produção (`tsc -b && vite build`)
- `npm run preview` — preview do build
- `npm run lint` — rodar ESLint

## Boas práticas e dicas

- Use o `features/` para organizar lógica de domínio (hooks, components, types por feature).
- Favor componentes pequenos e testes unitários para lógica crítica.
