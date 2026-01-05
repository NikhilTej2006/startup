/** @type {import('tailwindcss').Config} */
export default {
  darkMode: "class",
  content: [
    "./index.html",
    "./src/**/*.{js,ts,jsx,tsx}",
  ],
  theme: {
    extend: {
      colors: {
        bg: "#0B0F1A",          // deep navy
        surface: "#111827",     // card background
        muted: "#9CA3AF",
        primary: "#6366F1",     // indigo
        accent: "#22D3EE",      // cyan glow
        success: "#22C55E",
        danger: "#EF4444",
      },
      boxShadow: {
        glow: "0 0 30px rgba(99,102,241,0.35)",
        soft: "0 10px 30px rgba(0,0,0,0.4)",
      },
    },
  },
  plugins: [],
}
