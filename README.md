# AI Job Automation System

Daily job collection, dedupe, Claude fit-scoring and Google Sheet tracking, built on n8n.

## Flow
1. Schedule (9 AM) -> Fetch Jobs (job API URL)
2. Split + normalize fields (title, company, location, url)
3. Filter invalid, remove jobs already seen
4. Claude Job Match -> `score | reason`
5. Append to Google Sheet "AI Job Tracker" (tab: Jobs)
6. Gmail digest -> you approve by writing `Yes` in the `approval` column

## Sheet headers
found_on, job_title, company, location, job_url, posted_on, status, match_score, approval

## Files
- `n8n/ai-job-automation.json` - import in n8n (Workflows > Import from file)
- `scripts/match_jobs.py` - offline resume vs job-description keyword matcher
- `data/resume_skills.txt` - one skill per line (edit with your verified skills only)

## Setup
1. Import the workflow JSON in n8n.
2. Connect Google Sheets, Gmail, Anthropic credentials.
3. Set the job API URL in "Fetch Jobs" and your email in "Email Daily Digest".
4. Activate the workflow.

Never commit API keys. Keep credentials inside n8n.
