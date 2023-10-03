import axios from 'axios';
import { useAuthStore } from '@/stores';
import type { Ref } from "vue";
import type { ListScansResponse, Scan } from "@/api/scanning/Scan";
import type { ParsedScan } from "./types";

const LIST_SCANS_URl = `${import.meta.env.VITE_BASE_URL}/scanning/list`;

function parseScanResponse(scan: Scan): ParsedScan {
  const jsonStringResponse = scan.serpJsonResponse;
  const jsonResponse = JSON.parse(jsonStringResponse);
  
  const scannedDate = jsonResponse["search_metadata"]["created_at"];
  const visualMatches = jsonResponse["visual_matches"]

  const parsedScan: ParsedScan = {
    ...scan,
    scannedDate,
    visualMatches
  }

  return parsedScan;
}


async function listScans(scans: Ref<ParsedScan[]>) {
  const store = useAuthStore();
  const config = {
    headers: {
      "X-ACCESS-TOKEN": store.getAccessToken,
      "Authorization": `Bearer ${store.getIdToken}`,
    }
  };
  const response = await axios.get(LIST_SCANS_URl, config);
  const data: ListScansResponse = response.data;
  const parsedScans = data.scans.map((scan) => parseScanResponse(scan));
  scans.value = parsedScans;
}

export function useScanning() {
  return {
    listScans: (scans: Ref<ParsedScan[]>) => listScans(scans)
  };
}
