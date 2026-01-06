import { useEffect, useState } from "react";

export default function Results() {
  const [result, setResult] = useState(null);

  useEffect(() => {
    const stored = localStorage.getItem("validation_result");
    if (stored) {
      setResult(JSON.parse(stored));
    }
  }, []);

  if (!result) {
    return (
      <div className="min-h-screen bg-bg flex items-center justify-center text-muted">
        No validation data found.
      </div>
    );
  }

  return (
    <div className="min-h-screen bg-bg p-10 text-white">
      <h1 className="text-4xl font-bold mb-6">Startup Verdict</h1>

      <pre className="bg-black/40 p-6 rounded-xl overflow-auto text-sm">
        {JSON.stringify(result, null, 2)}
      </pre>
    </div>
  );
}
