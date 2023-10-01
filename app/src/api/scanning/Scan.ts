export type Scan = {
  image_url: string
  serp_found_title: string
  serp_found_price: number
  serp_json_response?: string
}

export type ListScansResponse = {
  scans: Scan[]
}
