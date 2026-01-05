import { useState } from "react";
import { useNavigate } from "react-router-dom";
import { validateStartup } from "../services/api";

export default function Validate() {
  const navigate = useNavigate();
  const [idea, setIdea] = useState("");
  const [domain, setDomain] = useState("");
  const [loading, setLoading] = useState(false);

  async function handleSubmit() {
    if (!idea || !domain) return;

    setLoading(true);
    try {
      const result = await validateStartup({
        idea,
        domain,
        target_users: "General",
      });

      // save response for dashboard
      localStorage.setItem("validation_result", JSON.stringify(result));
      navigate("/dashboard");
    } catch (e) {
      alert("Validation failed");
    } finally {
      setLoading(false);
    }
  }

  return (
    <div className="min-h-screen bg-bg flex items-center justify-center px-6">
      <div className="max-w-xl w-full bg-surface border border-white/10 rounded-2xl p-8 backdrop-blur">
        <h2 className="text-3xl font-bold mb-6 text-center">
          Validate Your Startup Idea
        </h2>

        <label className="block text-sm text-muted mb-2">Startup Idea</label>
        <textarea
          className="w-full mb-4 rounded-xl bg-black/40 border border-white/10 p-3 focus:outline-none focus:ring-2 focus:ring-primary"
          rows={4}
          value={idea}
          onChange={(e) => setIdea(e.target.value)}
          placeholder="AI-powered delivery drones for medical logistics"
        />

        <label className="block text-sm text-muted mb-2">Domain</label>
        <input
          className="w-full mb-6 rounded-xl bg-black/40 border border-white/10 p-3 focus:outline-none focus:ring-2 focus:ring-primary"
          value={domain}
          onChange={(e) => setDomain(e.target.value)}
          placeholder="Logistics / Healthcare"
        />

        <button
          onClick={handleSubmit}
          disabled={loading}
          className="w-full py-3 rounded-xl bg-primary hover:bg-indigo-500 transition shadow-glow"
        >
          {loading ? "Running AI Agents..." : "Run Validation"}
        </button>
      </div>
    </div>
  );
}
