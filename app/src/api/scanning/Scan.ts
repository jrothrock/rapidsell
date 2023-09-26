export type Scan = {
  image_url: string
  serp_found_title: string
}

export type ListScansResponse = {
  scans: Scan[]
}
