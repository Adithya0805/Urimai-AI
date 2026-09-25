"use client";

import { useEffect, useState, use } from "react";
import Link from "next/link";
import Header from "@/components/Header";
import AudioButton from "@/components/AudioButton";
import { api, Family, Person } from "@/lib/api";

export default function FamilyDashboardPage({
  params,
}: {
  params: Promise<{ familyId: string }>;
}) {
  const resolvedParams = use(params);
  const familyId = resolvedParams.familyId;

  const [family, setFamily] = useState<Family | null>(null);
  const [familyGuidance, setFamilyGuidance] = useState<any | null>(null);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState<string | null>(null);

  // Add person modal state
  const [showAddMember, setShowAddMember] = useState(false);
  const [newPerson, setNewPerson] = useState({
    name: "",
    age: 20,
    gender: "male",
    education_level: "secondary",
    occupation: "student",
    marital_status: "single",
    caste_category: "BC",
    disability_status: false,
    special_flags: [] as string[],
  });

  const loadFamilyData = async () => {
    try {
      setLoading(true);
      const [famData, guideData] = await Promise.all([
        api.getFamily(familyId),
        api.getFamilyGuidance(familyId),
      ]);
      setFamily(famData);
      setFamilyGuidance(guideData);
    } catch (err: any) {
      setError(err.message || "குடும்ப விவரங்களைப் பெறுவதில் பிழை.");
    } finally {
      setLoading(false);
    }
  };

  useEffect(() => {
    loadFamilyData();
  }, [familyId]);

  const handleAddMemberSubmit = async (e: React.FormEvent) => {
    e.preventDefault();
    try {
      await api.addPerson(familyId, {
        name: newPerson.name.trim() || "உறுப்பினர்",
        age: Number(newPerson.age),
        gender: newPerson.gender as any,
        education_level: newPerson.education_level as any,
        occupation: newPerson.occupation as any,
        marital_status: newPerson.marital_status as any,
        caste_category: newPerson.caste_category as any,
        disability_status: Boolean(newPerson.disability_status),
        special_flags: newPerson.special_flags,
      });
      setShowAddMember(false);
      loadFamilyData();
    } catch (err: any) {
      alert("உறுப்பினரை சேர்ப்பதில் பிழை: " + err.message);
    }
  };

  if (loading) {
    return (
      <div className="min-h-screen flex flex-col bg-[#FBF9F5]">
        <Header />
        <div className="flex-1 flex flex-col items-center justify-center p-8 text-center">
          <div className="w-16 h-16 border-4 border-emerald-600 border-t-transparent rounded-full animate-spin mb-4" />
          <h2 className="text-lg font-bold text-slate-800">
            குடும்ப விவரங்கள் ஏற்றப்படுகின்றன...
          </h2>
        </div>
      </div>
    );
  }

  if (error || !family) {
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

  const members = family.persons || [];

  return (
    <div className="min-h-screen flex flex-col bg-[#FBF9F5]">
      <Header />

      <main className="flex-1 max-w-4xl w-full mx-auto px-4 py-6 sm:py-8">
        {/* Household Overview Header */}
        <div className="gov-card p-6 bg-gradient-to-br from-emerald-950 to-emerald-900 text-white rounded-2xl mb-6 shadow-md">
          <div className="flex flex-wrap items-center justify-between gap-3 mb-4">
            <div>
              <span className="text-xs font-bold uppercase tracking-wider bg-emerald-800 text-emerald-200 px-3 py-1 rounded-full inline-block mb-1">
                குடும்ப நல பலகை (Family Dashboard)
              </span>
              <h1 className="text-2xl sm:text-3xl font-extrabold">
                {family.taluk}, {family.district} — குடும்பம்
              </h1>
            </div>

            <button
              onClick={() => setShowAddMember(true)}
              className="tap-target px-4 py-2.5 bg-amber-400 hover:bg-amber-300 text-slate-950 font-bold rounded-xl text-xs sm:text-sm shadow flex items-center space-x-1.5"
            >
              <span>➕</span>
              <span>புதிய உறுப்பினர் சேர்க்க</span>
            </button>
          </div>

          <div className="grid grid-cols-2 sm:grid-cols-4 gap-3 bg-emerald-900/60 p-3.5 rounded-xl border border-emerald-700/60 text-xs sm:text-sm">
            <div>
              <span className="text-emerald-300 block text-xs">குடும்ப அட்டை</span>
              <span className="font-bold">{family.ration_card_type}</span>
            </div>
            <div>
              <span className="text-emerald-300 block text-xs">மாத வருமானம்</span>
              <span className="font-bold">₹{Number(family.total_household_income).toLocaleString("en-IN")}</span>
            </div>
            <div>
              <span className="text-emerald-300 block text-xs">உறுப்பினர்கள்</span>
              <span className="font-bold">{members.length} நபர்கள்</span>
            </div>
            <div>
              <span className="text-emerald-300 block text-xs">அமைப்பு</span>
              <span className="font-bold">{family.composition_type}</span>
            </div>
          </div>
        </div>

        {/* Members List */}
        <div className="mb-8">
          <h2 className="text-lg sm:text-xl font-bold text-slate-900 mb-4 flex items-center space-x-2">
            <span>👥</span>
            <span>குடும்ப உறுப்பினர்கள் ({members.length})</span>
          </h2>

          <div className="space-y-4">
            {members.map((person, idx) => {
              const personGuidance = familyGuidance?.members_guidance?.find(
                (m: any) => m.person_id === person.id
              );
              const eligibleCount = personGuidance?.eligible_schemes_count ?? 0;

              return (
                <div
                  key={person.id || idx}
                  className="gov-card p-5 sm:p-6 bg-white border-2 border-slate-200 hover:border-emerald-600 transition-all"
                >
                  <div className="flex flex-col sm:flex-row sm:items-center justify-between gap-4">
                    <div>
                      <div className="flex items-center space-x-2 mb-1">
                        <span className="font-bold text-lg text-slate-900">
                          {person.name}
                        </span>
                        <span className="text-xs bg-slate-100 text-slate-700 px-2 py-0.5 rounded font-semibold">
                          {person.age} வயது
                        </span>
                        <span className="text-xs bg-emerald-100 text-emerald-800 px-2 py-0.5 rounded font-semibold">
                          {person.gender === "female" ? "பெண்" : person.gender === "male" ? "ஆண்" : "மூன்றாம் பாலினம்"}
                        </span>
                      </div>
                      <p className="text-xs text-slate-600">
                        தொழில்: <strong>{person.occupation}</strong> • சமூகப் பிரிவு: <strong>{person.caste_category}</strong> • கல்வி: <strong>{person.education_level}</strong>
                      </p>
                    </div>

                    <div className="flex items-center space-x-3 flex-shrink-0">
                      <div className="text-right">
                        <span className="text-xs text-slate-500 block">தகுதி பெற்றவை</span>
                        <span className="text-base font-extrabold text-emerald-700">
                          {eligibleCount} திட்டங்கள்
                        </span>
                      </div>

                      <Link
                        href={`/results?person_id=${person.id}&family_id=${familyId}`}
                        className="tap-target px-4 py-2.5 bg-[#0D5C3A] hover:bg-[#083B25] text-white font-bold rounded-xl text-xs sm:text-sm shadow flex items-center space-x-1"
                      >
                        <span>தகுதி பார்க்க</span>
                        <span>→</span>
                      </Link>
                    </div>
                  </div>
                </div>
              );
            })}
          </div>
        </div>

        {/* Add Member Modal */}
        {showAddMember && (
          <div className="fixed inset-0 bg-black/50 z-50 flex items-center justify-center p-4">
            <div className="bg-white rounded-2xl p-6 max-w-lg w-full max-h-[90vh] overflow-y-auto border-2 border-emerald-800 shadow-2xl">
              <div className="flex items-center justify-between mb-4 border-b pb-2">
                <h3 className="font-bold text-lg text-slate-900">
                  புதிய உறுப்பினர் சேர்க்க
                </h3>
                <button
                  onClick={() => setShowAddMember(false)}
                  className="text-slate-500 hover:text-slate-800 text-lg font-bold"
                >
                  ✕
                </button>
              </div>

              <form onSubmit={handleAddMemberSubmit} className="space-y-4">
                <div>
                  <label className="block text-xs font-bold text-slate-800 mb-1">
                    பெயர் (Name):
                  </label>
                  <input
                    type="text"
                    required
                    value={newPerson.name}
                    onChange={(e) => setNewPerson({ ...newPerson, name: e.target.value })}
                    placeholder="உதாரணம்: கார்த்திக்"
                    className="tap-target w-full p-3 border-2 border-slate-300 rounded-xl text-sm"
                  />
                </div>

                <div className="grid grid-cols-2 gap-3">
                  <div>
                    <label className="block text-xs font-bold text-slate-800 mb-1">
                      வயது (Age):
                    </label>
                    <input
                      type="number"
                      required
                      min="1"
                      value={newPerson.age}
                      onChange={(e) => setNewPerson({ ...newPerson, age: Number(e.target.value) })}
                      className="tap-target w-full p-3 border-2 border-slate-300 rounded-xl text-sm"
                    />
                  </div>

                  <div>
                    <label className="block text-xs font-bold text-slate-800 mb-1">
                      பாலினம் (Gender):
                    </label>
                    <select
                      value={newPerson.gender}
                      onChange={(e) => setNewPerson({ ...newPerson, gender: e.target.value })}
                      className="tap-target w-full p-3 border-2 border-slate-300 rounded-xl text-sm"
                    >
                      <option value="male">ஆண்</option>
                      <option value="female">பெண்</option>
                      <option value="transgender">மூன்றாம் பாலினம்</option>
                    </select>
                  </div>
                </div>

                <div>
                  <label className="block text-xs font-bold text-slate-800 mb-1">
                    தொழில் (Occupation):
                  </label>
                  <select
                    value={newPerson.occupation}
                    onChange={(e) => setNewPerson({ ...newPerson, occupation: e.target.value })}
                    className="tap-target w-full p-3 border-2 border-slate-300 rounded-xl text-sm"
                  >
                    <option value="student">மாணவர் (Student)</option>
                    <option value="farmer">விவசாயி (Farmer)</option>
                    <option value="daily_wage">கூலித் தொழிலாளி (Daily Wage)</option>
                    <option value="homemaker">குடும்பத்தலைவி (Homemaker)</option>
                    <option value="unemployed">வேலையில்லாதவர் (Unemployed)</option>
                    <option value="self_employed">சுயதொழில் (Self Employed)</option>
                    <option value="private_employee">தனியார் ஊழியர்</option>
                    <option value="govt_employee">அரசு ஊழியர்</option>
                  </select>
                </div>

                <div className="flex gap-3 pt-3">
                  <button
                    type="button"
                    onClick={() => setShowAddMember(false)}
                    className="tap-target flex-1 py-3 bg-slate-200 text-slate-800 font-bold rounded-xl"
                  >
                    ரத்து
                  </button>
                  <button
                    type="submit"
                    className="tap-target flex-1 py-3 bg-[#0D5C3A] text-white font-bold rounded-xl shadow"
                  >
                    சேர்க்கவும்
                  </button>
                </div>
              </form>
            </div>
          </div>
        )}
      </main>
    </div>
  );
}
