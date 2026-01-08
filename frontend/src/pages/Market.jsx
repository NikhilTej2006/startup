import { useEffect, useState } from "react";
import { useNavigate } from "react-router-dom";

export default function Market() {
  const navigate = useNavigate();
  const [data, setData] = useState(null);

  useEffect(() => {
    const saved = localStorage.getItem("validation_result");
    if (!saved) {
      navigate("/validate");
      return;
    }
    const parsed = JSON.parse(saved).context;
    setData(parsed);
  }, [navigate]);

  if (!data) return <div className="text-white p-10">Loading...</div>;

  return (
    <div className="min-h-screen bg-bg text-white px-8 py-10">
      {/* Header */}
      <div className="flex justify-between items-center mb-10">
        <h1 className="text-4xl font-bold">Market Analysis</h1>

        <button
          onClick={() => navigate("/dashboard")}
          className="px-4 py-2 rounded-lg bg-black/40 border border-white/10 hover:bg-white/10 transition"
        >
          ← Back to Dashboard
        </button>
      </div>

      {/* Grid Section */}
      <div className="grid md:grid-cols-2 lg:grid-cols-3 gap-8">

        {/* Market Score */}
        <Card title="Market Score">
          <p className="text-4xl font-black text-primary">
            {data.market_score || "N/A"}
          </p>
          <p className="text-muted text-sm mt-2">
            Higher score = better market demand
          </p>
        </Card>

        {/* Market Maturity */}
        <Card title="Market Maturity">
          <p className="text-3xl font-semibold text-blue-400">
            {data.competition?.market_maturity || "Unknown"}
          </p>
        </Card>

        {/* Entry Barriers */}
        <Card title="Entry Barriers">
          <p className="text-3xl font-semibold text-red-400">
            {data.competition?.entry_barriers || "Unknown"}
          </p>
        </Card>
      </div>

      {/* Market Sentiment */}
      <Card className="mt-10" title="Market Sentiment (NLP / LLM Analysis)">
        <p className="text-lg text-muted">
          The Market Agent analyzed multiple signals (news, trends, AI sentiment)
          to derive the score.
        </p>
        <div className="mt-4 p-4 bg-black/40 rounded-lg border border-white/5">
          <p className="text-2xl font-bold text-indigo-400">
            Sentiment: {data.market?.sentiment || "0.20"}
          </p>
          <p className="text-xl text-purple-300 mt-2">
            Demand: {data.market?.demand || "Medium Demand"}
          </p>
        </div>
      </Card>

      {/* Insights */}
      <Card className="mt-10" title="AI Insights">
        <ul className="space-y-3 text-muted">
          <li>• Market is currently evolving with strong potential.</li>
          <li>• Demand for AI-powered automation is rising.</li>
          <li>• Early players can establish dominance quickly.</li>
          <li>• Strong need for differentiated AI execution strategy.</li>
        </ul>
      </Card>
    </div>
  );
}

/* ---- Reusable Card Component ---- */
function Card({ title, children, className }) {
  return (
    <div
      className={`bg-surface border border-white/10 rounded-2xl p-6 backdrop-blur ${className}`}
    >
      <h2 className="text-2xl font-semibold mb-3">{title}</h2>
      {children}
    </div>
  );
}
