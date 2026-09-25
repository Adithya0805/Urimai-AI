// Audio assistance and voice recognition utilities in Tamil (ta-IN)

export function speakTamil(text: string, onEnd?: () => void): boolean {
  if (typeof window === "undefined" || !("speechSynthesis" in window)) {
    return false;
  }

  // Cancel any ongoing speech
  window.speechSynthesis.cancel();

  // Strip markdown formatting for natural speech
  const cleanText = text
    .replace(/[#*`_~]/g, "")
    .replace(/\n+/g, " ")
    .trim();

  const utterance = new SpeechSynthesisUtterance(cleanText);
  utterance.lang = "ta-IN";
  utterance.rate = 0.95; // Slightly slower for crisp clarity
  utterance.pitch = 1.0;

  // Try to find native Tamil voice if available
  const voices = window.speechSynthesis.getVoices();
  const tamilVoice = voices.find(
    (v) => v.lang.startsWith("ta") || v.name.toLowerCase().includes("tamil")
  );
  if (tamilVoice) {
    utterance.voice = tamilVoice;
  }

  if (onEnd) {
    utterance.onend = onEnd;
    utterance.onerror = onEnd;
  }

  window.speechSynthesis.speak(utterance);
  return true;
}

export function stopSpeaking(): void {
  if (typeof window !== "undefined" && "speechSynthesis" in window) {
    window.speechSynthesis.cancel();
  }
}

export function startSpeechRecognition(
  onResult: (text: string) => void,
  onError?: (err: any) => void
): { stop: () => void } | null {
  if (typeof window === "undefined") return null;

  const SpeechRecognition =
    (window as any).SpeechRecognition || (window as any).webkitSpeechRecognition;

  if (!SpeechRecognition) {
    if (onError) onError("குரல் உள்ளீடு இந்த உலாவியில் ஆதரிக்கப்படவில்லை (Speech not supported)");
    return null;
  }

  try {
    const recognition = new SpeechRecognition();
    recognition.lang = "ta-IN";
    recognition.continuous = false;
    recognition.interimResults = false;

    recognition.onresult = (event: any) => {
      if (event.results && event.results[0] && event.results[0][0]) {
        const transcript = event.results[0][0].transcript;
        onResult(transcript);
      }
    };

    recognition.onerror = (event: any) => {
      if (onError) onError(event.error);
    };

    recognition.start();

    return {
      stop: () => {
        try {
          recognition.stop();
        } catch {
          // ignore
        }
      },
    };
  } catch (err) {
    if (onError) onError(err);
    return null;
  }
}
