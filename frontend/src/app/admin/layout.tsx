"use client";

import { useEffect, useState } from "react";
import Link from "next/link";
import { usePathname, useRouter } from "next/navigation";

export default function AdminLayout({ children }: { children: React.ReactNode }) {
  const pathname = usePathname();
  const router = useRouter();
  const [adminUser, setAdminUser] = useState<{ email: string; name: string } | null>(null);

  useEffect(() => {
    // Only check auth for admin sub-pages (not login)
    if (pathname === "/admin/login") return;

    const token = localStorage.getItem("urimai_token");
    const role = localStorage.getItem("urimai_role");
    const email = localStorage.getItem("urimai_email");
    const name = localStorage.getItem("urimai_name");

    if (!token || role !== "admin") {
      router.push("/admin/login");
    } else {
      setAdminUser({
        email: email || "admin@urimai.tn.gov.in",
        name: name || "TN Welfare Administrator",
      });
    }
  }, [pathname, router]);

  const handleLogout = () => {
    localStorage.removeItem("urimai_token");
    localStorage.removeItem("urimai_role");
    localStorage.removeItem("urimai_email");
    localStorage.removeItem("urimai_name");
    router.push("/admin/login");
  };

  if (pathname === "/admin/login") {
    return <>{children}</>;
  }

  const navItems = [
    { href: "/admin", label: "📊 Overview Stats" },
    { href: "/admin/review-queue", label: "🕒 Freshness Queue" },
    { href: "/admin/applications", label: "⏳ Stuck Applications" },
    { href: "/admin/rules", label: "⚖️ Rule Editor" },
    { href: "/admin/logs", label: "🚨 Error Logs" },
    { href: "/admin/audit", label: "📜 Audit Trail" },
  ];

  return (
    <div className="min-h-screen bg-slate-900 text-slate-100 flex flex-col font-sans">
      {/* Admin Top Navigation */}
      <header className="bg-slate-950 border-b border-slate-800 px-6 py-3 flex items-center justify-between">
        <div className="flex items-center gap-3">
          <div className="bg-emerald-600 text-white font-black text-lg px-2.5 py-1 rounded">
            🏛️ URIMAI ADMIN
          </div>
          <span className="text-xs text-slate-400 border-l border-slate-700 pl-3">
            Tamil Nadu State Welfare Scheme Operations Control
          </span>
        </div>

        <div className="flex items-center gap-4 text-xs">
          {adminUser && (
            <div className="text-right">
              <div className="font-semibold text-slate-200">{adminUser.name}</div>
              <div className="text-slate-400">{adminUser.email}</div>
            </div>
          )}
          <button
            onClick={handleLogout}
            className="bg-rose-900/60 hover:bg-rose-800 text-rose-200 px-3 py-1.5 rounded border border-rose-700/50 transition"
          >
            Logout
          </button>
        </div>
      </header>

      {/* Admin Subnav */}
      <nav className="bg-slate-950/70 border-b border-slate-800 px-6 flex gap-1 overflow-x-auto text-sm">
        {navItems.map((item) => {
          const isActive = pathname === item.href;
          return (
            <Link
              key={item.href}
              href={item.href}
              className={`px-4 py-2.5 font-medium border-b-2 transition whitespace-nowrap ${
                isActive
                  ? "border-emerald-500 text-emerald-400 bg-slate-900/80"
                  : "border-transparent text-slate-400 hover:text-slate-200 hover:bg-slate-900/40"
              }`}
            >
              {item.label}
            </Link>
          );
        })}
      </nav>

      {/* Admin Content Area */}
      <main className="flex-1 p-6 max-w-7xl w-full mx-auto">{children}</main>
    </div>
  );
}
