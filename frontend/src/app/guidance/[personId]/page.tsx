"use client";

import { useEffect, useState, use, Suspense } from "react";
import { useSearchParams, useRouter } from "next/navigation";
import Link from "next/link";
import Header from "@/components/Header";
import AudioButton from "@/components/AudioButton";
import { api, PersonGuidanceResponse, EligibleSchemeGuidance } from "@/lib/api";

function GuidanceContent({
  personId,
}: {
  personId: string;
}) {
  const searchParams = useSearchParams();
  const router = useRouter();
  const selectedSchemeCode = searchParams.get("scheme_code");

  const [loading, setLoading] = useState(true);
  const [error, setError] = useState<string | null>(null);
  const [guidanceData, setGuidanceData] = useState<PersonGuidanceResponse | null>(null);
  const [selectedScheme, setSelectedScheme] = useState<EligibleSchemeGuidance | null>(null);
  const [checkedDocs, setCheckedDocs] = useState<Record<string, boolean>>({});
  const [trackingSuccess, setTrackingSuccess] = useState<string | null>(null);

  useEffect(() => {
    async function loadGuidance() {
      try {
        setLoading(true);
        const data = await api.getPersonGuidance(personId);
        setGuidanceData(data);

        if (data.eligible_schemes_guidance.length > 0) {
          const match = selectedSchemeCode
            ? data.eligible_schemes_guidance.find((g) => g.scheme_code === selectedSchemeCode)
            : data.eligible_schemes_guidance[0];
          setSelectedScheme(match || data.eligible_schemes_guidance[0]);
        }
      } catch (err: any) {
        setError(err.message || "வழிகாட்டி விவரங்களைப் பெற முடியவில்லை.");
      } finally {
        setLoading(false);
      }
    }

    loadGuidance();
  }, [personId, selectedSchemeCode]);

  const toggleDoc = (doc: string) => {
    setCheckedDocs((prev) => ({ ...prev, [doc]: !prev[doc] }));
  };

  const handleStartTracking = async (scheme: EligibleSchemeGuidance) => {
    try {
      const missing = scheme.required_documents.filter((d) => !checkedDocs[d]);
      await api.createApplicationTracking({
        person_id: personId,
        scheme_id: scheme.scheme_id,
        status: missing.length > 0 ? "documents_pending" : "submitted",
        pending_documents: missing,
        next_action_note: missing.length > 0 ? "தயாராகாத ஆவணங்களை சேகரிக்கவும்" : "விண்ணப்பிக்கவும்",
      });
      setTrackingSuccess("விண்ணப்ப கண்காணிப்பு வெற்றிகரமாக தொடங்கப்பட்டது!");
      setTimeout(() => {
        router.push("/tracker");
      }, 1500);
    } catch (err: any) {
      alert("கண்காணிப்பை தொடங்குவதில் பிழை: " + err.message);
    }
  };

  if (loading) {
    return (
      <div className="min-h-screen flex flex-col bg-[#FBF9F5]">
        <Header />
        <div className="flex-1 flex flex-col items-center justify-center p-8 text-center">
          <div className="w-16 h-16 border-4 border-emerald-600 border-t-transparent rounded-full animate-spin mb-4" />
          <h2 className="text-lg font-bold text-slate-800">
            விண்ணப்ப வழிகாட்டி மற்றும் ஆவணப் பட்டியல் தயாராகிறது...
          </h2>
        </div>
      </div>
    );
  }

  if (error || !guidanceData) {
    return (
      <div className="min-h-screen flex flex-col bg-[#FBF9F5]">
        <Header />
        <div className="flex-1 max-w-lg mx-auto p-6 text-center">
          <div className="bg-red-50 border-2 border-red-300 rounded-2xl p-6 mb-4">
            <span className="text-3xl block mb-2">⚠️</span>
            <h2 className="text-lg font-bold text-red-900 mb-2">பிழை ஏற்பட்டது</h2>
            <p className="text-sm text-red-700">{error}</p>
          </div>
          <Link
            href="/"
            className="tap-target px-6 py-3 bg-[#0D5C3A] text-white font-bold rounded-xl shadow"
          >
            முகப்பு
          </Link>
        </div>
      </div>
    );
  }

  return (
    <div className="min-h-screen flex flex-col bg-[#FBF9F5]">
      <Header />

      <main className="flex-1 max-w-4xl w-full mx-auto px-4 py-6 sm:py-8">
        {/* Breadcrumb / Back Navigation */}
        <div className="mb-4">
          <Link
            href={`/results?person_id=${personId}`}
            className="text-xs sm:text-sm font-bold text-emerald-800 hover:text-emerald-950 flex items-center space-x-1"
          >
            <span>←</span>
            <span>தகுதி முடிவுகளுக்குத் திரும்புக (Back to Results)</span>
          </Link>
        </div>

        {/* Scheme Selector Tabs */}
        {guidanceData.eligible_schemes_guidance.length > 1 && (
          <div className="flex overflow-x-auto gap-2 pb-3 mb-6 no-scrollbar">
            {guidanceData.eligible_schemes_guidance.map((sch) => (
              <button
                key={sch.scheme_code}
                onClick={() => setSelectedScheme(sch)}
                className={`tap-target px-4 py-2.5 rounded-xl font-bold text-xs sm:text-sm whitespace-nowrap transition-all border-2 ${
                  selectedScheme?.scheme_code === sch.scheme_code
                    ? "bg-[#0D5C3A] text-white border-[#0D5C3A] shadow-sm"
                    : "bg-white text-slate-800 border-slate-200 hover:border-slate-300"
                }`}
              >
                {sch.name_tamil}
              </button>
            ))}
          </div>
        )}

        {selectedScheme ? (
          <div className="space-y-6">
            {/* Scheme Title Card */}
            <div className="gov-card p-6 bg-emerald-950 text-white rounded-2xl relative">
              <div className="flex flex-wrap items-start justify-between gap-3 mb-3">
                <div>
                  <span className="text-xs font-mono text-emerald-300 block mb-1">
                    {selectedScheme.scheme_code}
                  </span>
                  <h1 className="text-xl sm:text-2xl font-bold leading-tight">
                    {selectedScheme.name_tamil}
                  </h1>
                  <p className="text-xs text-emerald-200 mt-1">
                    {selectedScheme.name_english}
                  </p>
                </div>

                <div className="bg-emerald-900 border border-emerald-700 rounded-xl px-4 py-2 text-right">
                  <span className="text-xs text-emerald-300 block">மாத / ஒருமுறை உதவி</span>
                  <span className="text-xl font-extrabold text-amber-300">
                    {selectedScheme.benefit_amount}
                  </span>
                </div>
              </div>

              {/* Staleness Warning if Applicable */}
              {selectedScheme.is_stale && (
                <div className="bg-amber-500/20 border border-amber-400/50 rounded-xl p-3 text-xs text-amber-200 mt-3 flex items-center space-x-2">
                  <span>⚠️</span>
                  <span>{selectedScheme.disclaimer_tamil || "இந்த தகவல் 6 மாதங்களுக்கு முன்பு சரிபார்க்கப்பட்டது. உள்ளூர் அலுவலகத்தில் உறுதிப்படுத்தவும்."}</span>
                </div>
              )}

              <div className="mt-4 pt-3 border-t border-emerald-800 flex items-center justify-between">
                <AudioButton
                  textToSpeak={`${selectedScheme.name_tamil}. உதவித்தொகை ${selectedScheme.benefit_amount}. விண்ணப்பிக்கும் முறை: ${selectedScheme.steps_tamil.join(". ")}`}
                  label="முழு வழிகாட்டலையும் கேட்க"
                  className="bg-amber-400 text-slate-900 border-amber-300"
                />
              </div>
            </div>

            {/* Checklist of Required Physical Documents */}
            <div className="gov-card p-6 border-2 border-slate-200">
              <div className="flex items-center justify-between mb-4">
                <h2 className="text-base sm:text-lg font-bold text-slate-900 flex items-center space-x-2">
                  <span>📄</span>
                  <span>தேவையான அசல் ஆவணங்கள் (Document Checklist)</span>
                </h2>
                <span className="text-xs font-bold text-emerald-800 bg-emerald-50 px-2.5 py-1 rounded-full border border-emerald-200">
                  {Object.values(checkedDocs).filter(Boolean).length} / {selectedScheme.required_documents.length} தயார்
                </span>
              </div>

              <p className="text-xs text-slate-600 mb-3">
                நேரில் விண்ணப்பிக்க செல்லும் முன் உங்களிடம் உள்ள ஆவணங்களை சரிபார்த்து டிக் (Tick) செய்யவும்:
              </p>

              <div className="space-y-2.5">
                {selectedScheme.required_documents.map((doc, idx) => {
                  const isChecked = Boolean(checkedDocs[doc]);
                  return (
                    <button
                      key={idx}
                      type="button"
                      onClick={() => toggleDoc(doc)}
                      className={`tap-target w-full text-left p-3.5 rounded-xl border-2 transition-all flex items-center justify-between ${
                        isChecked
                          ? "bg-emerald-50 border-emerald-500 text-emerald-950 font-bold"
                          : "bg-slate-50 border-slate-200 text-slate-800"
                      }`}
                    >
                      <span className="text-sm flex items-center space-x-2.5">
                        <span className="text-lg">{isChecked ? "✅" : "⬜"}</span>
                        <span>{doc}</span>
                      </span>
                      <span className="text-xs text-slate-500">
                        {isChecked ? "தயாராக உள்ளது" : "கிளிக் செய்து டிக் செய்யவும்"}
                      </span>
                    </button>
                  );
                })}
              </div>
            </div>

            {/* Step-by-Step Numbered Application Roadmap */}
            <div className="gov-card p-6 border-2 border-slate-200">
              <h2 className="text-base sm:text-lg font-bold text-slate-900 mb-4 flex items-center space-x-2">
                <span>📍</span>
                <span>விண்ணப்பிக்கும் முறை (Step-by-Step Instructions)</span>
              </h2>

              <div className="space-y-4">
                {selectedScheme.steps_tamil.map((stepText, sIdx) => (
                  <div
                    key={sIdx}
                    className="flex items-start space-x-3.5 p-3.5 bg-slate-50 rounded-xl border border-slate-200"
                  >
                    <span className="w-7 h-7 rounded-full bg-emerald-800 text-white font-bold text-sm flex items-center justify-center flex-shrink-0 mt-0.5">
                      {sIdx + 1}
                    </span>
                    <p className="text-sm text-slate-800 leading-relaxed font-medium">
                      {stepText}
                    </p>
                  </div>
                ))}
              </div>
            </div>

            {/* Where to Go & Apply */}
            <div className="gov-card p-6 bg-gradient-to-br from-slate-50 to-emerald-50/40 border-2 border-emerald-300">
              <h2 className="text-base sm:text-lg font-bold text-emerald-950 mb-3 flex items-center space-x-2">
                <span>🏛️</span>
                <span>எங்கு விண்ணப்பிக்க வேண்டும்? (Application Office)</span>
              </h2>

              <div className="bg-white p-4 rounded-xl border border-emerald-200 mb-4">
                <span className="text-xs font-bold text-emerald-800 uppercase block">அலுவலகம்</span>
                <span className="text-base font-bold text-slate-900 block mt-0.5">
                  {selectedScheme.where_to_apply_tamil}
                </span>
                <span className="text-xs text-slate-600 block mt-1">
                  மதிப்பிடப்பட்ட காலம்: <strong>{selectedScheme.processing_time_estimate}</strong>
                </span>
              </div>

              {selectedScheme.online_application_url && (
                <div className="mb-4">
                  <a
                    href={selectedScheme.online_application_url}
                    target="_blank"
                    rel="noopener noreferrer"
                    className="tap-target w-full px-4 py-3 bg-[#1E40AF] hover:bg-[#1E3A8A] text-white font-bold rounded-xl text-center text-sm shadow transition-all flex items-center justify-center space-x-2"
                  >
                    <span>🌐</span>
                    <span>இணையதளம் மூலம் நேரடியாக விண்ணப்பிக்க (Official Portal)</span>
                    <span>↗</span>
                  </a>
                </div>
              )}

              {/* Start Tracking Button */}
              <div className="pt-2">
                <button
                  onClick={() => handleStartTracking(selectedScheme)}
                  className="tap-target w-full px-5 py-3.5 bg-[#0D5C3A] hover:bg-[#083B25] text-white font-bold rounded-xl text-sm shadow-md transition-all flex items-center justify-center space-x-2"
                >
                  <span>📌</span>
                  <span>இந்த திட்ட விண்ணப்பத்தை கண்காணிக்க (Track Application)</span>
                </button>
                {trackingSuccess && (
                  <p className="text-xs font-bold text-emerald-700 text-center mt-2">
                    ✓ {trackingSuccess}
                  </p>
                )}
              </div>
            </div>
          </div>
        ) : (
          <div className="gov-card p-6 text-center text-slate-600">
            திட்ட வழிகாட்டி தகவல் கிடைக்கவில்லை.
          </div>
        )}
      </main>
    </div>
  );
}

export default function GuidancePage({
  params,
}: {
  params: Promise<{ personId: string }>;
}) {
  const resolvedParams = use(params);
  return (
    <Suspense
      fallback={
        <div className="min-h-screen flex items-center justify-center font-bold text-slate-700">
          வழிகாட்டி ஏற்றப்படுகிறது...
        </div>
      }
    >
      <GuidanceContent personId={resolvedParams.personId} />
    </Suspense>
  );
}

