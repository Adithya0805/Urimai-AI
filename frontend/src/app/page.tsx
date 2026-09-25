"use client";

import Link from "next/link";
import Header from "@/components/Header";
import AudioButton from "@/components/AudioButton";

export default function HomePage() {
  const introAudioText =
    "வணக்கம்! உரிமை AI தளத்திற்கு வரவேற்கிறோம். தங்களுக்கு அல்லது தங்கள் குடும்பத்திற்குரிய தமிழ்நாடு அரசு நலத்திட்டங்களை கண்டறிய கீழே உள்ள பொத்தான்களில் ஒன்றைத் தேர்வு செய்யவும்.";

  return (
    <div className="min-h-screen flex flex-col bg-[#FBF9F5]">
      <Header />

      <main className="flex-1 max-w-4xl w-full mx-auto px-4 py-6 sm:py-10">
        {/* Welcome Callout */}
        <div className="gov-card p-6 sm:p-8 bg-gradient-to-br from-emerald-900 to-[#0D5C3A] text-white mb-8 relative overflow-hidden shadow-md">
          <div className="relative z-10">
            <div className="inline-flex items-center space-x-2 bg-emerald-800/80 px-3 py-1 rounded-full text-xs font-semibold text-emerald-200 mb-3 border border-emerald-600/50">
              <span>🏛️</span>
              <span>தமிழ்நாடு அரசு மக்கள் நல சேவை</span>
            </div>

            <h1 className="text-2xl sm:text-4xl font-extrabold tracking-tight mb-2 leading-tight">
              உங்களுக்குரிய அரசு நலத்திட்டங்களை உடனடியாக அறியுங்கள்
            </h1>

            <p className="text-emerald-100 text-sm sm:text-base max-w-2xl mb-4 leading-relaxed">
              முதியோர் ஓய்வூதியம், மகளிர் உரிமைத் தொகை, கல்வி உதவித்தொகை, விவசாய மானியங்கள் மற்றும் நலவாரிய உதவிகளுக்கான தகுதி வழிகாட்டி.
            </p>

            <div className="flex items-center space-x-3">
              <AudioButton
                textToSpeak={introAudioText}
                label="விளக்கத்தை தமிழில் கேட்க"
                className="bg-amber-400 text-slate-900 border-amber-300 font-bold hover:bg-amber-300"
              />
            </div>
          </div>

          {/* Decorative background element */}
          <div className="absolute -right-10 -bottom-10 w-48 h-48 bg-white/5 rounded-full blur-2xl pointer-events-none" />
        </div>

        {/* Primary Action Choices (Large touch targets) */}
        <div className="grid grid-cols-1 sm:grid-cols-2 gap-4 sm:gap-6 mb-10">
          {/* Choice 1: Individual Eligibility */}
          <Link
            href="/intake?mode=individual"
            className="gov-card p-6 hover:border-[#0D5C3A] hover:shadow-md transition-all group flex flex-col justify-between border-2 border-slate-200"
          >
            <div>
              <div className="w-14 h-14 rounded-2xl bg-emerald-100 text-emerald-800 flex items-center justify-center text-3xl mb-4 group-hover:scale-105 transition-transform shadow-inner">
                👤
              </div>
              <h2 className="text-xl font-bold text-slate-900 mb-2 group-hover:text-[#0D5C3A]">
                என் தகுதியை அறிய
              </h2>
              <p className="text-slate-600 text-sm leading-relaxed mb-4">
                தங்களின் வயது, தொழில் மற்றும் நிலையை குறிப்பிட்டு தங்களுக்குரிய அரசு உதவிகளை உடனே தெரிந்துகொள்ளுங்கள்.
              </p>
            </div>
            <div className="tap-target w-full bg-[#0D5C3A] group-hover:bg-[#083B25] text-white font-bold rounded-xl text-center text-sm shadow transition-colors flex items-center justify-center space-x-2">
              <span>தொடங்கவும் (Start)</span>
              <span>→</span>
            </div>
          </Link>

          {/* Choice 2: Family Eligibility */}
          <Link
            href="/intake?mode=family"
            className="gov-card p-6 hover:border-[#0D5C3A] hover:shadow-md transition-all group flex flex-col justify-between border-2 border-slate-200"
          >
            <div>
              <div className="w-14 h-14 rounded-2xl bg-amber-100 text-amber-800 flex items-center justify-center text-3xl mb-4 group-hover:scale-105 transition-transform shadow-inner">
                👨‍👩‍👧‍👦
              </div>
              <h2 className="text-xl font-bold text-slate-900 mb-2 group-hover:text-[#0D5C3A]">
                முழுக் குடும்பத்தின் தகுதி
              </h2>
              <p className="text-slate-600 text-sm leading-relaxed mb-4">
                குடும்ப அட்டை விவரங்களுடன் அனைத்து உறுப்பினர்களுக்கும் (பெற்றோர், குழந்தைகள்) கிடைக்கும் உதவிகளை ஒரே நேரத்தில் கணக்கிடலாம்.
              </p>
            </div>
            <div className="tap-target w-full bg-[#0D5C3A] group-hover:bg-[#083B25] text-white font-bold rounded-xl text-center text-sm shadow transition-colors flex items-center justify-center space-x-2">
              <span>குடும்பமாக தொடங்கவும்</span>
              <span>→</span>
            </div>
          </Link>

          {/* Choice 3: Scheme Catalog */}
          <Link
            href="/schemes"
            className="gov-card p-6 hover:border-slate-400 hover:shadow-md transition-all group flex flex-col justify-between"
          >
            <div>
              <div className="w-14 h-14 rounded-2xl bg-blue-100 text-blue-800 flex items-center justify-center text-3xl mb-4 shadow-inner">
                📋
              </div>
              <h2 className="text-lg font-bold text-slate-900 mb-2">
                அனைத்து அரசு திட்டங்கள்
              </h2>
              <p className="text-slate-600 text-sm leading-relaxed mb-4">
                சமூக நலம், கல்வி, வேளாண்மை மற்றும் தொழிலாளர் நலத்துறை திட்டங்களின் அதிகாரப்பூர்வ பட்டியலை நேரடியாகப் பார்வையிடுங்கள்.
              </p>
            </div>
            <div className="tap-target w-full bg-slate-100 group-hover:bg-slate-200 text-slate-800 font-bold rounded-xl text-center text-sm transition-colors flex items-center justify-center space-x-1 border border-slate-300">
              <span>பட்டியலை பார்க்க</span>
              <span>→</span>
            </div>
          </Link>

          {/* Choice 4: Application Tracker */}
          <Link
            href="/tracker"
            className="gov-card p-6 hover:border-slate-400 hover:shadow-md transition-all group flex flex-col justify-between"
          >
            <div>
              <div className="w-14 h-14 rounded-2xl bg-purple-100 text-purple-800 flex items-center justify-center text-3xl mb-4 shadow-inner">
                🔍
              </div>
              <h2 className="text-lg font-bold text-slate-900 mb-2">
                விண்ணப்ப நிலை அறிதல்
              </h2>
              <p className="text-slate-600 text-sm leading-relaxed mb-4">
                ஏற்கனவே விண்ணப்பித்த திட்டங்களின் நிலை, நிலுவையில் உள்ள ஆவணங்கள் மற்றும் புதுப்பித்தல் காலத்தை அறியலாம்.
              </p>
            </div>
            <div className="tap-target w-full bg-slate-100 group-hover:bg-slate-200 text-slate-800 font-bold rounded-xl text-center text-sm transition-colors flex items-center justify-center space-x-1 border border-slate-300">
              <span>நிலையை சரிபார்க்க</span>
              <span>→</span>
            </div>
          </Link>
        </div>

        {/* 4 Core Department Seals */}
        <div className="bg-white rounded-2xl p-6 border border-slate-200 mb-8">
          <h3 className="font-bold text-base text-slate-900 mb-4 flex items-center space-x-2">
            <span>🏛️</span>
            <span>இணைக்கப்பட்டுள்ள அரசுத் துறைகள்:</span>
          </h3>
          <div className="grid grid-cols-2 sm:grid-cols-4 gap-3 text-center">
            <div className="p-3 bg-slate-50 rounded-xl border border-slate-200">
              <span className="text-2xl block mb-1">👩‍👧</span>
              <span className="text-xs font-bold text-slate-800 block">சமூக நலம் & மகளிர் உரிமை</span>
            </div>
            <div className="p-3 bg-slate-50 rounded-xl border border-slate-200">
              <span className="text-2xl block mb-1">🎓</span>
              <span className="text-xs font-bold text-slate-800 block">பள்ளி & உயர்கல்வித் துறை</span>
            </div>
            <div className="p-3 bg-slate-50 rounded-xl border border-slate-200">
              <span className="text-2xl block mb-1">🌾</span>
              <span className="text-xs font-bold text-slate-800 block">வேளாண்மை & உழவர் நலத்துறை</span>
            </div>
            <div className="p-3 bg-slate-50 rounded-xl border border-slate-200">
              <span className="text-2xl block mb-1">👷</span>
              <span className="text-xs font-bold text-slate-800 block">தொழிலாளர் நல வாரியங்கள்</span>
            </div>
          </div>
        </div>
      </main>

      {/* Trust Footer */}
      <footer className="bg-slate-900 text-slate-400 text-xs py-6 border-t border-slate-800 no-print text-center px-4">
        <div className="max-w-4xl mx-auto space-y-2">
          <p className="text-slate-300 font-medium">
            உரிமை AI — தமிழ்நாடு அரசு நலத்திட்ட தகவல் வழிகாட்டி மையம்
          </p>
          <p>
            அனைத்து தகவல்களும் தமிழ்நாடு அரசின் அதிகாரப்பூர்வ அரசாணைகள் மற்றும் தளங்களின் அடிப்படையில் சரிபார்க்கப்பட்டவை.
          </p>
        </div>
      </footer>
    </div>
  );
}
