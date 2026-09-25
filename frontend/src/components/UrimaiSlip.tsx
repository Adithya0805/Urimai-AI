"use client";

import { EligibleSchemeGuidance, EligibleScheme } from "@/lib/api";
import AudioButton from "./AudioButton";

interface UrimaiSlipProps {
  personName: string;
  age?: number;
  district?: string;
  schemes: (EligibleSchemeGuidance | EligibleScheme)[];
  onClose?: () => void;
}

export default function UrimaiSlip({
  personName,
  age,
  district,
  schemes,
  onClose,
}: UrimaiSlipProps) {
  const allDocs = Array.from(
    new Set(
      schemes.flatMap((s) => (s as any).required_documents || [])
    )
  );

  const handlePrint = () => {
    window.print();
  };

  const handleWhatsAppShare = () => {
    const text = `*உரிமை AI — அரசு நலத்திட்ட உரிமைச் சீட்டு*\n\nபெயர்: ${personName}\nதகுதி பெற்ற திட்டங்கள் (${schemes.length}):\n${schemes
      .map((s, i) => `${i + 1}. ${s.name_tamil} (${s.benefit_amount})`)
      .join("\n")}\n\nதேவையான ஆவணங்கள்:\n${allDocs.map((d) => `• ${d}`).join("\n")}\n\nவிவரங்களை சரிபார்க்க: ${window.location.href}`;
    const url = `https://api.whatsapp.com/send?text=${encodeURIComponent(text)}`;
    window.open(url, "_blank");
  };

  const audioSummary = `${personName} அவர்களுக்கு ${schemes.length} தமிழ்நாடு அரசு திட்டங்களில் உரிமை உள்ளது. ${schemes
    .map((s) => `${s.name_tamil}, உதவித்தொகை ${s.benefit_amount}.`)
    .join(" ")}`;

  return (
    <div className="bg-white border-2 border-emerald-800 rounded-2xl p-5 sm:p-7 shadow-lg max-w-2xl mx-auto my-4 relative overflow-hidden">
      {/* Top Banner */}
      <div className="border-b-2 border-emerald-800 pb-4 mb-5 text-center relative">
        <div className="inline-block bg-emerald-800 text-white text-xs font-bold px-3 py-1 rounded-full uppercase tracking-wider mb-2">
          அரசு நலத்திட்ட உரிமைச் சீட்டு (Citizen Entitlement Slip)
        </div>
        <h2 className="text-xl sm:text-2xl font-bold text-emerald-950">
          உரிமை AI — மக்கள் தகவல் சீட்டு
        </h2>
        <p className="text-xs text-slate-600 mt-1">
          தமிழ்நாடு அரசு நலத்திட்ட வழிகாட்டி மையம் • தமிழ்நாடு அரசு
        </p>

        <div className="mt-3 flex items-center justify-center space-x-2">
          <AudioButton textToSpeak={audioSummary} label="சீட்டை முழுமையாக கேட்க" />
        </div>
      </div>

      {/* Citizen Snapshot */}
      <div className="bg-emerald-50 rounded-xl p-4 border border-emerald-200 mb-5 flex flex-wrap justify-between items-center gap-2">
        <div>
          <span className="text-xs font-bold text-emerald-800 block">பயனாளர் பெயர்</span>
          <span className="text-lg font-bold text-slate-900">{personName}</span>
        </div>
        {age && (
          <div>
            <span className="text-xs font-bold text-emerald-800 block">வயது</span>
            <span className="text-base font-semibold text-slate-800">{age} ஆண்டுகள்</span>
          </div>
        )}
        {district && (
          <div>
            <span className="text-xs font-bold text-emerald-800 block">மாவட்டம்</span>
            <span className="text-base font-semibold text-slate-800">{district}</span>
          </div>
        )}
        <div>
          <span className="text-xs font-bold text-emerald-800 block">தகுதி பெற்ற திட்டங்கள்</span>
          <span className="text-lg font-bold text-emerald-700">{schemes.length} திட்டங்கள்</span>
        </div>
      </div>

      {/* Matched Schemes List */}
      <div className="mb-5">
        <h3 className="font-bold text-base text-slate-900 mb-3 flex items-center space-x-2">
          <span>🟢</span>
          <span>தாங்கள் பெறக்கூடிய அரசு உதவிகள்</span>
        </h3>
        <div className="space-y-3">
          {schemes.map((scheme, idx) => (
            <div
              key={scheme.scheme_code || idx}
              className="border border-slate-200 rounded-xl p-3.5 bg-slate-50 flex items-start justify-between"
            >
              <div>
                <span className="font-bold text-sm sm:text-base text-emerald-950 block">
                  {idx + 1}. {scheme.name_tamil}
                </span>
                <span className="text-xs text-slate-600 block mt-0.5">
                  {scheme.name_english}
                </span>
                {(scheme as any).department && (
                  <span className="text-xs bg-slate-200 text-slate-800 px-2 py-0.5 rounded font-mono inline-block mt-1">
                    {(scheme as any).department}
                  </span>
                )}
              </div>
              <div className="text-right pl-3 flex-shrink-0">
                <span className="text-xs font-semibold text-emerald-800 block">உதவித்தொகை</span>
                <span className="font-bold text-sm sm:text-base text-emerald-700 bg-emerald-100 px-2.5 py-1 rounded-lg inline-block">
                  {scheme.benefit_amount}
                </span>
              </div>
            </div>
          ))}
        </div>
      </div>

      {/* Physical Document Checklist */}
      {allDocs.length > 0 && (
        <div className="mb-6 bg-amber-50/70 border border-amber-200 rounded-xl p-4">
          <h3 className="font-bold text-sm sm:text-base text-amber-950 mb-2 flex items-center space-x-2">
            <span>📄</span>
            <span>நேரில் எடுத்துச் செல்ல வேண்டிய அசல் ஆவணங்கள்:</span>
          </h3>
          <ul className="grid grid-cols-1 sm:grid-cols-2 gap-2 text-xs sm:text-sm text-slate-800">
            {allDocs.map((doc, idx) => (
              <li key={idx} className="flex items-center space-x-2 bg-white p-2 rounded-lg border border-amber-100">
                <span className="text-emerald-700 font-bold">✓</span>
                <span>{doc}</span>
              </li>
            ))}
          </ul>
        </div>
      )}

      {/* Action Buttons (Hidden on Print) */}
      <div className="flex flex-wrap gap-3 pt-3 border-t border-slate-200 no-print">
        <button
          onClick={handlePrint}
          className="tap-target flex-1 min-w-[140px] px-4 py-3 bg-emerald-800 hover:bg-emerald-900 text-white font-bold rounded-xl shadow transition-all flex items-center justify-center space-x-2"
        >
          <span>🖨️</span>
          <span>சீட்டு அச்சிட (Print / PDF)</span>
        </button>

        <button
          onClick={handleWhatsAppShare}
          className="tap-target flex-1 min-w-[140px] px-4 py-3 bg-[#25D366] hover:bg-[#1EBE5D] text-white font-bold rounded-xl shadow transition-all flex items-center justify-center space-x-2"
        >
          <span>📲</span>
          <span>WhatsApp பகிர்க</span>
        </button>

        {onClose && (
          <button
            onClick={onClose}
            className="tap-target px-4 py-3 bg-slate-200 hover:bg-slate-300 text-slate-800 font-bold rounded-xl transition-all"
          >
            மூடு
          </button>
        )}
      </div>
    </div>
  );
}
