import axios from 'axios';
import { useAuthStore } from '@/stores';
import type { Ref } from "vue";
import type { ListScansResponse, Scan } from "@/api/scanning/Scan";

const LIST_SCANS_URl = `${import.meta.env.VITE_BASE_URL}/scanning/list`;

async function listScans(scans: Ref<Scan[]>) {
  const store = useAuthStore();
  const config = {
    headers: {
      "X-ACCESS-TOKEN": store.getAccessToken,
      "Authorization": `Bearer ${store.getIdToken}`,
    }
  };
  const response = await axios.get(LIST_SCANS_URl, config);
  const data: ListScansResponse = response.data;
  scans.value = data.scans;
}

export function useScanning() {
  return {
    listScans: (scans: Ref<Scan[]>) => listScans(scans)
  };
}
