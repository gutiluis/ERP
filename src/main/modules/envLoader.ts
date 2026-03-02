// src/main/modules/envLoader.ts
import { config } from 'dotenv'
import { resolve } from 'path'
import { existsSync } from 'fs'

export function loadEnv() {
  // Determine mode: production, development, or fallback
  const mode = process.env.NODE_ENV || 'development'

  // Build env file path
  const envFile = resolve(process.cwd(), `.env.${mode}`)

  // Optional: fallback to default .env if specific file doesn't exist
  const fileToLoad = existsSync(envFile)
    ? envFile
    : resolve(process.cwd(), '.env')

  const result = config({ path: fileToLoad })

  if (result.error) {
    console.warn(`Failed to load env file at ${fileToLoad}`)
  } else {
    console.log(`Loaded environment variables from ${fileToLoad}`)
  }
}