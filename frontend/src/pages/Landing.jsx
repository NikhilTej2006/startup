import { useNavigate } from "react-router-dom";

export default function Landing() {
  const navigate = useNavigate();

  return (
    <div className="min-h-screen relative overflow-hidden bg-bg flex items-center justify-center">
      {/* Background glow */}
      <div className="absolute inset-0 -z-10">
        <div className="absolute top-[-20%] left-[-10%] w-[500px] h-[500px] bg-indigo-500/10 rounded-full blur-[120px]" />
        <div className="absolute bottom-[-20%] right-[-10%] w-[500px] h-[500px] bg-purple-500/10 rounded-full blur-[120px]" />
      </div>

      <div className="text-center max-w-3xl px-6">
        <div className="inline-block mb-6 px-4 py-1 rounded-full bg-surface border border-white/10 text-sm text-muted backdrop-blur">
          AI Startup Validation Platform
        </div>

        <h1 className="text-5xl md:text-6xl font-bold leading-tight tracking-tight">
          Validate Your Startup
          <span className="block text-primary drop-shadow-glow">
            Before You Build It
          </span>
        </h1>

        <p className="mt-6 text-lg text-muted">
          Multi-agent AI that analyzes market, competition, risk,
          fundability, and survivability — end-to-end.
        </p>

        <div className="mt-10 flex flex-wrap justify-center gap-4">
          {/* ✅ Navigate to Validate Page */}
          <button
            onClick={() => navigate("/validate")}
            className="px-6 py-3 rounded-xl bg-primary hover:bg-indigo-500 transition-all duration-200 shadow-glow hover:scale-[1.02]"
          >
            Validate Idea
          </button>

          {/* ✅ Navigate to Dashboard */}
          <button
            onClick={() => navigate("/dashboard")}
            className="px-6 py-3 rounded-xl border border-white/20 hover:bg-white/5 transition-all duration-200"
          >
            View Sample Report
          </button>
        </div>
      </div>
    </div>
  );
}
