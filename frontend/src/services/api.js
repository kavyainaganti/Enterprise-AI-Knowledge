const API_BASE_URL = import.meta.env.VITE_API_BASE_URL || "http://127.0.0.1:8000";

export async function sendChatQuestion(question) {
  const response = await fetch(`${API_BASE_URL}/api/chat`, {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify({ question, top_k: 5 }),
  });

  const data = await response.json().catch(() => ({}));
  if (!response.ok) {
    throw new Error(data.detail || `Backend request failed (${response.status})`);
  }
  return data;
}

export async function checkBackendHealth() {
  const response = await fetch(`${API_BASE_URL}/api/health`);
  if (!response.ok) throw new Error("Backend health check failed");
  return response.json();
}
