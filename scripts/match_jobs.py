#!/usr/bin/env python3
"""Offline resume-vs-job matcher.

Usage:
    python match_jobs.py data/resume_skills.txt jobs.csv > ranked.csv

jobs.csv needs columns: job_title, company, location, job_url, description
Output adds: score (0-100) and matched_skills.
"""
import csv
import re
import sys


def load_skills(path):
    with open(path, encoding="utf-8") as f:
        return [s.strip().lower() for s in f if s.strip()]


def score_job(skills, text):
    text = text.lower()
    hits = [s for s in skills if re.search(r"\b" + re.escape(s) + r"\b", text)]
    pct = round(100 * len(hits) / len(skills)) if skills else 0
    return pct, hits


def main():
    if len(sys.argv) != 3:
        sys.exit(__doc__)
    skills = load_skills(sys.argv[1])
    with open(sys.argv[2], newline="", encoding="utf-8") as f:
        rows = list(csv.DictReader(f))
    for r in rows:
        text = f"{r.get('job_title', '')} {r.get('description', '')}"
        r["score"], hits = score_job(skills, text)
        r["matched_skills"] = ", ".join(hits)
    rows.sort(key=lambda r: r["score"], reverse=True)
    if not rows:
        return
    w = csv.DictWriter(sys.stdout, fieldnames=list(rows[0].keys()))
    w.writeheader()
    w.writerows(rows)


if __name__ == "__main__":
    main()
