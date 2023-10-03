import type { Scan } from "@/api/scanning/Scan";

type VisualMatchPrice = {
  value: string
  extracted_value: number
  currency: string
}

type VisualMatches = {
  position: number
  title: string
  link: string
  source: string
  source_icon?: string
  rating?: string
  price?: [VisualMatchPrice]
  thumbnail?: string
}

export interface ParsedScan extends Scan {
  scannedDate: string
  visualMatches: [VisualMatches]
}
