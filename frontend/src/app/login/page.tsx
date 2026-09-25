"use client";

import { useState } from "react";
import { useRouter } from "next/navigation";
import Link from "next/link";
import Header from "@/components/Header";
import AudioButton from "@/components/AudioButton";
import { api } from "@/lib/api";

export default function LoginPage() {
  const router = useRouter();
  const [phone, setPhone] = useState("");
  const [otp, setOtp] = useState("");
  const [otpSent, setOtpSent] = useState(false);
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState<string | null>(null);

  const handleSendOtp = async (e: React.FormEvent) => {
    e.preventDefault();
    if (!phone.trim()) return;

    setLoading(true);
    setError(null);

    try {
      await api.sendOtp(phone);
      setOtpSent(true);
    } catch (err: any) {
      setError(err.message || "OTP அனுப்புவதில் பிழை ஏற்பட்டது.");
    } finally {
      setLoading(false);
    }
  };

  const handleVerifyOtp = async (e: React.FormEvent) => {
    e.preventDefault();
    if (!otp.trim()) return;

    setLoading(true);
    setError(null);

    try {
      const data = await api.verifyOtp(phone, otp);
      localStorage.setItem("urimai_token", data.access_token);

      // Check if user has an uncompleted intake session to resume
      try {
        const resumeData = await api.resumeIntake();
        if (resumeData && !resumeData.is_completed) {
          router.push("/intake");
          return;
        }
      } catch {
        // no active uncompleted intake, proceed to family check
      }

      // Check if user has existing families
      const meData = await api.getMe();
      if (meData.family_ids && meData.family_ids.length > 0) {
        router.push(`/family/${meData.family_ids[0]}`);
        return;
      }

      router.push("/intake");
    } catch (err: any) {
      setError(err.message || "OTP சரிபார்ப்பதில் பிழை.");
    } finally {
      setLoading(false);
    }
  };


  return (
    <div className="min-h-screen flex flex-col bg-[#FBF9F5]">
      <Header />

      <main className="flex-1 max-w-md w-full mx-auto px-4 py-8 sm:py-12">
        <div className="gov-card p-6 sm:p-8 bg-white border-2 border-emerald-900/20 shadow-md rounded-2xl">
          <div className="text-center mb-6 border-b pb-4">
            <div className="w-14 h-14 rounded-2xl bg-emerald-100 text-emerald-800 flex items-center justify-center text-2xl mx-auto mb-3 shadow-inner">
              📱
            </div>
            <h1 className="text-xl font-bold text-slate-900">
              தொலைபேசி எண் மூலம் உள்நுழைவு
            </h1>
            <p className="text-xs text-slate-600 mt-1">
              (Phone OTP Login & Secure Session)
            </p>

            <div className="mt-3 flex justify-center">
              <AudioButton
                textToSpeak="தங்களின் 10 இலக்க தொலைபேசி எண்ணை உள்ளிட்டு கடவுச்சொல் பெற்று உள்நுழையவும்."
                label="கேட்க"
              />
            </div>
          </div>

          {error && (
            <div className="bg-red-50 border border-red-300 text-red-800 p-3 rounded-xl text-xs font-semibold mb-4">
              ⚠️ {error}
            </div>
          )}

          {!otpSent ? (
            <form onSubmit={handleSendOtp} className="space-y-4">
              <div>
                <label className="block text-xs font-bold text-slate-800 mb-1.5">
                  தொலைபேசி எண் (Mobile Number):
                </label>
                <div className="flex">
                  <span className="inline-flex items-center px-3 bg-slate-100 border-2 border-r-0 border-slate-300 rounded-l-xl text-sm font-bold text-slate-700">
                    +91
                  </span>
                  <input
                    type="tel"
                    required
                    maxLength={10}
                    value={phone}
                    onChange={(e) => setPhone(e.target.value.replace(/\D/g, ""))}
                    placeholder="98765 43210"
                    className="tap-target flex-1 p-3.5 border-2 border-slate-300 rounded-r-xl text-base font-bold text-slate-900"
                  />
                </div>
              </div>

              <button
                type="submit"
                disabled={loading || phone.length < 10}
                className="tap-target w-full py-3.5 bg-[#0D5C3A] hover:bg-[#083B25] disabled:bg-slate-300 text-white font-bold rounded-xl shadow transition-all text-sm"
              >
                {loading ? "அனுப்புகிறது..." : "கடவுச்சொல் பெற (Send OTP)"}
              </button>
            </form>
          ) : (
            <form onSubmit={handleVerifyOtp} className="space-y-4">
              <div className="bg-emerald-50 p-3 rounded-xl border border-emerald-200 text-xs text-emerald-900">
                ✓ <strong>+91 {phone}</strong> எண்ணிற்கு கடவுச்சொல் அனுப்பப்பட்டது. (சோதனை OTP: <strong>123456</strong>)
              </div>

              <div>
                <label className="block text-xs font-bold text-slate-800 mb-1.5">
                  6 இலக்க கடவுச்சொல் (Enter 6-digit OTP):
                </label>
                <input
                  type="text"
                  required
                  maxLength={6}
                  value={otp}
                  onChange={(e) => setOtp(e.target.value)}
                  placeholder="123456"
                  className="tap-target w-full p-3.5 border-2 border-slate-300 rounded-xl text-center text-xl font-mono font-bold tracking-widest text-slate-900"
                />
              </div>

              <button
                type="submit"
                disabled={loading || otp.length < 6}
                className="tap-target w-full py-3.5 bg-[#0D5C3A] hover:bg-[#083B25] disabled:bg-slate-300 text-white font-bold rounded-xl shadow transition-all text-sm"
              >
                {loading ? "சரிபார்க்கிறது..." : "உள்நுழையவும் (Verify & Login)"}
              </button>

              <div className="text-center pt-2">
                <button
                  type="button"
                  onClick={() => setOtpSent(false)}
                  className="text-xs text-emerald-800 font-bold hover:underline"
                >
                  எண்ணை மாற்ற வேண்டுமா? (Change Number)
                </button>
              </div>
            </form>
          )}
        </div>
      </main>
    </div>
  );
}
