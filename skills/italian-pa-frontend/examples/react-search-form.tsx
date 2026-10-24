// Esempio semantico minimo. NON è un componente ufficiale di Design React Kit.
import { useState, type FormEvent } from 'react';

type SearchFormProps = { onSearch: (query: string) => void };

export function SearchForm({ onSearch }: SearchFormProps) {
  const [query, setQuery] = useState('');
  function submit(event: FormEvent<HTMLFormElement>) {
    event.preventDefault();
    onSearch(query.trim());
  }
  return (
    <form role="search" onSubmit={submit}>
      <label htmlFor="pa-search">Cerca nel portale</label>
      <input id="pa-search" type="search" value={query}
        onChange={event => setQuery(event.target.value)} />
      <button type="submit">Cerca</button>
    </form>
  );
}
