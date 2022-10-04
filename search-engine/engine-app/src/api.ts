import axios from 'axios';

export const api = axios.create({
  baseURL: 'http://localhost:5001/',
});

export async function searchMutation(query: string) {
  const response = await api.get('/search/', { params: { query } })
  return response.data;
}

export async function advancedSearchMutation(marca: string, memoria: string, armazenamento: string) {
  const response = await api.get('/advanced-search/', { params: { marca, memoria, armazenamento } })
  return response.data;
}