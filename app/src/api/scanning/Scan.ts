export type Scan = {
  imageUrl: string
  serpFoundTitle: string
  serpFoundPrice: number
  serpJsonResponse: string
}

export type ListScansResponse = {
  scans: Scan[]
}
