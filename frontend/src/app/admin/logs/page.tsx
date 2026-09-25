"use client";

import { useEffect, useState } from "react";
import { api, ErrorLogItem } from "@/lib/api";

export default function AdminErrorLogsPage() {
  const [logs, setLogs] = useState<ErrorLogItem[]>([]);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState<string | null>(null);

  const loadLogs = async () => {
    try {
      setLoading(true);
      setError(null);
      const data = await api.getAdminErrorLogs(100);
      setLogs(data);
    } catch (err: any) {
      setError(err.message || "Failed to load error logs.");
    } finally {
      setLoading(false);
    }
  };

  useEffect(() => {
    loadLogs();
  }, []);

  return (
    <div className="space-y-6">
      <div className="flex items-center justify-between">
        <div>
          <h1 className="text-xl font-bold text-white">🚨 Error & Exception Logs</h1>
          <p className="text-xs text-slate-400">
            Real-time conversational extraction failures, schema validation rejections, and system faults.
          </p>
        </div>
        <button
          onClick={loadLogs}
          className="bg-slate-800 hover:bg-slate-700 text-slate-300 text-xs px-3 py-1.5 rounded transition"
        >
          Refresh Logs
        </button>
      </div>

      {error && (
        <div className="p-3 bg-rose-950/70 border border-rose-800 rounded text-rose-300 text-xs">
          {error}
        </div>
      )}

      {/* Logs Table */}
      <div className="bg-slate-950 border border-slate-800 rounded-xl overflow-hidden">
        <div className="overflow-x-auto">
          <table className="w-full text-left text-xs">
            <thead className="bg-slate-900 text-slate-400 border-b border-slate-800 uppercase tracking-wider font-semibold">
              <tr>
                <th className="py-3 px-4">Timestamp</th>
                <th className="py-3 px-4">Type</th>
                <th className="py-3 px-4">Target Field</th>
                <th className="py-3 px-4">Raw Citizen Input</th>
                <th className="py-3 px-4">Failure Reason</th>
              </tr>
            </thead>
            <tbody className="divide-y divide-slate-800/60 font-mono text-slate-300">
              {loading ? (
                <tr>
                  <td colSpan={5} className="py-8 text-center text-slate-500 font-sans">
                    Loading logs...
                  </td>
                </tr>
              ) : logs.length === 0 ? (
                <tr>
                  <td colSpan={5} className="py-8 text-center text-emerald-400 font-semibold font-sans">
                    ✓ Clean operation. No recent failure logs recorded.
                  </td>
                </tr>
              ) : (
                logs.map((log) => (
                  <tr key={log.id} className="hover:bg-slate-900/40 transition">
                    <td className="py-3 px-4 text-slate-400 text-[11px] whitespace-nowrap">
                      {new Date(log.created_at).toLocaleString("en-IN")}
                    </td>
                    <td className="py-3 px-4">
                      <span className="bg-rose-950 text-rose-300 border border-rose-800/60 px-2 py-0.5 rounded text-[10px] uppercase font-sans font-semibold">
                        {log.log_type}
                      </span>
                    </td>
                    <td className="py-3 px-4 text-sky-400 font-bold">{log.target_field || "N/A"}</td>
                    <td className="py-3 px-4 text-amber-200 font-sans">{log.raw_input || "—"}</td>
                    <td className="py-3 px-4 text-rose-400 text-[11px] font-sans">
                      {log.error_message || "Validation failed on value parsing"}
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
