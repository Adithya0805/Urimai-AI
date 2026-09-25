"use client";

import { useEffect, useState } from "react";
import Link from "next/link";
import { api, DashboardStats } from "@/lib/api";

export default function AdminOverviewPage() {
  const [stats, setStats] = useState<DashboardStats | null>(null);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState<string | null>(null);
  const [actionMsg, setActionMsg] = useState<string | null>(null);

  const loadStats = async () => {
    try {
      setLoading(true);
      setError(null);
      const data = await api.getAdminStats();
      setStats(data);
    } catch (err: any) {
      setError(err.message || "Failed to load dashboard statistics.");
    } finally {
      setLoading(false);
    }
  };

  useEffect(() => {
    loadStats();
  }, []);

  const handleRunFreshness = async () => {
    try {
      setActionMsg("Running freshness inspection across schemes...");
      const res = await api.triggerAdminFreshnessCheck(180);
      setActionMsg(
        `Freshness scan complete: ${res.total_schemes_checked} checked, ${res.stale_schemes_flagged} flagged stale.`
      );
      loadStats();
    } catch (err: any) {
      setError(err.message);
    }
  };

  const handleRunFollowups = async () => {
    try {
      setActionMsg("Executing follow-up agent cycle for pending applications...");
      const res = await api.triggerAdminFollowups(7);
      setActionMsg(
        `Follow-up cycle complete: ${res.total_applications_checked} checked, ${res.notifications_created} reminders generated.`
      );
      loadStats();
    } catch (err: any) {
      setError(err.message);
    }
  };

  if (loading && !stats) {
    return (
      <div className="py-16 text-center text-slate-400">
        <div className="inline-block animate-spin text-3xl mb-3">⚙️</div>
        <div>Loading Operations Console...</div>
      </div>
    );
  }

  return (
    <div className="space-y-6">
      {/* Top Banner & Trigger Actions */}
      <div className="flex flex-col sm:flex-row sm:items-center justify-between gap-4 bg-slate-950 p-4 rounded-xl border border-slate-800">
        <div>
          <h1 className="text-xl font-bold text-white">Operations Overview</h1>
          <p className="text-xs text-slate-400">
            Real-time welfare scheme eligibility matching and lifecycle metrics
          </p>
        </div>

        <div className="flex items-center gap-2">
          <button
            onClick={handleRunFreshness}
            className="bg-amber-600 hover:bg-amber-500 text-white text-xs font-semibold px-3.5 py-2 rounded transition shadow"
          >
            🔄 Run Freshness Scan
          </button>
          <button
            onClick={handleRunFollowups}
            className="bg-indigo-600 hover:bg-indigo-500 text-white text-xs font-semibold px-3.5 py-2 rounded transition shadow"
          >
            📬 Trigger Follow-ups
          </button>
        </div>
      </div>

      {actionMsg && (
        <div className="p-3 bg-emerald-950/70 border border-emerald-800 rounded text-emerald-300 text-xs flex justify-between items-center">
          <span>{actionMsg}</span>
          <button onClick={() => setActionMsg(null)} className="text-slate-400 hover:text-white">
            ✕
          </button>
        </div>
      )}

      {error && (
        <div className="p-3 bg-rose-950/70 border border-rose-800 rounded text-rose-300 text-xs">
          {error}
        </div>
      )}

      {/* Stats Cards Grid */}
      {stats && (
        <div className="grid grid-cols-2 md:grid-cols-3 lg:grid-cols-6 gap-4">
          <div className="bg-slate-950 border border-slate-800 rounded-lg p-4">
            <div className="text-xs text-slate-400 font-medium">Families Onboarded</div>
            <div className="text-2xl font-black text-emerald-400 mt-1">
              {stats.total_families}
            </div>
            <div className="text-[10px] text-slate-500 mt-1">Registered households</div>
          </div>

          <div className="bg-slate-950 border border-slate-800 rounded-lg p-4">
            <div className="text-xs text-slate-400 font-medium">Total Citizens</div>
            <div className="text-2xl font-black text-sky-400 mt-1">
              {stats.total_persons}
            </div>
            <div className="text-[10px] text-slate-500 mt-1">Individual profiles</div>
          </div>

          <div className="bg-slate-950 border border-slate-800 rounded-lg p-4">
            <div className="text-xs text-slate-400 font-medium">Active Schemes</div>
            <div className="text-2xl font-black text-indigo-400 mt-1">
              {stats.active_schemes_count}
            </div>
            <div className="text-[10px] text-slate-500 mt-1">Across 4 departments</div>
          </div>

          <div className="bg-slate-950 border border-amber-900/40 rounded-lg p-4">
            <div className="text-xs text-amber-400 font-medium">Stale Review Queue</div>
            <div className="text-2xl font-black text-amber-400 mt-1">
              {stats.stale_schemes_count}
            </div>
            <Link
              href="/admin/review-queue"
              className="text-[10px] text-amber-300 hover:underline mt-1 inline-block"
            >
              View queue →
            </Link>
          </div>

          <div className="bg-slate-950 border border-rose-900/40 rounded-lg p-4">
            <div className="text-xs text-rose-400 font-medium">Stuck Applications</div>
            <div className="text-2xl font-black text-rose-400 mt-1">
              {stats.stuck_applications_count}
            </div>
            <Link
              href="/admin/applications"
              className="text-[10px] text-rose-300 hover:underline mt-1 inline-block"
            >
              Inspect bottlenecks →
            </Link>
          </div>

          <div className="bg-slate-950 border border-slate-800 rounded-lg p-4">
            <div className="text-xs text-slate-400 font-medium">Intake Turns</div>
            <div className="text-2xl font-black text-slate-200 mt-1">
              {stats.total_extractions_logged}
            </div>
            <div className="text-[10px] text-slate-500 mt-1">
              {stats.recent_errors_count} failed parses
            </div>
          </div>
        </div>
      )}

      {/* Schemes With Zero Matches Alert Table */}
      <div className="bg-slate-950 border border-slate-800 rounded-xl overflow-hidden">
        <div className="p-4 border-b border-slate-800 flex items-center justify-between">
          <div>
            <h2 className="text-sm font-bold text-slate-200 flex items-center gap-2">
              <span>⚠️ Miscalibration Signal:</span> Schemes With Zero Tracked Matches
            </h2>
            <p className="text-xs text-slate-400 mt-0.5">
              Schemes where eligibility rules may be overly restrictive or requiring threshold recalibration.
            </p>
          </div>
          <Link
            href="/admin/rules"
            className="text-xs text-emerald-400 hover:underline font-semibold"
          >
            Review Rules →
          </Link>
        </div>

        <div className="overflow-x-auto">
          <table className="w-full text-left text-xs">
            <thead className="bg-slate-900 text-slate-400 border-b border-slate-800 uppercase tracking-wider font-semibold">
              <tr>
                <th className="py-2.5 px-4">Scheme Code</th>
                <th className="py-2.5 px-4">Scheme Name (Tamil & English)</th>
                <th className="py-2.5 px-4">Department</th>
                <th className="py-2.5 px-4">Rules Attached</th>
                <th className="py-2.5 px-4 text-right">Action</th>
              </tr>
            </thead>
            <tbody className="divide-y divide-slate-800/60 font-mono text-slate-300">
              {stats?.schemes_zero_matches && stats.schemes_zero_matches.length > 0 ? (
                stats.schemes_zero_matches.map((item) => (
                  <tr key={item.scheme_id} className="hover:bg-slate-900/40 transition">
                    <td className="py-3 px-4 font-bold text-amber-300">{item.scheme_code}</td>
                    <td className="py-3 px-4 font-sans">
                      <div className="font-semibold text-slate-100">{item.name_tamil}</div>
                      <div className="text-[11px] text-slate-400">{item.name_english}</div>
                    </td>
                    <td className="py-3 px-4 font-sans">{item.department}</td>
                    <td className="py-3 px-4">{item.rules_count} conditions</td>
                    <td className="py-3 px-4 text-right font-sans">
                      <Link
                        href="/admin/rules"
                        className="bg-slate-800 hover:bg-slate-700 text-slate-200 px-2.5 py-1 rounded text-xs transition"
                      >
                        Inspect Rules
                      </Link>
                    </td>
                  </tr>
                ))
              ) : (
                <tr>
                  <td colSpan={5} className="py-6 text-center text-slate-500 font-sans">
                    ✓ All active schemes have active matching activity.
                  </td>
                </tr>
              )}
            </tbody>
          </table>
        </div>
      </div>
    </div>
  );
}
