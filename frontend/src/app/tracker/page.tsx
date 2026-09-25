"use client";

import { useState } from "react";
import Link from "next/link";
import Header from "@/components/Header";
import AudioButton from "@/components/AudioButton";
import { api, ApplicationStatusRecord } from "@/lib/api";

export default function TrackerPage() {
  const [personIdInput, setPersonIdInput] = useState("");
  const [applications, setApplications] = useState<ApplicationStatusRecord[]>([]);
  const [loading, setLoading] = useState(false);
  const [searched, setSearched] = useState(false);
  const [error, setError] = useState<string | null>(null);

  const handleSearch = async (e: React.FormEvent) => {
    e.preventDefault();
    if (!personIdInput.trim()) return;

    setLoading(true);
    setError(null);
    setSearched(true);

    try {
      const data = await api.getPersonApplications(personIdInput.trim());
      setApplications(data);
    } catch (err: any) {
      setError(err.message || "விண்ணப்பங்களை தேடுவதில் பிழை ஏற்பட்டது.");
      setApplications([]);
    } finally {
      setLoading(false);
    }
  };

  const statusBadge = (status: string) => {
    switch (status) {
      case "documents_pending":
        return {
          bg: "bg-amber-100 border-amber-300 text-amber-900",
          icon: "🟡",
          text: "ஆவணங்கள் நிலுவையில் உள்ளன (Documents Pending)",
        };
      case "submitted":
        return {
          bg: "bg-blue-100 border-blue-300 text-blue-900",
          icon: "🔵",
          text: "சமர்ப்பிக்கப்பட்டது (Submitted)",
        };
      case "under_review":
        return {
          bg: "bg-purple-100 border-purple-300 text-purple-900",
          icon: "🟣",
          text: "பரிசீலனையில் உள்ளது (Under Review)",
        };
      case "approved":
        return {
          bg: "bg-emerald-100 border-emerald-300 text-emerald-900",
          icon: "🟢",
          text: "அங்கீகரிக்கப்பட்டது (Approved)",
        };
      case "renewal_due":
        return {
          bg: "bg-orange-100 border-orange-300 text-orange-900",
          icon: "🟠",
          text: "புதுப்பித்தல் தேவை (Renewal Due)",
        };
      case "rejected":
        return {
          bg: "bg-red-100 border-red-300 text-red-900",
          icon: "🔴",
          text: "நிராகரிக்கப்பட்டது (Rejected)",
        };
      default:
        return {
          bg: "bg-slate-100 border-slate-300 text-slate-800",
          icon: "⚪",
          text: "தொடங்கப்படவில்லை (Not Started)",
        };
    }
  };

  return (
    <div className="min-h-screen flex flex-col bg-[#FBF9F5]">
      <Header />

      <main className="flex-1 max-w-4xl w-full mx-auto px-4 py-6 sm:py-8">
        <div className="mb-6">
          <h1 className="text-2xl sm:text-3xl font-extrabold text-emerald-950 mb-1">
            🔍 விண்ணப்ப நிலை அறிதல் (Application Tracking)
          </h1>
          <p className="text-xs sm:text-sm text-slate-600">
            தாங்கள் விண்ணப்பித்த அரசு நலத்திட்டங்களின் தற்போதைய நிலை மற்றும் நிலுவை ஆவணங்களை சரிபார்க்கவும்.
          </p>
        </div>

        {/* Search by Person ID */}
        <div className="gov-card p-6 bg-white border-2 border-slate-200 mb-8">
          <form onSubmit={handleSearch} className="space-y-3">
            <label className="block text-sm font-bold text-slate-900">
              பயனாளர் அடையாள எண் (Person ID / UUID):
            </label>
            <div className="flex flex-col sm:flex-row gap-3">
              <input
                type="text"
                required
                value={personIdInput}
                onChange={(e) => setPersonIdInput(e.target.value)}
                placeholder="எ.கா: 6ba7b810-9dad-11d1-80b4-00c04fd430c8"
                className="tap-target flex-1 p-3.5 border-2 border-slate-300 rounded-xl text-sm font-mono"
              />
              <button
                type="submit"
                disabled={loading}
                className="tap-target px-6 py-3 bg-[#0D5C3A] hover:bg-[#083B25] text-white font-bold rounded-xl shadow text-sm transition-all"
              >
                {loading ? "தேடுகிறது..." : "நிலையை சரிபார்க்கவும்"}
              </button>
            </div>
            <p className="text-xs text-slate-500">
              குறிப்பு: தகுதி அறிதல் முடிவுகள் பக்கத்தில் உள்ள உங்கள் Person ID எண்ணை உள்ளிடவும்.
            </p>
          </form>
        </div>

        {/* Results */}
        {error && (
          <div className="bg-red-50 border-2 border-red-300 p-4 rounded-xl text-red-800 text-sm mb-6">
            ⚠️ {error}
          </div>
        )}

        {searched && !loading && applications.length === 0 && !error && (
          <div className="gov-card p-8 text-center text-slate-600">
            இந்த அடையாள எண்ணுக்குரிய விண்ணப்பங்கள் எதுவும் இதுவரை பதிவு செய்யப்படவில்லை.
            <div className="mt-4">
              <Link
                href="/intake"
                className="tap-target px-5 py-2.5 bg-[#0D5C3A] text-white font-bold rounded-xl text-xs sm:text-sm inline-block shadow"
              >
                புதிய தகுதி மதிப்பீட்டைத் தொடங்கவும் →
              </Link>
            </div>
          </div>
        )}

        {applications.length > 0 && (
          <div className="space-y-4">
            <h2 className="text-lg font-bold text-slate-900 flex items-center space-x-2">
              <span>📋</span>
              <span>கண்டறியப்பட்ட விண்ணப்பங்கள் ({applications.length}):</span>
            </h2>

            {applications.map((app) => {
              const badge = statusBadge(app.status);
              return (
                <div
                  key={app.id}
                  className="gov-card p-5 sm:p-6 bg-white border-2 border-slate-200"
                >
                  <div className="flex flex-col sm:flex-row sm:items-start justify-between gap-3 mb-3">
                    <div>
                      <span className="text-xs font-mono text-slate-500 block">
                        {app.scheme_code || "SCHEME"}
                      </span>
                      <h3 className="text-base sm:text-lg font-bold text-slate-900">
                        {app.scheme_name_tamil || app.scheme_name_english || "அரசு நலத்திட்டம்"}
                      </h3>
                      <p className="text-xs text-slate-600">
                        பயனாளர்: <strong>{app.person_name || "பயனாளர்"}</strong>
                      </p>
                    </div>

                    <div className={`p-2.5 rounded-xl border text-xs font-bold ${badge.bg} flex items-center space-x-1.5 self-start`}>
                      <span>{badge.icon}</span>
                      <span>{badge.text}</span>
                    </div>
                  </div>

                  {/* Missing documents alert if documents pending */}
                  {app.status === "documents_pending" && app.pending_documents?.length > 0 && (
                    <div className="bg-amber-50 border border-amber-300 rounded-xl p-3.5 mb-3">
                      <span className="text-xs font-bold text-amber-900 block mb-1">
                        ⚠️ இன்னும் சமர்ப்பிக்க வேண்டிய ஆவணங்கள்:
                      </span>
                      <ul className="text-xs text-slate-800 space-y-1">
                        {app.pending_documents.map((doc, dIdx) => (
                          <li key={dIdx}>• {doc}</li>
                        ))}
                      </ul>
                    </div>
                  )}

                  {/* Next action note */}
                  {app.next_action_note && (
                    <p className="text-xs text-slate-700 bg-slate-50 p-2.5 rounded-lg border border-slate-100 mb-3">
                      <strong>அடுத்த நடவடிக்கை:</strong> {app.next_action_note}
                    </p>
                  )}

                  <div className="flex items-center justify-between pt-2 border-t border-slate-100 text-xs text-slate-500">
                    <span>கடைசியாக புதுப்பிக்கப்பட்டது: {app.last_updated}</span>
                    <AudioButton
                      textToSpeak={`திட்டம் ${app.scheme_name_tamil || ""}. தற்போதைய நிலை ${badge.text}.`}
                      label="நிலையைக் கேட்க"
                    />
                  </div>
                </div>
              );
            })}
          </div>
        )}
      </main>
    </div>
  );
}
