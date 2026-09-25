"use client";

import Link from "next/link";
import { useState } from "react";
import { speakTamil, stopSpeaking } from "@/lib/audio";

export default function Header() {
  const [isPlaying, setIsPlaying] = useState(false);

  const handleGlobalVoiceHelp = () => {
    if (isPlaying) {
      stopSpeaking();
      setIsPlaying(false);
      return;
    }
    setIsPlaying(true);
    speakTamil(
      "வணக்கம்! உரிமை AI தளத்திற்கு உங்களை வரவேற்கிறோம். தங்களுக்குரிய தமிழ்நாடு அரசு நலத்திட்டங்களை எளிதாக கண்டறியவும், தேவையான ஆவணங்களை தெரிந்துகொள்ளவும் இந்த தளம் உதவுகிறது.",
      () => setIsPlaying(false)
    );
  };

  return (
    <header className="bg-[#0D5C3A] text-white shadow-md no-print border-b-2 border-[#083B25]">
      <div className="max-w-5xl mx-auto px-4 py-3 sm:py-4 flex items-center justify-between">
        {/* Brand & Gov Counter Identity */}
        <Link href="/" className="flex items-center space-x-3 group">
          <div className="w-10 h-10 sm:w-12 sm:h-12 rounded-full bg-white text-[#0D5C3A] flex items-center justify-center font-bold text-xl sm:text-2xl shadow-inner border-2 border-emerald-200">
            🏛️
          </div>
          <div>
            <div className="flex items-center space-x-2">
              <span className="font-bold text-lg sm:text-2xl tracking-wide">
                உரிமை AI
              </span>
              <span className="text-xs bg-emerald-800 text-emerald-100 px-2 py-0.5 rounded font-mono hidden sm:inline-block">
                URIMAI AI
              </span>
            </div>
            <p className="text-xs sm:text-sm text-emerald-100 font-medium">
              தமிழ்நாடு அரசு நலத்திட்ட வழிகாட்டி
            </p>
          </div>
        </Link>

        {/* Action controls */}
        <div className="flex items-center space-x-2 sm:space-x-3">
          {/* Audio Assistance Button */}
          <button
            onClick={handleGlobalVoiceHelp}
            className={`tap-target px-3 py-2 rounded-lg font-semibold text-xs sm:text-sm transition-all flex items-center space-x-2 border ${
              isPlaying
                ? "bg-amber-400 text-slate-900 border-amber-300 animate-pulse"
                : "bg-emerald-800/80 hover:bg-emerald-700 text-white border-emerald-600"
            }`}
            title="குரல் வழிகாட்டல் (Voice Guide)"
            aria-label="குரல் வழிகாட்டல் (Voice Guide)"
          >
            <span>{isPlaying ? "⏹️" : "🔊"}</span>
            <span className="hidden xs:inline">
              {isPlaying ? "நிறுத்து" : "ஒலி உதவி"}
            </span>
          </button>

          {/* Scheme Catalog Link */}
          <Link
            href="/schemes"
            className="tap-target px-3 py-2 rounded-lg bg-white/10 hover:bg-white/20 text-white text-xs sm:text-sm font-semibold border border-white/20 flex items-center space-x-1"
          >
            <span>📋</span>
            <span className="hidden sm:inline">திட்டங்கள்</span>
          </Link>

          {/* Application Tracker Link */}
          <Link
            href="/tracker"
            className="tap-target px-3 py-2 rounded-lg bg-white/10 hover:bg-white/20 text-white text-xs sm:text-sm font-semibold border border-white/20 flex items-center space-x-1"
          >
            <span>🔍</span>
            <span className="hidden sm:inline">நிலை அறிதல்</span>
          </Link>

          {/* Login / Account Link */}
          <Link
            href="/login"
            className="tap-target px-3 py-2 rounded-lg bg-emerald-950/80 hover:bg-emerald-950 text-white text-xs sm:text-sm font-semibold border border-emerald-700 flex items-center space-x-1"
          >
            <span>👤</span>
            <span className="hidden sm:inline">உள்நுழைவு</span>
          </Link>
        </div>
      </div>
    </header>
  );
}

