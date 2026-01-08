import { useEffect, useState } from "react";
import { useNavigate } from "react-router-dom";

export default function Dashboard() {
  const navigate = useNavigate();
  const [data, setData] = useState(null);

  useEffect(() => {
    const saved = localStorage.getItem("validation_result");
    if (!saved) {
      navigate("/validate");
      return;
    }
    setData(JSON.parse(saved).context);
  }, [navigate]);

  if (!data) return <div className="text-white p-10">Loading...</div>;

  return (
    <div className="min-h-screen bg-bg text-white px-8 py-10">
      <h1 className="text-4xl font-bold mb-6">Startup Validation Dashboard</h1>

      {/* ========= SUMMARY GRID ========= */}
      <div className="grid md:grid-cols-3 gap-6 mb-10">

        {/* Verdict Card */}
        <div className="bg-surface p-6 rounded-2xl border border-white/10">
          <h2 className="text-xl font-semibold mb-2">Final Verdict</h2>
          <p className={`text-3xl font-black ${
            data.verdict?.verdict === "GO"
              ? "text-green-400"
              : data.verdict?.verdict === "PIVOT"
              ? "text-yellow-400"
              : "text-red-400"
          }`}>
            {data.verdict?.verdict}
          </p>
          <p className="text-sm text-muted mt-2">
            Confidence: {data.verdict?.confidence_score}
          </p>
        </div>

        {/* Market Score */}
        <div className="bg-surface p-6 rounded-2xl border border-white/10">
          <h2 className="text-xl font-semibold mb-2">Market Score</h2>
          <p className="text-3xl font-black text-blue-400">
            {data.market_score || "N/A"}
          </p>
        </div>

        {/* Competition Score */}
        <div className="bg-surface p-6 rounded-2xl border border-white/10">
          <h2 className="text-xl font-semibold mb-2">Competition Score</h2>
          <p className="text-3xl font-black text-purple-400">
            {data.competition_score || "N/A"}
          </p>
        </div>
      </div>

      {/* ========= MAIN DETAILS ========= */}
      <div className="grid lg:grid-cols-2 gap-8">

        {/* Reasoning */}
        <div className="bg-surface p-6 rounded-2xl border border-white/10">
          <h2 className="text-2xl font-semibold mb-3">Verdict Reasoning</h2>
          <p className="text-muted">{data.verdict?.reasoning || "No reasoning found."}</p>
        </div>

        {/* Core Idea & Domain */}
        <div className="bg-surface p-6 rounded-2xl border border-white/10">
          <h2 className="text-2xl font-semibold mb-3">Idea Overview</h2>

          <p><span className="font-bold text-primary">Idea:</span> {data.idea}</p>
          <p className="mt-2">
            <span className="font-bold text-primary">Domain:</span> {data.domain}
          </p>
          <p className="mt-2">
            <span className="font-bold text-primary">Target Users:</span> {data.target_users}
          </p>
        </div>
      </div>

      {/* ========= NAVIGATION TO NEXT PHASES ========= */}
      <h2 className="text-3xl font-bold mt-12 mb-4">Detailed Reports</h2>

      <div className="grid md:grid-cols-3 gap-6">
        <DashboardButton label="Market Analysis" to="/market" />
        <DashboardButton label="Competition" to="/competition" />
        <DashboardButton label="SWOT" to="/swot" />
        <DashboardButton label="Financials" to="/financials" />
        <DashboardButton label="Roadmap" to="/roadmap" />
        <DashboardButton label="MVP" to="/mvp" />
        <DashboardButton label="Tech Stack" to="/techstack" />
        <DashboardButton label="Execution Plan" to="/execution" />
        <DashboardButton label="Pitch Deck" to="/pitchdeck" />
      </div>
    </div>
  );
}


function DashboardButton({ label, to }) {
  const navigate = useNavigate();
  return (
    <button
      onClick={() => navigate(to)}
      className="bg-black/40 border border-white/10 rounded-xl p-5 text-left hover:bg-white/10 transition"
    >
      <p className="text-lg font-semibold">{label}</p>
      <p className="text-sm text-muted">View details →</p>
    </button>
  );
}
