#!/usr/bin/env python3
import os
import json
from datetime import datetime
import google.generativeai as genai

genai.configure(api_key=os.getenv('GEMINI_API_KEY'))
model = genai.GenerativeModel('gemini-pro')

# Sample articles
articles = [
    {"title": "Power Platform AI Update", "desc": "New Copilot in Power Apps"},
    {"title": "SharePoint Search AI", "desc": "Semantic search released"},
    {"title": "Azure Gov Cloud", "desc": "New AI services for government"}
]

# Analyze with Gemini
prompt = f"""Rank these articles by developer importance (1-10):
{json.dumps(articles)}
Return as JSON array with: title, score, why_matters"""

response = model.generate_content(prompt)
print(response.text)

# Save results
results = {
    "date": datetime.now().isoformat(),
    "analysis": response.text
}

with open("curated_research.json", "w") as f:
    json.dump(results, f, indent=2)

print("✅ Done! Results saved to curated_research.json")