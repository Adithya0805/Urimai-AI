"use client";

import { useEffect, useState } from "react";
import { api, StuckApplication } from "@/lib/api";

export default function AdminStuckApplicationsPage() {
  const [apps, setApps] = useState<StuckApplication[]>([]);
  const [daysThreshold, setDaysThreshold] = useState(7);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState<string | null>(null);

  const loadStuckApps = async () => {
    try {
      setLoading(true);
      setError(null);
      const data = await api.getAdminStuckApplications(daysThreshold);
      setApps(data);
    } catch (err: any) {
      setError(err.message || "Failed to load stuck applications.");
    } finally {
      setLoading(false);
    }
  };

  useEffect(() => {
    loadStuckApps();
  }, [daysThreshold]);

  return (
    <div className="space-y-6">
      <div className="flex flex-col sm:flex-row sm:items-center justify-between gap-4">
        <div>
          <h1 className="text-xl font-bold text-white">⏳ Stuck Application Bottlenecks</h1>
          <p className="text-xs text-slate-400">
            Citizen applications stalled in &apos;documents_pending&apos; or &apos;renewal_due&apos;.
          </p>
        </div>

        <div className="flex items-center gap-3">
          <label className="text-xs text-slate-400">Filter pending &gt;:</label>
          <select
            value={daysThreshold}
            onChange={(e) => setDaysThreshold(Number(e.target.value))}
            className="bg-slate-950 border border-slate-700 text-slate-200 text-xs rounded px-2.5 py-1.5"
          >
            <option value={3}>3 Days</option>
            <option value={7}>7 Days (Standard)</option>
            <option value={14}>14 Days</option>
            <option value={30}>30 Days</option>
          </select>
          <button
            onClick={loadStuckApps}
            className="bg-slate-800 hover:bg-slate-700 text-slate-300 text-xs px-3 py-1.5 rounded transition"
          >
            Refresh
          </button>
        </div>
      </div>

      {error && (
        <div className="p-3 bg-rose-950/70 border border-rose-800 rounded text-rose-300 text-xs">
          {error}
        </div>
      )}

      {/* Stuck Applications Table */}
      <div className="bg-slate-950 border border-slate-800 rounded-xl overflow-hidden">
        <div className="overflow-x-auto">
          <table className="w-full text-left text-xs">
            <thead className="bg-slate-900 text-slate-400 border-b border-slate-800 uppercase tracking-wider font-semibold">
              <tr>
                <th className="py-3 px-4">Citizen & District</th>
                <th className="py-3 px-4">Scheme</th>
                <th className="py-3 px-4">Status</th>
                <th className="py-3 px-4">Days Pending</th>
                <th className="py-3 px-4">Missing Documents</th>
                <th className="py-3 px-4">Action Note</th>
              </tr>
            </thead>
            <tbody className="divide-y divide-slate-800/60 text-slate-300">
              {loading ? (
                <tr>
                  <td colSpan={6} className="py-8 text-center text-slate-500">
                    Loading stalled applications...
                  </td>
                </tr>
              ) : apps.length === 0 ? (
                <tr>
                  <td colSpan={6} className="py-8 text-center text-emerald-400 font-semibold">
                    ✓ No applications currently stuck beyond {daysThreshold} days.
                  </td>
                </tr>
              ) : (
                apps.map((app) => (
                  <tr key={app.id} className="hover:bg-slate-900/40 transition">
                    <td className="py-3 px-4">
                      <div className="font-semibold text-slate-100">{app.person_name}</div>
                      <div className="text-[10px] text-slate-400 font-mono">📍 {app.district}</div>
                    </td>
                    <td className="py-3 px-4">
                      <span className="font-bold text-sky-400 font-mono text-[11px]">
                        {app.scheme_code}
                      </span>
                      <div className="text-slate-200 text-[11px]">{app.scheme_name_tamil}</div>
                    </td>
                    <td className="py-3 px-4">
                      <span
                        className={`px-2 py-0.5 rounded text-[10px] font-medium ${
                          app.status === "documents_pending"
                            ? "bg-amber-950 text-amber-300 border border-amber-800"
                            : "bg-purple-950 text-purple-300 border border-purple-800"
                        }`}
                      >
                        {app.status}
                      </span>
                    </td>
                    <td className="py-3 px-4 font-mono">
                      <span className="text-rose-400 font-bold">{app.days_stuck} days</span>
                      <div className="text-[10px] text-slate-500">Since {app.last_updated}</div>
                    </td>
                    <td className="py-3 px-4">
                      {app.pending_documents && app.pending_documents.length > 0 ? (
                        <ul className="list-disc list-inside text-[11px] text-rose-300 space-y-0.5">
                          {app.pending_documents.map((doc, idx) => (
                            <li key={idx}>{doc}</li>
                          ))}
                        </ul>
                      ) : (
                        <span className="text-slate-500 text-[10px]">None specified</span>
                      )}
                    </td>
                    <td className="py-3 px-4 text-[11px] text-slate-400">
                      {app.next_action_note || "—"}
                    </td>
                  </tr>
                ))
              )}
            </tbody>
          </table>
        </div>
      </div>
    </div>
  );
}
