import type { Metadata } from "next";
import { Inter } from "next/font/google";
import { usePathname } from "next/navigation";
import Link from "next/link"
import "./globals.css";

const inter = Inter({ subsets: ["latin"] });

export const metadata: Metadata = {
  title: "Finance Tracker",
  description: "Generated by create next app",
};

export function Links() {
  const pathname = usePathname()

  return (
    <nav>
      <Link className={`link ${pathname === '/' ? 'active' : ''}`} href="/">
        Home
      </Link>
      <Link className={`link ${pathname === '/tutorial' ? 'active' : ''}`} href="/tutorial">
        Tutorial
      </Link>
    </nav>
  )
}

export default function RootLayout({
  children,
}: Readonly<{
  children: React.ReactNode;
}>) {
  return (
    <html lang="en">
      <body className={inter.className}>
        {children}
      </body>
    </html>
  );
}
