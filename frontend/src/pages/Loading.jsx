import { useEffect } from "react";
import { useLocation, useNavigate } from "react-router-dom";
import { validateStartup } from "../services/api";

export default function Loading() {
  const { state } = useLocation();
  const navigate = useNavigate();

  useEffect(() => {
    async function run() {
      const data = await validateStartup(state.idea);
      navigate("/results", { state: data });
    }
    run();
  }, []);

  return (
    <div className="min-h-screen bg-bg flex items-center justify-center text-center">
      <div>
        <h2 className="text-3xl font-bold mb-4">Analyzing your startup…</h2>
        <p className="text-muted">Market • Competition • Risk • Fundability</p>
      </div>
    </div>
  );
}
