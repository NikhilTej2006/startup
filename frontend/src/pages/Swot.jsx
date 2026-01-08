import { useEffect, useState } from "react";
import { useNavigate } from "react-router-dom";

export default function Swot() {
  const navigate = useNavigate();
  const [swot, setSwot] = useState(null);

  useEffect(() => {
    const saved = localStorage.getItem("validation_result");
    if (!saved) {
      navigate("/validate");
      return;
    }
    const parsed = JSON.parse(saved).context.swot;
    setSwot(parsed);
  }, [navigate]);

  if (!swot)
    return <div className="text-white p-10">Loading SWOT...</div>;

  return (
    <div className="min-h-screen bg-bg text-white px-8 py-10">

      {/* Header */}
      <div className="flex justify-between items-center mb-10">
        <h1 className="text-4xl font-bold">SWOT Analysis</h1>

        <button
          onClick={() => navigate("/dashboard")}
          className="px-4 py-2 rounded-lg bg-black/40 border border-white/10 hover:bg-white/10 transition"
        >
          ← Back to Dashboard
        </button>
      </div>

      {/* SWOT GRID */}
      <div className="grid md:grid-cols-2 gap-8">

        <SwotCard
          title="Strengths"
          color="text-green-400"
          items={swot.strengths}
        />

        <SwotCard
          title="Weaknesses"
          color="text-red-400"
          items={swot.weaknesses}
        />

        <SwotCard
          title="Opportunities"
          color="text-blue-400"
          items={swot.opportunities}
        />

        <SwotCard
          title="Threats"
          color="text-yellow-400"
          items={swot.threats}
        />
      </div>

      {/* Confidence Score */}
      <div className="mt-12 bg-surface rounded-2xl p-6 border border-white/10 backdrop-blur">
        <h2 className="text-2xl font-semibold mb-3">Confidence Level</h2>

        <p className="text-3xl font-bold text-primary">
          {swot.confidence_level ?? "N/A"}
        </p>

        <p className="text-muted mt-2">
          Higher confidence = stronger reliability of SWOT analysis.
        </p>
      </div>
    </div>
  );
}

/* ---- Reusable SWOT Card ---- */
function SwotCard({ title, color, items }) {
  return (
    <div className="bg-surface border border-white/10 rounded-2xl p-6 backdrop-blur">
      <h2 className={`text-2xl font-semibold mb-3 ${color}`}>{title}</h2>

      {items && items.length > 0 ? (
        <ul className="space-y-2 text-muted">
          {items.map((item, i) => (
            <li key={i}>• {item}</li>
          ))}
        </ul>
      ) : (
        <p className="text-muted">No data available</p>
      )}
    </div>
  );
}
