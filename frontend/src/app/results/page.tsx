"use client";

import { useEffect, useState, Suspense } from "react";
import { useSearchParams, useRouter } from "next/navigation";
import Link from "next/link";
import Header from "@/components/Header";
import AudioButton from "@/components/AudioButton";
import UrimaiSlip from "@/components/UrimaiSlip";
import { api, PersonEligibilityResponse, PersonGuidanceResponse } from "@/lib/api";

function ResultsContent() {
  const searchParams = useSearchParams();
  const router = useRouter();
  const personId = searchParams.get("person_id");
  const familyId = searchParams.get("family_id");

  const [loading, setLoading] = useState(true);
  const [error, setError] = useState<string | null>(null);
  const [eligibilityData, setEligibilityData] = useState<PersonEligibilityResponse | null>(null);
  const [guidanceData, setGuidanceData] = useState<PersonGuidanceResponse | null>(null);
  const [showSlip, setShowSlip] = useState(false);

  useEffect(() => {
    if (!personId) {
      setError("பயனாளர் அடையாளம் (Person ID) காணப்படவில்லை.");
      setLoading(false);
      return;
    }

    async function loadData() {
      try {
        setLoading(true);
        const [elig, guide] = await Promise.all([
          api.getPersonEligibility(personId!),
          api.getPersonGuidance(personId!),
        ]);
        setEligibilityData(elig);
        setGuidanceData(guide);
      } catch (err: any) {
        setError(err.message || "தகுதி முடிவுகளைப் பெறுவதில் பிழை ஏற்பட்டது.");
      } finally {
        setLoading(false);
      }
    }

    loadData();
  }, [personId]);

  if (loading) {
    return (
      <div className="flex-1 flex flex-col items-center justify-center p-8 text-center">
        <div className="w-16 h-16 border-4 border-emerald-600 border-t-transparent rounded-full animate-spin mb-4" />
        <h2 className="text-xl font-bold text-slate-800">
          அரசு விதிமுறைகளின்படி தகுதியை மதிப்பீடு செய்கிறது...
        </h2>
        <p className="text-sm text-slate-500 mt-2">
          (Checking eligibility rules across all departments)
        </p>
      </div>
    );
  }

  if (error || !eligibilityData) {
    return (
      <div className="flex-1 max-w-xl mx-auto p-6 text-center">
        <div className="bg-red-50 border-2 border-red-300 rounded-2xl p-6 mb-4">
          <span className="text-4xl block mb-2">⚠️</span>
          <h2 className="text-lg font-bold text-red-900 mb-2">முடிவுகளைப் பெற முடியவில்லை</h2>
          <p className="text-sm text-red-700">{error}</p>
        </div>
        <Link
          href="/"
          className="tap-target px-6 py-3 bg-[#0D5C3A] text-white font-bold rounded-xl shadow"
        >
          முகப்புப் பக்கத்திற்குச் செல்ல
        </Link>
      </div>
    );
  }

  const eligibleCount = eligibilityData.eligible_schemes.length;
  const partiallyCount = eligibilityData.partially_eligible_schemes.length;
  const personName = eligibilityData.person_name;

  const resultsAudioText = `${personName} அவர்களுக்கு ${eligibleCount} தமிழ்நாடு அரசு திட்டங்களில் முழு தகுதி உள்ளது. ${
    eligibleCount > 0 ? "திட்டங்களின் முழு விவரங்களை கீழே காண்க." : ""
  }`;

  return (
    <div className="flex-1 max-w-4xl w-full mx-auto px-4 py-6 sm:py-8">
      {/* Top Banner */}
      <div className="gov-card p-6 sm:p-7 bg-gradient-to-r from-emerald-900 via-emerald-800 to-[#0D5C3A] text-white mb-6 shadow-md rounded-2xl">
        <div className="flex flex-wrap items-center justify-between gap-3">
          <div>
            <span className="text-xs uppercase tracking-wider bg-emerald-700/70 text-emerald-200 px-3 py-1 rounded-full font-bold inline-block mb-2">
              தகுதி அறிதல் அறிக்கை (Eligibility Report)
            </span>
            <h1 className="text-2xl sm:text-3xl font-extrabold">
              {personName} — தகுதி முடிவுகள்
            </h1>
            <p className="text-emerald-100 text-sm mt-1">
              தாங்கள் பெறக்கூடிய தமிழ்நாடு அரசு நலத்திட்டங்கள் கீழே பட்டியலிடப்பட்டுள்ளன.
            </p>
          </div>

          <div className="flex flex-wrap gap-2">
            <AudioButton
              textToSpeak={resultsAudioText}
              label="முடிவுகளைக் கேட்க"
              className="bg-amber-400 text-slate-900 border-amber-300 font-bold"
            />
            <button
              onClick={() => setShowSlip(!showSlip)}
              className="tap-target px-4 py-2 bg-white text-emerald-950 hover:bg-emerald-50 font-bold rounded-xl shadow text-xs sm:text-sm flex items-center space-x-1.5"
            >
              <span>🎫</span>
              <span>{showSlip ? "முடிவுகளைக் காட்டு" : "உரிமைச் சீட்டு (Slip)"}</span>
            </button>
          </div>
        </div>
      </div>

      {/* Show Citizen Entitlement Slip if toggled */}
      {showSlip && (
        <div className="mb-8 animate-fadeIn">
          <UrimaiSlip
            personName={personName}
            schemes={guidanceData?.eligible_schemes_guidance || eligibilityData.eligible_schemes}
            onClose={() => setShowSlip(false)}
          />
        </div>
      )}

      {/* Summary Scoreboard */}
      <div className="grid grid-cols-2 gap-3 sm:gap-4 mb-8">
        <div className="gov-card p-4 sm:p-5 border-l-4 border-l-emerald-600 bg-emerald-50/50">
          <span className="text-xs font-bold text-emerald-800 uppercase block">
            முழு தகுதி பெற்றவை
          </span>
          <span className="text-3xl sm:text-4xl font-extrabold text-emerald-900 mt-1 block">
            {eligibleCount} <span className="text-sm font-normal text-emerald-700">திட்டங்கள்</span>
          </span>
        </div>

        <div className="gov-card p-4 sm:p-5 border-l-4 border-l-amber-500 bg-amber-50/50">
          <span className="text-xs font-bold text-amber-800 uppercase block">
            கூடுதல் நிபந்தனை தேவைப்படுபவை
          </span>
          <span className="text-3xl sm:text-4xl font-extrabold text-amber-900 mt-1 block">
            {partiallyCount} <span className="text-sm font-normal text-amber-700">திட்டங்கள்</span>
          </span>
        </div>
      </div>

      {/* SECTION 1: Fully Eligible Schemes */}
      <div className="mb-10">
        <div className="flex items-center space-x-2 mb-4">
          <span className="text-2xl">🟢</span>
          <h2 className="text-xl font-bold text-slate-900">
            முழு தகுதி உள்ள திட்டங்கள் ({eligibleCount})
          </h2>
        </div>

        {eligibleCount === 0 ? (
          <div className="gov-card p-6 text-center text-slate-600 bg-slate-50">
            தற்போது தங்களின் சுயவிவரத்திற்கு முழு தகுதி உள்ள திட்டங்கள் எதுவும் கண்டறியப்படவில்லை.
          </div>
        ) : (
          <div className="space-y-4">
            {eligibilityData.eligible_schemes.map((scheme) => (
              <div
                key={scheme.scheme_code}
                className="gov-card p-5 sm:p-6 border-2 border-emerald-200 hover:border-emerald-600 transition-all bg-white"
              >
                <div className="flex flex-col sm:flex-row sm:items-start justify-between gap-3 mb-3">
                  <div>
                    <div className="flex items-center space-x-2 mb-1">
                      <span className="text-xs font-bold bg-emerald-100 text-emerald-800 px-2.5 py-0.5 rounded-full">
                        {scheme.category}
                      </span>
                      <span className="text-xs font-mono text-slate-500">
                        {scheme.scheme_code}
                      </span>
                    </div>
                    <h3 className="text-lg sm:text-xl font-bold text-emerald-950">
                      {scheme.name_tamil}
                    </h3>
                    <p className="text-xs text-slate-600">
                      {scheme.name_english} • {scheme.department}
                    </p>
                  </div>

                  <div className="bg-emerald-50 border border-emerald-200 rounded-xl p-3 text-right flex-shrink-0">
                    <span className="text-xs font-bold text-emerald-800 block">உதவித்தொகை</span>
                    <span className="text-lg font-extrabold text-emerald-900 block">
                      {scheme.benefit_amount}
                    </span>
                  </div>
                </div>

                <p className="text-slate-700 text-xs sm:text-sm mb-4 leading-relaxed bg-slate-50 p-3 rounded-lg border border-slate-100">
                  {scheme.description_tamil}
                </p>

                <div className="flex flex-wrap items-center justify-between gap-3 pt-3 border-t border-slate-100">
                  <div className="flex items-center space-x-2">
                    <AudioButton
                      textToSpeak={`${scheme.name_tamil}. உதவித்தொகை ${scheme.benefit_amount}. ${scheme.description_tamil}`}
                      label="விளக்கம் கேட்க"
                    />
                  </div>

                  <Link
                    href={`/guidance/${personId}?scheme_code=${scheme.scheme_code}`}
                    className="tap-target px-4 py-2.5 bg-[#0D5C3A] hover:bg-[#083B25] text-white font-bold rounded-xl text-xs sm:text-sm shadow transition-all flex items-center space-x-1.5"
                  >
                    <span>📄</span>
                    <span>விண்ணப்பிக்கும் முறை & ஆவணங்கள்</span>
                    <span>→</span>
                  </Link>
                </div>
              </div>
            ))}
          </div>
        )}
      </div>

      {/* SECTION 2: Partially Eligible Schemes (Gap Analysis) */}
      {partiallyCount > 0 && (
        <div className="mb-10">
          <div className="flex items-center space-x-2 mb-4">
            <span className="text-2xl">🟡</span>
            <h2 className="text-xl font-bold text-slate-900">
              கூடுதல் நிபந்தனை தேவைப்படும் திட்டங்கள் ({partiallyCount})
            </h2>
          </div>

          <div className="space-y-4">
            {eligibilityData.partially_eligible_schemes.map((item) => (
              <div
                key={item.scheme.scheme_code}
                className="gov-card p-5 border-2 border-amber-200 bg-amber-50/20"
              >
                <div className="flex flex-col sm:flex-row sm:items-start justify-between gap-2 mb-2">
                  <div>
                    <span className="text-xs font-mono text-slate-500 block">
                      {item.scheme.scheme_code}
                    </span>
                    <h3 className="text-base sm:text-lg font-bold text-slate-900">
                      {item.scheme.name_tamil}
                    </h3>
                  </div>
                  <span className="text-xs font-bold text-emerald-800 bg-emerald-100 px-2 py-1 rounded self-start">
                    {item.scheme.benefit_amount}
                  </span>
                </div>

                <div className="mt-3 bg-white border border-amber-300 rounded-xl p-3.5">
                  <span className="text-xs font-bold text-amber-900 flex items-center space-x-1 mb-1.5">
                    <span>⚠️</span>
                    <span>தற்போது விடுபட்டுள்ள நிபந்தனை:</span>
                  </span>
                  <ul className="space-y-1 text-xs sm:text-sm text-slate-800">
                    {item.failed_rules.map((rule, rIdx) => (
                      <li key={rIdx} className="bg-amber-50 p-2 rounded border border-amber-100">
                        • <strong>{rule.field_name}:</strong> {rule.reason}
                      </li>
                    ))}
                  </ul>
                </div>
              </div>
            ))}
          </div>
        </div>
      )}

      {/* Bottom Actions */}
      <div className="flex flex-wrap items-center justify-between gap-3 pt-6 border-t border-slate-300">
        <Link
          href="/"
          className="tap-target px-5 py-3 bg-slate-200 hover:bg-slate-300 text-slate-800 font-bold rounded-xl"
        >
          ← முகப்பு
        </Link>

        {familyId && (
          <Link
            href={`/family/${familyId}`}
            className="tap-target px-5 py-3 bg-emerald-800 hover:bg-emerald-900 text-white font-bold rounded-xl"
          >
            👨‍👩‍👧‍👦 குடும்ப பலகையை பார்க்க (Family Board) →
          </Link>
        )}
      </div>
    </div>
  );
}

export default function ResultsPage() {
  return (
    <div className="min-h-screen flex flex-col bg-[#FBF9F5]">
      <Header />
      <Suspense
        fallback={
          <div className="flex-1 flex items-center justify-center p-8 text-center font-bold">
            ஏற்றுகிறது...
          </div>
        }
      >
        <ResultsContent />
      </Suspense>
    </div>
  );
}
