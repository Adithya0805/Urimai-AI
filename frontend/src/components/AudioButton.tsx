"use client";

import { useState } from "react";
import { speakTamil, stopSpeaking } from "@/lib/audio";

interface AudioButtonProps {
  textToSpeak: string;
  label?: string;
  className?: string;
}

export default function AudioButton({
  textToSpeak,
  label = "கேட்க",
  className = "",
}: AudioButtonProps) {
  const [isPlaying, setIsPlaying] = useState(false);

  const toggleSpeech = () => {
    if (isPlaying) {
      stopSpeaking();
      setIsPlaying(false);
    } else {
      setIsPlaying(true);
      speakTamil(textToSpeak, () => setIsPlaying(false));
    }
  };

  return (
    <button
      type="button"
      onClick={toggleSpeech}
      className={`tap-target inline-flex items-center space-x-1.5 px-3 py-1.5 rounded-full text-xs sm:text-sm font-semibold transition-all border ${
        isPlaying
          ? "bg-amber-100 text-amber-900 border-amber-400 animate-pulse"
          : "bg-emerald-50 text-emerald-900 border-emerald-300 hover:bg-emerald-100"
      } ${className}`}
      aria-label={`${label}: ${textToSpeak}`}
      title="குரல் மூலம் கேட்க (Listen to audio)"
    >
      <span className="text-base">{isPlaying ? "⏹️" : "🔊"}</span>
      <span>{isPlaying ? "நிறுத்து" : label}</span>
    </button>
  );
}
