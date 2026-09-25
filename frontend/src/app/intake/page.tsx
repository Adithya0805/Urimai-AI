"use client";

import { useState, useEffect, Suspense } from "react";
import { useRouter, useSearchParams } from "next/navigation";
import Header from "@/components/Header";
import AudioButton from "@/components/AudioButton";
import { startSpeechRecognition, speakTamil } from "@/lib/audio";
import { api } from "@/lib/api";

const TN_DISTRICTS = [
  "சென்னை", "மதுரை", "கோயம்புத்தூர்", "திருச்சிராப்பள்ளி", "சேலம்",
  "தஞ்சாவூர்", "திருநெல்வேலி", "ஈரோடு", "வேலூர்", "திண்டுக்கல்",
  "கடலூர்", "காஞ்சிபுரம்", "திருவள்ளூர்", "திருப்பூர்", "தூத்துக்குடி",
  "விருதுநகர்", "நாகப்பட்டினம்", "சிவகங்கை", "புதுக்கோட்டை", "கரூர்"
];

function IntakeContent() {
  const router = useRouter();
  const searchParams = useSearchParams();
  const isIndividualOnly = searchParams.get("mode") === "individual";

  // Form Step State
  const [step, setStep] = useState<number>(1);
  const [isSubmitting, setIsSubmitting] = useState(false);
  const [errorMessage, setErrorMessage] = useState<string | null>(null);
  const [isListening, setIsListening] = useState(false);
  const [speechRecognizer, setSpeechRecognizer] = useState<{ stop: () => void } | null>(null);

  // Form Data State
  const [familyData, setFamilyData] = useState({
    composition_type: isIndividualOnly ? "single" : "nuclear",
    district: "மதுரை",
    taluk: "மதுரை வடக்கு",
    address: "தெற்கு மாசி வீதி",
    ration_card_type: "green",
    total_household_income: 8000,
  });

  const [personData, setPersonData] = useState({
    name: "",
    age: 35,
    gender: "female",
    education_level: "secondary",
    occupation: "homemaker",
    occupation_detail: "",
    marital_status: "married",
    caste_category: "BC",
    disability_status: false,
    disability_type: "",
    special_flags: [] as string[],
    land_holding_acres: 0,
    crop_type: "paddy",
  });

  // Calculate total steps
  const totalSteps = personData.occupation === "farmer" ? 9 : 8;

  const currentQuestionText = () => {
    switch (step) {
      case 1:
        return "தங்கள் குடும்ப அட்டை (Ration Card) என்ன வகை?";
      case 2:
        return "தங்கள் மாவட்டம் மற்றும் வசிப்பிடத்தை தேர்ந்தெடுக்கவும்.";
      case 3:
        return "குடும்பத்தின் மொத்த மாத வருமானம் தோராயமாக எவ்வளவு?";
      case 4:
        return "பயனாளரின் பெயர் மற்றும் வயது என்ன?";
      case 5:
        return "பயனாளரின் பாலினம் மற்றும் திருமண நிலை என்ன?";
      case 6:
        return "பயனாளரின் தொழில் மற்றும் கல்வித் தகுதி என்ன?";
      case 7:
        if (personData.occupation === "farmer") {
          return "விவசாய நில விவரம்: எத்தனை ஏக்கர் நிலம் உள்ளது? பயிரிடப்படும் பயிர் என்ன?";
        }
        return "சமூகப் பிரிவு (Caste Category) என்ன?";
      case 8:
        if (personData.occupation === "farmer") {
          return "சமூகப் பிரிவு (Caste Category) என்ன?";
        }
        return "மாற்றுத்திறனாளி நிலை மற்றும் சிறப்புப் பிரிவுகள் ஏதேனும் உள்ளதா?";
      case 9:
        return "மாற்றுத்திறனாளி நிலை மற்றும் சிறப்புப் பிரிவுகள் ஏதேனும் உள்ளதா?";
      default:
        return "விவரங்களை உறுதி செய்து சேமிக்கவும்.";
    }
  };

  const handleVoiceInput = () => {
    if (isListening && speechRecognizer) {
      speechRecognizer.stop();
      setIsListening(false);
      return;
    }

    setIsListening(true);
    const rec = startSpeechRecognition(
      (transcript) => {
        setIsListening(false);
        // Handle name or number voice inputs
        if (step === 4) {
          // If transcript contains numbers
          const matchNum = transcript.match(/\d+/);
          if (matchNum) {
            setPersonData((p) => ({ ...p, age: parseInt(matchNum[0], 10) }));
          } else {
            setPersonData((p) => ({ ...p, name: transcript }));
          }
        }
      },
      () => setIsListening(false)
    );
    setSpeechRecognizer(rec);
  };

  const toggleSpecialFlag = (flag: string) => {
    setPersonData((prev) => {
      const exists = prev.special_flags.includes(flag);
      return {
        ...prev,
        special_flags: exists
          ? prev.special_flags.filter((f) => f !== flag)
          : [...prev.special_flags, flag],
      };
    });
  };

  const handleSubmit = async () => {
    setIsSubmitting(true);
    setErrorMessage(null);

    try {
      // 1. Create family
      const createdFamily = await api.createFamily({
        composition_type: familyData.composition_type as any,
        district: familyData.district,
        taluk: familyData.taluk,
        address: familyData.address,
        ration_card_type: familyData.ration_card_type as any,
        total_household_income: Number(familyData.total_household_income),
      });

      // 2. Add Person
      const createdPerson = await api.addPerson(createdFamily.id, {
        name: personData.name.trim() || "பயனாளர்",
        age: Number(personData.age),
        gender: personData.gender as any,
        education_level: personData.education_level as any,
        occupation: personData.occupation as any,
        occupation_detail: personData.occupation_detail || undefined,
        marital_status: personData.marital_status as any,
        caste_category: personData.caste_category as any,
        disability_status: Boolean(personData.disability_status),
        disability_type: personData.disability_type || undefined,
        special_flags: personData.special_flags,
        land_holding_acres: Number(personData.land_holding_acres) || 0,
        crop_type: personData.crop_type || undefined,
      });

      // Speak confirmation
      speakTamil("தங்கள் விவரங்கள் வெற்றிகரமாக பதிவு செய்யப்பட்டன. தகுதி முடிவுகளை இப்போது பார்க்கலாம்.");

      // Navigate to results
      router.push(`/results?person_id=${createdPerson.id}&family_id=${createdFamily.id}`);
    } catch (err: any) {
      setErrorMessage(err.message || "விவரங்களை சேமிப்பதில் பிழை ஏற்பட்டது. மீண்டும் முயற்சிக்கவும்.");
      setIsSubmitting(false);
    }
  };

  return (
    <div className="min-h-screen flex flex-col bg-[#FBF9F5]">
      <Header />

      <main className="flex-1 max-w-2xl w-full mx-auto px-4 py-6 sm:py-8">
        {/* Step Progress Header */}
        <div className="mb-6">
          <div className="flex items-center justify-between text-xs sm:text-sm font-bold text-emerald-950 mb-2">
            <span>படி {step} / {totalSteps + 1}</span>
            <span>{Math.round((step / (totalSteps + 1)) * 100)}% முடிந்தது</span>
          </div>
          <div className="w-full bg-slate-200 h-2.5 rounded-full overflow-hidden">
            <div
              className="bg-[#0D5C3A] h-full transition-all duration-300 rounded-full"
              style={{ width: `${(step / (totalSteps + 1)) * 100}%` }}
            />
          </div>
        </div>

        {/* Question Box */}
        <div className="gov-card p-5 sm:p-7 mb-6 shadow-sm border-2 border-emerald-900/10">
          <div className="flex items-start justify-between gap-3 mb-5 border-b border-slate-200 pb-3">
            <h1 className="text-lg sm:text-xl font-bold text-slate-900 leading-snug">
              {currentQuestionText()}
            </h1>
            <AudioButton textToSpeak={currentQuestionText()} label="கேட்க" />
          </div>

          {/* STEP 1: Ration Card Type */}
          {step === 1 && (
            <div className="space-y-3">
              {[
                { id: "green", label: "🟢 பச்சை அட்டை (PHH - அரிசி கார்டு)", desc: "அனைத்து அரிசி மற்றும் இலவச பொருட்கள்" },
                { id: "white", label: "⚪ வெள்ளை அட்டை (NPHH-Sugar - சர்க்கரை கார்டு)", desc: "சர்க்கரை மட்டும் / பொருளற்ற அட்டை" },
                { id: "phh_aay", label: "⭐ அந்தியோதயா அட்டை (AAY)", desc: "35 கிலோ இலவச அரிசி பெறும் குடும்பங்கள்" },
                { id: "khaki", label: "👮 காக்கி அட்டை (Police)", desc: "காவல்துறை குடும்பங்களுக்கான அட்டை" },
                { id: "none", label: "❌ ரேஷன் கார்டு இல்லை", desc: "குடும்ப அட்டை இதுவரை பெறாதவர்கள்" },
              ].map((opt) => (
                <button
                  key={opt.id}
                  type="button"
                  onClick={() => setFamilyData({ ...familyData, ration_card_type: opt.id })}
                  className={`tap-target w-full text-left p-4 rounded-xl border-2 transition-all flex flex-col justify-center ${
                    familyData.ration_card_type === opt.id
                      ? "border-[#0D5C3A] bg-emerald-50 text-[#0D5C3A] font-bold shadow-sm"
                      : "border-slate-200 bg-white text-slate-800 hover:border-slate-300"
                  }`}
                >
                  <span className="text-base">{opt.label}</span>
                  <span className="text-xs text-slate-500 mt-0.5">{opt.desc}</span>
                </button>
              ))}
            </div>
          )}

          {/* STEP 2: District & Taluk */}
          {step === 2 && (
            <div className="space-y-4">
              <div>
                <label className="block text-sm font-bold text-slate-900 mb-2">
                  மாவட்டம் (District):
                </label>
                <select
                  value={familyData.district}
                  onChange={(e) => setFamilyData({ ...familyData, district: e.target.value })}
                  className="tap-target w-full p-3.5 bg-white border-2 border-slate-300 rounded-xl text-base font-semibold text-slate-900"
                >
                  {TN_DISTRICTS.map((dist) => (
                    <option key={dist} value={dist}>{dist}</option>
                  ))}
                </select>
              </div>

              <div>
                <label className="block text-sm font-bold text-slate-900 mb-2">
                  வட்டம் / தாலுகா (Taluk):
                </label>
                <input
                  type="text"
                  value={familyData.taluk}
                  onChange={(e) => setFamilyData({ ...familyData, taluk: e.target.value })}
                  placeholder="உதாரணம்: மதுரை வடக்கு"
                  className="tap-target w-full p-3.5 bg-white border-2 border-slate-300 rounded-xl text-base text-slate-900"
                />
              </div>

              <div>
                <label className="block text-sm font-bold text-slate-900 mb-2">
                  முகவரி (Address):
                </label>
                <input
                  type="text"
                  value={familyData.address}
                  onChange={(e) => setFamilyData({ ...familyData, address: e.target.value })}
                  placeholder="கதவு எண், தெரு பெயர், ஊர்"
                  className="tap-target w-full p-3.5 bg-white border-2 border-slate-300 rounded-xl text-base text-slate-900"
                />
              </div>
            </div>
          )}

          {/* STEP 3: Monthly Household Income */}
          {step === 3 && (
            <div className="space-y-4">
              <p className="text-xs text-slate-600">
                குடும்பத்தின் அனைத்து உறுப்பினர்களின் மாத வருமானத்தின் கூட்டுத்தொகை.
              </p>

              <div className="grid grid-cols-2 sm:grid-cols-3 gap-2.5">
                {[0, 5000, 8000, 10000, 15000, 20000, 25000].map((amt) => (
                  <button
                    key={amt}
                    type="button"
                    onClick={() => setFamilyData({ ...familyData, total_household_income: amt })}
                    className={`tap-target p-3 rounded-xl border-2 font-bold text-sm ${
                      familyData.total_household_income === amt
                        ? "border-[#0D5C3A] bg-emerald-50 text-[#0D5C3A]"
                        : "border-slate-200 bg-white text-slate-800"
                    }`}
                  >
                    {amt === 0 ? "வருமானம் இல்லை (₹0)" : `₹${amt.toLocaleString("en-IN")}`}
                  </button>
                ))}
              </div>

              <div className="pt-2">
                <label className="block text-xs font-bold text-slate-700 mb-1">
                  வேறு தொகையை உள்ளிட (Custom Amount in ₹):
                </label>
                <input
                  type="number"
                  value={familyData.total_household_income}
                  onChange={(e) => setFamilyData({ ...familyData, total_household_income: Number(e.target.value) })}
                  className="tap-target w-full p-3.5 bg-white border-2 border-slate-300 rounded-xl text-lg font-bold text-slate-900"
                  min="0"
                />
              </div>
            </div>
          )}

          {/* STEP 4: Name & Age */}
          {step === 4 && (
            <div className="space-y-4">
              <div>
                <label className="block text-sm font-bold text-slate-900 mb-2">
                  பயனாளர் பெயர் (Full Name):
                </label>
                <div className="flex gap-2">
                  <input
                    type="text"
                    value={personData.name}
                    onChange={(e) => setPersonData({ ...personData, name: e.target.value })}
                    placeholder="உதாரணம்: மீனாட்சி அம்மாள்"
                    className="tap-target flex-1 p-3.5 bg-white border-2 border-slate-300 rounded-xl text-base text-slate-900"
                  />
                  <button
                    type="button"
                    onClick={handleVoiceInput}
                    className={`tap-target px-3.5 rounded-xl border-2 font-bold text-sm ${
                      isListening
                        ? "bg-red-500 text-white border-red-600 animate-pulse"
                        : "bg-slate-100 text-slate-800 border-slate-300"
                    }`}
                    title="குரல் மூலம் உள்ளிட"
                  >
                    {isListening ? "⏹️" : "🎤 குரல்"}
                  </button>
                </div>
              </div>

              <div>
                <label className="block text-sm font-bold text-slate-900 mb-2">
                  வயது (Age): <span className="text-emerald-800 font-extrabold text-xl ml-2">{personData.age} ஆண்டுகள்</span>
                </label>
                <div className="flex flex-wrap gap-2 mb-3">
                  {[18, 21, 30, 40, 50, 60, 65, 70].map((a) => (
                    <button
                      key={a}
                      type="button"
                      onClick={() => setPersonData({ ...personData, age: a })}
                      className={`tap-target px-3 py-2 rounded-lg border font-bold text-sm ${
                        personData.age === a
                          ? "bg-[#0D5C3A] text-white border-[#0D5C3A]"
                          : "bg-white text-slate-800 border-slate-200"
                      }`}
                    >
                      {a}
                    </button>
                  ))}
                </div>
                <input
                  type="number"
                  value={personData.age}
                  onChange={(e) => setPersonData({ ...personData, age: Number(e.target.value) })}
                  className="tap-target w-full p-3 bg-white border-2 border-slate-300 rounded-xl text-base text-slate-900"
                  min="1"
                  max="120"
                />
              </div>
            </div>
          )}

          {/* STEP 5: Gender & Marital Status */}
          {step === 5 && (
            <div className="space-y-5">
              <div>
                <label className="block text-sm font-bold text-slate-900 mb-2">
                  பாலினம் (Gender):
                </label>
                <div className="grid grid-cols-3 gap-2">
                  {[
                    { id: "female", label: "👩 பெண்" },
                    { id: "male", label: "👨 ஆண்" },
                    { id: "transgender", label: "⚧️ மூன்றாம் பாலினம்" },
                  ].map((g) => (
                    <button
                      key={g.id}
                      type="button"
                      onClick={() => setPersonData({ ...personData, gender: g.id })}
                      className={`tap-target p-3 rounded-xl border-2 font-bold text-sm text-center ${
                        personData.gender === g.id
                          ? "border-[#0D5C3A] bg-emerald-50 text-[#0D5C3A]"
                          : "border-slate-200 bg-white text-slate-800"
                      }`}
                    >
                      {g.label}
                    </button>
                  ))}
                </div>
              </div>

              <div>
                <label className="block text-sm font-bold text-slate-900 mb-2">
                  திருமண நிலை (Marital Status):
                </label>
                <div className="grid grid-cols-2 gap-2">
                  {[
                    { id: "married", label: "திருமணமானவர்" },
                    { id: "widowed", label: "விதவை (கணவர் மறைந்தவர்)" },
                    { id: "single", label: "திருமணமாகாதவர்" },
                    { id: "divorced", label: "விவாகரத்து / பிரிந்து வாழ்பவர்" },
                  ].map((m) => (
                    <button
                      key={m.id}
                      type="button"
                      onClick={() => setPersonData({ ...personData, marital_status: m.id })}
                      className={`tap-target p-3 rounded-xl border-2 font-bold text-xs sm:text-sm text-left ${
                        personData.marital_status === m.id
                          ? "border-[#0D5C3A] bg-emerald-50 text-[#0D5C3A]"
                          : "border-slate-200 bg-white text-slate-800"
                      }`}
                    >
                      {m.label}
                    </button>
                  ))}
                </div>
              </div>
            </div>
          )}

          {/* STEP 6: Occupation & Education */}
          {step === 6 && (
            <div className="space-y-5">
              <div>
                <label className="block text-sm font-bold text-slate-900 mb-2">
                  தொழில் (Occupation):
                </label>
                <div className="grid grid-cols-2 gap-2">
                  {[
                    { id: "farmer", label: "🌾 விவசாயி" },
                    { id: "daily_wage", label: "🔨 கூலித் தொழிலாளி" },
                    { id: "homemaker", label: "🏠 குடும்பத்தலைவி" },
                    { id: "unemployed", label: "🚫 வேலையில்லாதவர்" },
                    { id: "student", label: "🎓 மாணவர்" },
                    { id: "self_employed", label: "🏪 சுயதொழில்" },
                    { id: "private_employee", label: "🏢 தனியார் ஊழியர்" },
                    { id: "govt_employee", label: "🏛️ அரசு ஊழியர்" },
                  ].map((occ) => (
                    <button
                      key={occ.id}
                      type="button"
                      onClick={() => setPersonData({ ...personData, occupation: occ.id })}
                      className={`tap-target p-3 rounded-xl border-2 font-bold text-xs sm:text-sm text-left ${
                        personData.occupation === occ.id
                          ? "border-[#0D5C3A] bg-emerald-50 text-[#0D5C3A]"
                          : "border-slate-200 bg-white text-slate-800"
                      }`}
                    >
                      {occ.label}
                    </button>
                  ))}
                </div>
              </div>

              <div>
                <label className="block text-sm font-bold text-slate-900 mb-2">
                  கல்வித் தகுதி (Education Level):
                </label>
                <select
                  value={personData.education_level}
                  onChange={(e) => setPersonData({ ...personData, education_level: e.target.value })}
                  className="tap-target w-full p-3.5 bg-white border-2 border-slate-300 rounded-xl text-base text-slate-900"
                >
                  <option value="none">படிப்பறிவில்லை (No Formal Education)</option>
                  <option value="primary">தொடக்கக் கல்வி (1 முதல் 5 ஆம் வகுப்பு)</option>
                  <option value="secondary">உயர்நிலைக் கல்வி (10 ஆம் வகுப்பு)</option>
                  <option value="higher_secondary">மேல்நிலைக் கல்வி (12 ஆம் வகுப்பு)</option>
                  <option value="graduate">பட்டப்படிப்பு (Degree / Diploma)</option>
                  <option value="postgraduate">முதுகலை பட்டப்படிப்பு (PG)</option>
                  <option value="dropout">பள்ளி இடைநிற்றல் (Dropout)</option>
                </select>
              </div>
            </div>
          )}

          {/* STEP 7 (Only if Farmer): Agriculture Info */}
          {step === 7 && personData.occupation === "farmer" && (
            <div className="space-y-4">
              <div>
                <label className="block text-sm font-bold text-slate-900 mb-2">
                  நில உடைமை (Land Holding in Acres):
                </label>
                <div className="grid grid-cols-4 gap-2 mb-3">
                  {[0.5, 1.0, 2.5, 5.0].map((acres) => (
                    <button
                      key={acres}
                      type="button"
                      onClick={() => setPersonData({ ...personData, land_holding_acres: acres })}
                      className={`tap-target p-2 rounded-lg border font-bold text-xs sm:text-sm ${
                        personData.land_holding_acres === acres
                          ? "bg-[#0D5C3A] text-white"
                          : "bg-white text-slate-800 border-slate-200"
                      }`}
                    >
                      {acres} ஏக்கர்
                    </button>
                  ))}
                </div>
                <input
                  type="number"
                  step="0.1"
                  value={personData.land_holding_acres}
                  onChange={(e) => setPersonData({ ...personData, land_holding_acres: Number(e.target.value) })}
                  className="tap-target w-full p-3 bg-white border-2 border-slate-300 rounded-xl text-base text-slate-900"
                  min="0"
                />
              </div>

              <div>
                <label className="block text-sm font-bold text-slate-900 mb-2">
                  முக்கிய பயிர் (Primary Crop):
                </label>
                <div className="grid grid-cols-2 gap-2">
                  {[
                    { id: "paddy", label: "🌾 நெல் (Paddy)" },
                    { id: "millets", label: "🌽 சிறுதானியங்கள் (Millets)" },
                    { id: "sugarcane", label: "🎋 கரும்பு (Sugarcane)" },
                    { id: "cotton", label: "☁️ பருத்தி (Cotton)" },
                  ].map((c) => (
                    <button
                      key={c.id}
                      type="button"
                      onClick={() => setPersonData({ ...personData, crop_type: c.id })}
                      className={`tap-target p-3 rounded-xl border-2 font-bold text-xs sm:text-sm text-left ${
                        personData.crop_type === c.id
                          ? "border-[#0D5C3A] bg-emerald-50 text-[#0D5C3A]"
                          : "border-slate-200 bg-white text-slate-800"
                      }`}
                    >
                      {c.label}
                    </button>
                  ))}
                </div>
              </div>
            </div>
          )}

          {/* Caste Category Step */}
          {((step === 7 && personData.occupation !== "farmer") || (step === 8 && personData.occupation === "farmer")) && (
            <div className="space-y-4">
              <label className="block text-sm font-bold text-slate-900 mb-2">
                சமூகப் பிரிவு (Community Category):
              </label>
              <div className="grid grid-cols-2 gap-2.5">
                {[
                  { id: "BC", label: "BC (பிற்படுத்தப்பட்டோர்)" },
                  { id: "MBC", label: "MBC (மிகவும் பிற்படுத்தப்பட்டோர்)" },
                  { id: "DNC", label: "DNC (சீர்மரபினர்)" },
                  { id: "SC", label: "SC (பட்டியலினத்தவர்)" },
                  { id: "ST", label: "ST (பழங்குடியினர்)" },
                  { id: "General", label: "General (பொதுப்பிரிவு / OC)" },
                ].map((caste) => (
                  <button
                    key={caste.id}
                    type="button"
                    onClick={() => setPersonData({ ...personData, caste_category: caste.id })}
                    className={`tap-target p-3.5 rounded-xl border-2 font-bold text-xs sm:text-sm text-left ${
                      personData.caste_category === caste.id
                        ? "border-[#0D5C3A] bg-emerald-50 text-[#0D5C3A]"
                        : "border-slate-200 bg-white text-slate-800"
                    }`}
                  >
                    {caste.label}
                  </button>
                ))}
              </div>
            </div>
          )}

          {/* Disability & Special Flags Step */}
          {((step === 8 && personData.occupation !== "farmer") || (step === 9 && personData.occupation === "farmer")) && (
            <div className="space-y-5">
              <div>
                <label className="block text-sm font-bold text-slate-900 mb-2">
                  மாற்றுத்திறனாளி நிலை (Disability Status):
                </label>
                <div className="grid grid-cols-2 gap-2">
                  <button
                    type="button"
                    onClick={() => setPersonData({ ...personData, disability_status: false })}
                    className={`tap-target p-3.5 rounded-xl border-2 font-bold text-sm ${
                      !personData.disability_status
                        ? "border-[#0D5C3A] bg-emerald-50 text-[#0D5C3A]"
                        : "border-slate-200 bg-white text-slate-800"
                    }`}
                  >
                    இல்லை (No)
                  </button>
                  <button
                    type="button"
                    onClick={() => setPersonData({ ...personData, disability_status: true })}
                    className={`tap-target p-3.5 rounded-xl border-2 font-bold text-sm ${
                      personData.disability_status
                        ? "border-[#0D5C3A] bg-emerald-50 text-[#0D5C3A]"
                        : "border-slate-200 bg-white text-slate-800"
                    }`}
                  >
                    ♿ ஆம் (Yes)
                  </button>
                </div>
              </div>

              <div>
                <label className="block text-sm font-bold text-slate-900 mb-2">
                  பொருந்தும் சிறப்பு பிரிவுகள் (ஏதேனும் இருப்பின் தேர்வு செய்யவும்):
                </label>
                <div className="grid grid-cols-1 sm:grid-cols-2 gap-2">
                  {[
                    { id: "destitute", label: "ஆதரவற்ற நிலை (Destitute)" },
                    { id: "registered_construction_worker", label: "கட்டுமான நலவாரிய உறுப்பினர்" },
                    { id: "folk_artist", label: "நாட்டுப்புறக் கலைஞர்" },
                    { id: "orphan", label: "பெற்றோரை இழந்தவர் (Orphan)" },
                    { id: "ex_serviceman", label: "முன்னாள் ராணுவத்தினர்" },
                  ].map((flag) => {
                    const active = personData.special_flags.includes(flag.id);
                    return (
                      <button
                        key={flag.id}
                        type="button"
                        onClick={() => toggleSpecialFlag(flag.id)}
                        className={`tap-target p-3 rounded-xl border-2 text-left text-xs sm:text-sm font-semibold transition-all ${
                          active
                            ? "border-[#0D5C3A] bg-emerald-50 text-[#0D5C3A]"
                            : "border-slate-200 bg-white text-slate-800"
                        }`}
                      >
                        <span className="mr-1.5">{active ? "☑️" : "⬜"}</span>
                        <span>{flag.label}</span>
                      </button>
                    );
                  })}
                </div>
              </div>
            </div>
          )}

          {/* FINAL REVIEW STEP */}
          {step > totalSteps && (
            <div className="space-y-4">
              <div className="bg-emerald-50 border border-emerald-300 rounded-xl p-4">
                <h3 className="font-bold text-emerald-950 text-base mb-2">
                  📋 பதிவு செய்யப்பட்ட விவரங்களின் சுருக்கம்:
                </h3>
                <ul className="text-xs sm:text-sm text-slate-800 space-y-1">
                  <li>• <strong>பெயர்:</strong> {personData.name || "பயனாளர்"} ({personData.age} வயது, {personData.gender === "female" ? "பெண்" : "ஆண்"})</li>
                  <li>• <strong>இருப்பிடம்:</strong> {familyData.taluk}, {familyData.district}</li>
                  <li>• <strong>ரேஷன் அட்டை:</strong> {familyData.ration_card_type}</li>
                  <li>• <strong>மாத வருமானம்:</strong> ₹{familyData.total_household_income.toLocaleString("en-IN")}</li>
                  <li>• <strong>தொழில்:</strong> {personData.occupation}</li>
                  <li>• <strong>சமூகப் பிரிவு:</strong> {personData.caste_category}</li>
                </ul>
              </div>

              {errorMessage && (
                <div className="bg-red-50 border border-red-300 text-red-800 p-3 rounded-xl text-xs font-semibold">
                  ⚠️ {errorMessage}
                </div>
              )}
            </div>
          )}
        </div>

        {/* Navigation Buttons */}
        <div className="flex items-center justify-between gap-3">
          {step > 1 && (
            <button
              type="button"
              onClick={() => setStep((s) => s - 1)}
              className="tap-target px-5 py-3 bg-slate-200 hover:bg-slate-300 text-slate-800 font-bold rounded-xl transition-all"
            >
              ← முந்தையது
            </button>
          )}

          {step <= totalSteps ? (
            <button
              type="button"
              onClick={() => setStep((s) => s + 1)}
              className="tap-target ml-auto px-6 py-3 bg-[#0D5C3A] hover:bg-[#083B25] text-white font-bold rounded-xl shadow transition-all flex items-center space-x-2"
            >
              <span>அடுத்த கேள்வி</span>
              <span>→</span>
            </button>
          ) : (
            <button
              type="button"
              disabled={isSubmitting}
              onClick={handleSubmit}
              className="tap-target ml-auto px-7 py-3 bg-[#0D5C3A] hover:bg-[#083B25] disabled:bg-slate-400 text-white font-bold rounded-xl shadow-lg transition-all flex items-center space-x-2"
            >
              <span>{isSubmitting ? "மதிப்பீடு செய்கிறது..." : "🎉 தகுதியை சரிபார்க்கவும்"}</span>
            </button>
          )}
        </div>
      </main>
    </div>
  );
}

export default function IntakePage() {
  return (
    <Suspense
      fallback={
        <div className="min-h-screen flex items-center justify-center font-bold text-slate-700">
          படிவம் ஏற்றப்படுகிறது...
        </div>
      }
    >
      <IntakeContent />
    </Suspense>
  );
}

