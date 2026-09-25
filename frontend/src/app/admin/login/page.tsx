"use client";

import { useState } from "react";
import { useRouter } from "next/navigation";
import { api } from "@/lib/api";

export default function AdminLoginPage() {
  const router = useRouter();
  const [email, setEmail] = useState("admin@urimai.tn.gov.in");
  const [password, setPassword] = useState("Admin@Urimai2026!");
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState<string | null>(null);

  const handleLogin = async (e: React.FormEvent) => {
    e.preventDefault();
    setError(null);
    setLoading(true);

    try {
      const res = await api.adminLogin(email, password);
      localStorage.setItem("urimai_token", res.access_token);
      localStorage.setItem("urimai_role", res.user.role);
      localStorage.setItem("urimai_email", res.user.email);
      localStorage.setItem("urimai_name", res.user.name);

      router.push("/admin");
    } catch (err: any) {
      setError(err.message || "Invalid administrator credentials.");
    } finally {
      setLoading(false);
    }
  };

  return (
    <div className="min-h-screen bg-slate-950 flex items-center justify-center p-4 text-slate-100 font-sans">
      <div className="max-w-md w-full bg-slate-900 border border-slate-800 rounded-xl p-8 shadow-2xl">
        <div className="text-center mb-8">
          <div className="inline-block bg-emerald-600/20 text-emerald-400 p-3 rounded-full text-2xl mb-3 border border-emerald-500/30">
            🔒
          </div>
          <h1 className="text-xl font-bold tracking-tight text-white">
            Urimai AI — Admin Portal
          </h1>
          <p className="text-xs text-slate-400 mt-1">
            Restricted State Government Welfare Operations Console
          </p>
        </div>

        {error && (
          <div className="mb-6 p-3 bg-rose-950/80 border border-rose-800 rounded text-rose-300 text-xs">
            {error}
          </div>
        )}

        <form onSubmit={handleLogin} className="space-y-4">
          <div>
            <label className="block text-xs font-semibold text-slate-300 mb-1">
              Admin Email
            </label>
            <input
              type="email"
              value={email}
              onChange={(e) => setEmail(e.target.value)}
              required
              className="w-full bg-slate-950 border border-slate-700 rounded px-3 py-2 text-sm text-white focus:outline-none focus:border-emerald-500 font-mono"
            />
          </div>

          <div>
            <label className="block text-xs font-semibold text-slate-300 mb-1">
              Password
            </label>
            <input
              type="password"
              value={password}
              onChange={(e) => setPassword(e.target.value)}
              required
              className="w-full bg-slate-950 border border-slate-700 rounded px-3 py-2 text-sm text-white focus:outline-none focus:border-emerald-500 font-mono"
            />
          </div>

          <button
            type="submit"
            disabled={loading}
            className="w-full bg-emerald-600 hover:bg-emerald-500 disabled:opacity-50 text-white font-semibold py-2.5 rounded text-sm transition mt-2 shadow-lg shadow-emerald-900/30"
          >
            {loading ? "Authenticating..." : "Sign In to Admin Dashboard"}
          </button>
        </form>

        <div className="mt-8 pt-6 border-t border-slate-800 text-center">
          <a
            href="/"
            className="text-xs text-slate-500 hover:text-slate-300 transition"
          >
            ← Back to Citizen Portal
          </a>
        </div>
      </div>
    </div>
  );
}
