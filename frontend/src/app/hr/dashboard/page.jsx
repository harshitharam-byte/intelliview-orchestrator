"use client";

import { ErrorBoundary } from "@/components/ErrorBoundary";

export default function Page() {
  return (
    <ErrorBoundary>
      <div className="p-8">
        <h1 className="text-2xl font-bold">HR Dashboard</h1>
        <p className="mt-2">
          HR Dashboard module is currently unavailable.
        </p>
      </div>
    </ErrorBoundary>
  );
}