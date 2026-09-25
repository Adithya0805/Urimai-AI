import type { Metadata } from "next";
import { Noto_Sans_Tamil } from "next/font/google";
import "./globals.css";

const notoSansTamil = Noto_Sans_Tamil({
  weight: ["400", "500", "600", "700"],
  subsets: ["tamil", "latin"],
  display: "swap",
  variable: "--font-noto-tamil",
});

export const metadata: Metadata = {
  title: "உரிமை AI — தமிழ்நாடு அரசு நலத்திட்ட வழிகாட்டி (Urimai AI)",
  description: "தமிழ்நாடு அரசு நலத்திட்டங்களுக்கான ஒற்றைச் சாளர தகுதி அறிதல் மற்றும் வழிகாட்டி தளம்.",
};

export default function RootLayout({
  children,
}: {
  children: React.ReactNode;
}) {
  return (
    <html lang="ta" className={`${notoSansTamil.variable} h-full`}>
      <body className="min-h-full flex flex-col font-sans bg-[#FBF9F5] text-[#1A202C]">
        {children}
      </body>
    </html>
  );
}
