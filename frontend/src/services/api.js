export async function validateStartup(payload) {
  const res = await fetch("http://127.0.0.1:8000/api/v1/validate", {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify(payload),
  });

  if (!res.ok) {
    throw new Error("Validation failed");
  }

  return res.json();
}
