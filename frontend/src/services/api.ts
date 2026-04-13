const API_URL = import.meta.env.VITE_BASE_URL
const ACCESS_TOKEN = import.meta.env.VITE_ACCESS_TOKEN

export async function makeApiRequest<T>(path: string): Promise<T> {
    const response = await fetch(`${API_URL}/${path}`, {
        headers: { 'X-Request-Token': ACCESS_TOKEN }
    });

    if (!response.ok) {
        throw new Error(`Error fetching ${path}: ${response.statusText}`)
    }

    return response.json()
}