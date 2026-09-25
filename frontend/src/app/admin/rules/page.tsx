"use client";

import { useEffect, useState } from "react";
import { api, EligibleScheme } from "@/lib/api";

export default function AdminRulesPage() {
  const [schemes, setSchemes] = useState<EligibleScheme[]>([]);
  const [selectedScheme, setSelectedScheme] = useState<EligibleScheme | null>(null);
  const [schemeDetails, setSchemeDetails] = useState<any | null>(null);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState<string | null>(null);
  const [successMsg, setSuccessMsg] = useState<string | null>(null);

  // Edit Modal State
  const [editingRule, setEditingRule] = useState<any | null>(null);
  const [editValue, setEditValue] = useState("");
  const [adminNotes, setAdminNotes] = useState("");
  const [saving, setSaving] = useState(false);

  useEffect(() => {
    async function loadAllSchemes() {
      try {
        setLoading(true);
        const data = await api.getSchemes();
        setSchemes(data);
        if (data.length > 0) {
          selectScheme(data[0]);
        }
      } catch (err: any) {
        setError(err.message || "Failed to load schemes.");
      } finally {
        setLoading(false);
      }
    }
    loadAllSchemes();
  }, []);

  const selectScheme = async (scheme: EligibleScheme) => {
    try {
      setSelectedScheme(scheme);
      setError(null);
      setSuccessMsg(null);
      const details = await api.getScheme(scheme.id);
      setSchemeDetails(details);
    } catch (err: any) {
      setError(err.message || "Failed to load scheme details.");
    }
  };

  const handleOpenEdit = (rule: any) => {
    setEditingRule(rule);
    setEditValue(rule.value);
    setAdminNotes(`Adjusted threshold based on updated Government Order`);
  };

  const handleSaveRule = async (e: React.FormEvent) => {
    e.preventDefault();
    if (!selectedScheme || !editingRule) return;

    try {
      setSaving(true);
      setError(null);
      await api.updateAdminRule(selectedScheme.id, editingRule.id, {
        value: editValue,
        admin_notes: adminNotes,
      });

      setSuccessMsg(`Rule condition for '${editingRule.field_name}' successfully updated and logged.`);
      setEditingRule(null);
      selectScheme(selectedScheme);
    } catch (err: any) {
      setError(err.message || "Failed to update eligibility rule.");
    } finally {
      setSaving(false);
    }
  };

  return (
    <div className="space-y-6">
      <div>
        <h1 className="text-xl font-bold text-white">⚖️ Scheme & Eligibility Rule Editor</h1>
        <p className="text-xs text-slate-400">
          Inspect and recalibrate mathematical rule conditions with strict schema validation and audit logging.
        </p>
      </div>

      {successMsg && (
        <div className="p-3 bg-emerald-950/70 border border-emerald-800 rounded text-emerald-300 text-xs flex justify-between items-center">
          <span>{successMsg}</span>
          <button onClick={() => setSuccessMsg(null)}>✕</button>
        </div>
      )}

      {error && (
        <div className="p-3 bg-rose-950/70 border border-rose-800 rounded text-rose-300 text-xs">
          {error}
        </div>
      )}

      <div className="grid grid-cols-1 md:grid-cols-3 gap-6">
        {/* Scheme Selector List */}
        <div className="bg-slate-950 border border-slate-800 rounded-xl p-4 space-y-3 h-[650px] flex flex-col">
          <h2 className="text-xs font-bold text-slate-400 uppercase tracking-wider">
            Select Scheme ({schemes.length})
          </h2>
          <div className="flex-1 overflow-y-auto space-y-1.5 pr-1 text-xs">
            {schemes.map((s) => {
              const isSelected = selectedScheme?.id === s.id;
              return (
                <button
                  key={s.id}
                  onClick={() => selectScheme(s)}
                  className={`w-full text-left p-2.5 rounded transition border ${
                    isSelected
                      ? "bg-slate-900 border-emerald-500 text-white shadow"
                      : "border-transparent text-slate-400 hover:text-slate-200 hover:bg-slate-900/50"
                  }`}
                >
                  <div className="font-mono text-[10px] text-amber-400 font-bold">{s.scheme_code}</div>
                  <div className="font-semibold truncate">{s.name_tamil}</div>
                  <div className="text-[10px] text-slate-500 truncate">{s.department}</div>
                </button>
              );
            })}
          </div>
        </div>

        {/* Scheme Details & Rules Inspector */}
        <div className="md:col-span-2 bg-slate-950 border border-slate-800 rounded-xl p-5 space-y-5">
          {selectedScheme && schemeDetails ? (
            <>
              <div className="border-b border-slate-800 pb-4">
                <div className="flex items-center justify-between">
                  <span className="font-mono text-xs text-amber-400 font-bold">
                    {schemeDetails.scheme_code}
                  </span>
                  <span className="text-xs text-emerald-400 bg-emerald-950 px-2 py-0.5 rounded border border-emerald-800">
                    {schemeDetails.category}
                  </span>
                </div>
                <h2 className="text-base font-bold text-white mt-1">
                  {schemeDetails.name_tamil}
                </h2>
                <div className="text-xs text-slate-400">{schemeDetails.name_english}</div>
                <div className="text-xs text-slate-300 mt-2 bg-slate-900/80 p-2.5 rounded border border-slate-800">
                  <span className="text-slate-500">Benefit:</span> {schemeDetails.benefit_amount}
                </div>
              </div>

              {/* Rules Table */}
              <div>
                <h3 className="text-xs font-bold text-slate-300 uppercase tracking-wider mb-3">
                  Eligibility Rules & Criteria ({schemeDetails.rules?.length || 0})
                </h3>

                <div className="overflow-x-auto border border-slate-800 rounded-lg">
                  <table className="w-full text-left text-xs">
                    <thead className="bg-slate-900 text-slate-400 font-semibold uppercase text-[10px]">
                      <tr>
                        <th className="py-2.5 px-3">Field Name</th>
                        <th className="py-2.5 px-3">Applies To</th>
                        <th className="py-2.5 px-3">Operator</th>
                        <th className="py-2.5 px-3">Required Value</th>
                        <th className="py-2.5 px-3 text-right">Edit</th>
                      </tr>
                    </thead>
                    <tbody className="divide-y divide-slate-800 font-mono text-slate-300">
                      {schemeDetails.rules?.map((rule: any) => (
                        <tr key={rule.id} className="hover:bg-slate-900/40">
                          <td className="py-2.5 px-3 text-sky-300 font-bold">{rule.field_name}</td>
                          <td className="py-2.5 px-3 font-sans text-[11px] text-slate-400">
                            {rule.applies_to}
                          </td>
                          <td className="py-2.5 px-3 text-amber-300">{rule.operator}</td>
                          <td className="py-2.5 px-3 font-bold text-emerald-300">{rule.value}</td>
                          <td className="py-2.5 px-3 text-right font-sans">
                            <button
                              onClick={() => handleOpenEdit(rule)}
                              className="bg-slate-800 hover:bg-slate-700 text-slate-200 px-2.5 py-1 rounded text-xs transition"
                            >
                              Edit
                            </button>
                          </td>
                        </tr>
                      ))}
                    </tbody>
                  </table>
                </div>
              </div>
            </>
          ) : (
            <div className="py-12 text-center text-slate-500 text-xs">
              Select a scheme from the left panel to inspect its eligibility rules.
            </div>
          )}
        </div>
      </div>

      {/* Edit Rule Modal */}
      {editingRule && (
        <div className="fixed inset-0 bg-black/70 backdrop-blur-sm flex items-center justify-center p-4 z-50">
          <div className="bg-slate-900 border border-slate-700 rounded-xl max-w-md w-full p-6 space-y-4 shadow-2xl">
            <div className="flex items-center justify-between border-b border-slate-800 pb-3">
              <h2 className="text-sm font-bold text-white">
                Edit Eligibility Rule: {editingRule.field_name}
              </h2>
              <button onClick={() => setEditingRule(null)} className="text-slate-400 hover:text-white">
                ✕
              </button>
            </div>

            <form onSubmit={handleSaveRule} className="space-y-4 text-xs">
              <div>
                <label className="block text-slate-400 mb-1">Target Field / Operator</label>
                <div className="font-mono bg-slate-950 p-2 rounded border border-slate-800 text-slate-300">
                  {editingRule.field_name} ({editingRule.operator})
                </div>
              </div>

              <div>
                <label className="block font-semibold text-slate-300 mb-1">
                  Required Value (Threshold / Criteria)
                </label>
                <input
                  type="text"
                  value={editValue}
                  onChange={(e) => setEditValue(e.target.value)}
                  required
                  className="w-full bg-slate-950 border border-slate-700 rounded p-2 text-white font-mono focus:outline-none focus:border-emerald-500"
                />
              </div>

              <div>
                <label className="block font-semibold text-slate-300 mb-1">
                  Mandatory Administrative Rationale (Audit Trail)
                </label>
                <textarea
                  value={adminNotes}
                  onChange={(e) => setAdminNotes(e.target.value)}
                  required
                  rows={3}
                  className="w-full bg-slate-950 border border-slate-700 rounded p-2 text-white focus:outline-none focus:border-emerald-500 font-sans"
                  placeholder="Explain why this rule is being edited..."
                />
              </div>

              <div className="flex justify-end gap-2 pt-2">
                <button
                  type="button"
                  onClick={() => setEditingRule(null)}
                  className="px-3 py-1.5 bg-slate-800 hover:bg-slate-700 text-slate-300 rounded"
                >
                  Cancel
                </button>
                <button
                  type="submit"
                  disabled={saving}
                  className="px-4 py-1.5 bg-emerald-600 hover:bg-emerald-500 text-white font-semibold rounded transition"
                >
                  {saving ? "Updating..." : "Save Rule & Log Audit"}
                </button>
              </div>
            </form>
          </div>
        </div>
      )}
    </div>
  );
}
