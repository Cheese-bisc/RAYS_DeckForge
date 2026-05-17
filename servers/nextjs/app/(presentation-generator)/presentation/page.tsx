'use client'
import React from "react";
import PresentationPage from "./components/PresentationPage";
import { Button } from "@/components/ui/button";
import { useRouter, useSearchParams } from "next/navigation";
import "../utils/prism-languages";
const page = () => {

  const router = useRouter();
  const params = useSearchParams();
  const queryId = params.get("id");
  if (!queryId) {
    return (
      <div className="flex flex-col items-center justify-center h-screen" style={{ background: '#000000', fontFamily: "'Space Mono', monospace" }}>
        <h1 className="text-2xl font-bold" style={{ color: '#ffffff' }}>No presentation id found</h1>
        <p className="pb-4" style={{ color: '#888888' }}>Please try again</p>
        <Button onClick={() => router.push("/dashboard")} className="rounded-[10px]" style={{ background: '#ffffff', color: '#000000' }}>Go to home</Button>
      </div>
    );
  }
  return (

    <PresentationPage presentation_id={queryId} />

  );
};
export default page;
