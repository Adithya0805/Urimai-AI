"use client";

import { useEffect, useState } from "react";
import { api, SchemeReviewItem } from "@/lib/api";

export default function AdminReviewQueuePage() {
  const [items, setItems] = useState<SchemeReviewItem[]>([]);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState<string | null>(null);
  const [selectedItem, setSelectedItem] = useState<SchemeReviewItem | null>(null);
  const [reviewerNotes, setReviewerNotes] = useState("Verified against official gazette / TN e-Sevai portal");
  const [submitting, setSubmitting] = useState(false);

  const loadQueue = async () => {
    try {
      setLoading(true);
      setError(null);
      const data = await api.getAdminReviewQueue();
      setItems(data);
    } catch (err: any) {
      setError(err.message || "Failed to load review queue.");
    } finally {
      setLoading(false);
    }
  };

  useEffect(() => {
    loadQueue();
  }, []);

  const handleResolve = async (e: React.FormEvent) => {
    e.preventDefault();
    if (!selectedItem) return;

    try {
      setSubmitting(true);
      await api.resolveAdminReview(selectedItem.id, reviewerNotes, true);
      setSelectedItem(null);
      loadQueue();
    } catch (err: any) {
      setError(err.message || "Failed to resolve review item.");
    } finally {
      setSubmitting(false);
    }
  };

  return (
    <div className="space-y-6">
      <div className="flex items-center justify-between">
        <div>
          <h1 className="text-xl font-bold text-white">🕒 Scheme Freshness Review Queue</h1>
          <p className="text-xs text-slate-400">
            Schemes not verified within 180 days require official administrative verification.
          </p>
        </div>
        <button
          onClick={loadQueue}
          className="bg-slate-800 hover:bg-slate-700 text-slate-300 text-xs px-3 py-1.5 rounded transition"
        >
          Refresh Queue
        </button>
      </div>

      {error && (
        <div className="p-3 bg-rose-950/70 border border-rose-800 rounded text-rose-300 text-xs">
          {error}
        </div>
      )}

      {/* Review Queue Table */}
      <div className="bg-slate-950 border border-slate-800 rounded-xl overflow-hidden">
        <div className="overflow-x-auto">
          <table className="w-full text-left text-xs">
            <thead className="bg-slate-900 text-slate-400 border-b border-slate-800 uppercase tracking-wider font-semibold">
              <tr>
                <th className="py-3 px-4">Scheme</th>
                <th className="py-3 px-4">Department</th>
                <th className="py-3 px-4">Flagged Reason</th>
                <th className="py-3 px-4">Last Verified</th>
                <th className="py-3 px-4">Official Source</th>
                <th className="py-3 px-4 text-right">Action</th>
              </tr>
            </thead>
            <tbody className="divide-y divide-slate-800/60 text-slate-300">
              {loading ? (
                <tr>
                  <td colSpan={6} className="py-8 text-center text-slate-500">
                    Loading review queue...
                  </td>
                </tr>
              ) : items.length === 0 ? (
                <tr>
                  <td colSpan={6} className="py-8 text-center text-emerald-400 font-semibold">
                    ✓ All schemes are up-to-date. No pending reviews in the queue!
                  </td>
                </tr>
              ) : (
                items.map((item) => (
                  <tr key={item.id} className="hover:bg-slate-900/40 transition">
                    <td className="py-3 px-4">
                      <div className="font-bold text-amber-300 font-mono text-[11px]">
                        {item.scheme_code}
                      </div>
                      <div className="font-semibold text-slate-100">{item.scheme_name_tamil}</div>
                      <div className="text-[10px] text-slate-400">{item.scheme_name_english}</div>
                    </td>
                    <td className="py-3 px-4">{item.department}</td>
                    <td className="py-3 px-4">
                      <span className="bg-amber-950/70 text-amber-300 border border-amber-800/50 px-2 py-0.5 rounded text-[10px]">
                        {item.flagged_reason}
                      </span>
                    </td>
                    <td className="py-3 px-4 font-mono text-slate-400">
                      {item.last_verified_date || "Never Verified"}
                    </td>
                    <td className="py-3 px-4">
                      <a
                        href={item.source_url}
                        target="_blank"
                        rel="noreferrer"
                        className="text-emerald-400 hover:underline inline-flex items-center gap-1"
                      >
                        Official GO ↗
                      </a>
                    </td>
                    <td className="py-3 px-4 text-right">
                      <button
                        onClick={() => setSelectedItem(item)}
                        className="bg-emerald-600 hover:bg-emerald-500 text-white font-semibold px-3 py-1 rounded text-xs transition"
                      >
                        Mark Reviewed
                      </button>
                    </td>
                  </tr>
                ))
              )}
            </tbody>
          </table>
        </div>
      </div>

      {/* Review Sign-off Modal */}
      {selectedItem && (
        <div className="fixed inset-0 bg-black/70 backdrop-blur-sm flex items-center justify-center p-4 z-50">
          <div className="bg-slate-900 border border-slate-700 rounded-xl max-w-lg w-full p-6 space-y-4 shadow-2xl">
            <div className="flex items-center justify-between border-b border-slate-800 pb-3">
              <h2 className="text-base font-bold text-white">
                Sign-off Scheme Re-verification
              </h2>
              <button
                onClick={() => setSelectedItem(null)}
                className="text-slate-400 hover:text-white"
              >
                ✕
              </button>
            </div>

            <div className="text-xs text-slate-300 space-y-2 bg-slate-950 p-3 rounded border border-slate-800">
              <div>
                <span className="text-slate-500">Scheme:</span>{" "}
                <strong className="text-amber-300">{selectedItem.scheme_code}</strong> —{" "}
                {selectedItem.scheme_name_tamil}
              </div>
              <div>
                <span className="text-slate-500">Official Portal:</span>{" "}
                <a
                  href={selectedItem.source_url}
                  target="_blank"
                  rel="noreferrer"
                  className="text-emerald-400 underline"
                >
                  {selectedItem.source_url}
                </a>
              </div>
            </div>

            <form onSubmit={handleResolve} className="space-y-4">
              <div>
                <label className="block text-xs font-semibold text-slate-300 mb-1">
                  Administrator Review Notes / Gazette Reference
                </label>
                <textarea
                  value={reviewerNotes}
                  onChange={(e) => setReviewerNotes(e.target.value)}
                  required
                  rows={3}
                  className="w-full bg-slate-950 border border-slate-700 rounded p-2.5 text-xs text-white focus:outline-none focus:border-emerald-500 font-mono"
                  placeholder="E.g. Verified against G.O. Ms. No. 128 (Social Welfare Dept)..."
                />
              </div>

              <div className="flex justify-end gap-2 pt-2">
                <button
                  type="button"
                  onClick={() => setSelectedItem(null)}
                  className="px-3 py-1.5 bg-slate-800 hover:bg-slate-700 text-slate-300 text-xs rounded"
                >
                  Cancel
                </button>
                <button
                  type="submit"
                  disabled={submitting}
                  className="px-4 py-1.5 bg-emerald-600 hover:bg-emerald-500 text-white font-semibold text-xs rounded transition"
                >
                  {submitting ? "Signing Off..." : "Confirm & Update Verified Date"}
                </button>
              </div>
            </form>
          </div>
        </div>
      )}
    </div>
  );
}
