"use client";

import { useEffect, useState } from "react";
import { api, AdminAuditLog } from "@/lib/api";

export default function AdminAuditTrailPage() {
  const [logs, setLogs] = useState<AdminAuditLog[]>([]);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState<string | null>(null);

  const loadAuditLogs = async () => {
    try {
      setLoading(true);
      setError(null);
      const data = await api.getAdminAuditLogs(100);
      setLogs(data);
    } catch (err: any) {
      setError(err.message || "Failed to load audit logs.");
    } finally {
      setLoading(false);
    }
  };

  useEffect(() => {
    loadAuditLogs();
  }, []);

  return (
    <div className="space-y-6">
      <div className="flex items-center justify-between">
        <div>
          <h1 className="text-xl font-bold text-white">📜 Administrative Audit Trail</h1>
          <p className="text-xs text-slate-400">
            Immutable log of all administrative actions, rule modifications, and scheme sign-offs with before/after state diffs.
          </p>
        </div>
        <button
          onClick={loadAuditLogs}
          className="bg-slate-800 hover:bg-slate-700 text-slate-300 text-xs px-3 py-1.5 rounded transition"
        >
          Refresh Audit Trail
        </button>
      </div>

      {error && (
        <div className="p-3 bg-rose-950/70 border border-rose-800 rounded text-rose-300 text-xs">
          {error}
        </div>
      )}

      {/* Audit Log Table */}
      <div className="bg-slate-950 border border-slate-800 rounded-xl overflow-hidden">
        <div className="overflow-x-auto">
          <table className="w-full text-left text-xs">
            <thead className="bg-slate-900 text-slate-400 border-b border-slate-800 uppercase tracking-wider font-semibold">
              <tr>
                <th className="py-3 px-4">Timestamp</th>
                <th className="py-3 px-4">Administrator</th>
                <th className="py-3 px-4">Action</th>
                <th className="py-3 px-4">Entity</th>
                <th className="py-3 px-4">State Diff (Before → After)</th>
              </tr>
            </thead>
            <tbody className="divide-y divide-slate-800/60 font-mono text-slate-300">
              {loading ? (
                <tr>
                  <td colSpan={5} className="py-8 text-center text-slate-500 font-sans">
                    Loading audit trail...
                  </td>
                </tr>
              ) : logs.length === 0 ? (
                <tr>
                  <td colSpan={5} className="py-8 text-center text-slate-500 font-sans">
                    No admin actions logged yet.
                  </td>
                </tr>
              ) : (
                logs.map((log) => (
                  <tr key={log.id} className="hover:bg-slate-900/40 transition">
                    <td className="py-3 px-4 text-slate-400 text-[11px] whitespace-nowrap">
                      {new Date(log.created_at).toLocaleString("en-IN")}
                    </td>
                    <td className="py-3 px-4 font-sans text-sky-300 font-medium">
                      {log.admin_email}
                    </td>
                    <td className="py-3 px-4">
                      <span className="bg-indigo-950 text-indigo-300 border border-indigo-800/50 px-2 py-0.5 rounded text-[10px] font-bold">
                        {log.action}
                      </span>
                    </td>
                    <td className="py-3 px-4 text-slate-300">
                      <span className="text-slate-500">{log.entity_type}:</span>{" "}
                      <span className="text-amber-300 text-[11px]">{log.entity_id}</span>
                    </td>
                    <td className="py-3 px-4 font-sans">
                      <div className="bg-slate-900 p-2 rounded border border-slate-800 text-[11px] space-y-1">
                        {log.before_value && (
                          <div>
                            <span className="text-rose-400 font-bold">Before:</span>{" "}
                            <span className="font-mono text-slate-400">
                              {JSON.stringify(log.before_value)}
                            </span>
                          </div>
                        )}
                        {log.after_value && (
                          <div>
                            <span className="text-emerald-400 font-bold">After:</span>{" "}
                            <span className="font-mono text-emerald-200">
                              {JSON.stringify(log.after_value)}
                            </span>
                          </div>
                        )}
                      </div>
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
