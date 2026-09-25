"use client";

import { useEffect, useState } from "react";
import Link from "next/link";
import Header from "@/components/Header";
import AudioButton from "@/components/AudioButton";
import { api, EligibleScheme } from "@/lib/api";

const DEPARTMENTS = [
  { id: "", label: "அனைத்து துறைகள் (All)" },
  { id: "Social Welfare", label: "👩‍👧 சமூக நலம் & மகளிர்" },
  { id: "Education", label: "🎓 பள்ளி & உயர்கல்வி" },
  { id: "Agriculture", label: "🌾 வேளாண்மை & உழவர் நலம்" },
  { id: "Labour", label: "👷 தொழிலாளர் நல வாரியம்" },
];

export default function SchemesCatalogPage() {
  const [schemes, setSchemes] = useState<EligibleScheme[]>([]);
  const [selectedDept, setSelectedDept] = useState("");
  const [searchTerm, setSearchTerm] = useState("");
  const [loading, setLoading] = useState(true);
  const [errorMessage, setErrorMessage] = useState<string | null>(null);

  useEffect(() => {
    async function loadSchemes() {
      try {
        setLoading(true);
        setErrorMessage(null);
        const data = await api.getSchemes(selectedDept || undefined);
        setSchemes(data);
      } catch (err: any) {
        setErrorMessage(err.message || "திட்டங்கள் விவரங்களை ஏற்றுவதில் பிழை ஏற்பட்டது.");
      } finally {
        setLoading(false);
      }
    }
    loadSchemes();
  }, [selectedDept]);

  const filteredSchemes = schemes.filter(
    (s) =>
      s.name_tamil.toLowerCase().includes(searchTerm.toLowerCase()) ||
      s.name_english.toLowerCase().includes(searchTerm.toLowerCase()) ||
      s.scheme_code.toLowerCase().includes(searchTerm.toLowerCase()) ||
      s.category.toLowerCase().includes(searchTerm.toLowerCase())
  );

  return (
    <div className="min-h-screen flex flex-col bg-[#FBF9F5]">
      <Header />

      <main className="flex-1 max-w-4xl w-full mx-auto px-4 py-6 sm:py-8">
        <div className="mb-6">
          <h1 className="text-2xl sm:text-3xl font-extrabold text-emerald-950 mb-1">
            📋 தமிழ்நாடு அரசு நலத்திட்டங்கள் பட்டியல்
          </h1>
          <p className="text-xs sm:text-sm text-slate-600">
            அதிகாரப்பூர்வ அரசாணைகள் மற்றும் வழிகாட்டுதல்களுடன் கூடிய முழு பட்டியல்.
          </p>
        </div>

        {/* Search Bar */}
        <div className="mb-5">
          <input
            type="text"
            value={searchTerm}
            onChange={(e) => setSearchTerm(e.target.value)}
            placeholder="திட்டத்தின் பெயர் அல்லது துறையைத் தேடவும்..."
            className="tap-target w-full p-4 bg-white border-2 border-slate-300 rounded-2xl text-base text-slate-900 shadow-sm"
          />
        </div>

        {/* Department Filter Tabs */}
        <div className="flex overflow-x-auto gap-2 pb-3 mb-6 scrollbar-thin">
          {DEPARTMENTS.map((dept) => (
            <button
              key={dept.id}
              onClick={() => setSelectedDept(dept.id)}
              className={`tap-target flex-shrink-0 px-4 py-2.5 rounded-xl font-bold text-xs sm:text-sm whitespace-nowrap transition-all border-2 ${
                selectedDept === dept.id
                  ? "bg-[#0D5C3A] text-white border-[#0D5C3A] shadow"
                  : "bg-white text-slate-800 border-slate-200 hover:border-slate-300"
              }`}
            >
              {dept.label}
            </button>
          ))}
        </div>

        {/* Schemes List */}
        {loading ? (
          <div className="p-12 text-center text-slate-600 font-bold">
            திட்டங்கள் ஏற்றப்படுகின்றன...
          </div>
        ) : filteredSchemes.length === 0 ? (
          <div className="gov-card p-8 text-center text-slate-600">
            தேடலுக்குரிய திட்டங்கள் எதுவும் கிடைக்கவில்லை.
          </div>
        ) : (
          <div className="space-y-4">
            {filteredSchemes.map((scheme) => (
              <div
                key={scheme.scheme_code}
                className="gov-card p-5 sm:p-6 bg-white border-2 border-slate-200 hover:border-emerald-600 transition-all"
              >
                <div className="flex flex-col sm:flex-row sm:items-start justify-between gap-3 mb-2">
                  <div>
                    <div className="flex items-center space-x-2 mb-1">
                      <span className="text-xs bg-emerald-100 text-emerald-800 font-bold px-2 py-0.5 rounded">
                        {scheme.category}
                      </span>
                      <span className="text-xs font-mono text-slate-500">
                        {scheme.scheme_code}
                      </span>
                    </div>
                    <h2 className="text-lg font-bold text-slate-900">
                      {scheme.name_tamil}
                    </h2>
                    <p className="text-xs text-slate-600">
                      {scheme.name_english} • {scheme.department}
                    </p>
                  </div>

                  <div className="bg-emerald-50 border border-emerald-200 rounded-xl p-2.5 text-right flex-shrink-0">
                    <span className="text-xs font-bold text-emerald-800 block">உதவித்தொகை</span>
                    <span className="text-base font-extrabold text-emerald-700">
                      {scheme.benefit_amount}
                    </span>
                  </div>
                </div>

                <p className="text-xs sm:text-sm text-slate-700 mb-3 bg-slate-50 p-3 rounded-lg border border-slate-100">
                  {scheme.description_tamil}
                </p>

                <div className="flex flex-wrap items-center justify-between gap-3 pt-3 border-t border-slate-100 text-xs">
                  <div className="flex items-center space-x-2">
                    <AudioButton
                      textToSpeak={`${scheme.name_tamil}. உதவித்தொகை ${scheme.benefit_amount}. ${scheme.description_tamil}`}
                      label="விளக்கம் கேட்க"
                    />
                  </div>

                  <a
                    href={scheme.source_url}
                    target="_blank"
                    rel="noopener noreferrer"
                    className="tap-target text-blue-700 hover:text-blue-900 font-bold flex items-center space-x-1"
                  >
                    <span>அரசாணை / தளம்</span>
                    <span>↗</span>
                  </a>
                </div>
              </div>
            ))}
          </div>
        )}
      </main>
    </div>
  );
}
