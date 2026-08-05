import type { Metadata } from 'next';
import './globals.css';

export const metadata: Metadata = {
  title: 'DEVUP AI Chatbot Starter',
  description: 'Official DEVUP AI Chatbot starter kit built with Next.js and Vercel AI SDK',
};

export default function RootLayout({
  children,
}: {
  children: React.ReactNode;
}) {
  return (
    <html lang="en">
      <body>{children}</body>
    </html>
  );
}
