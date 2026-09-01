# Scrape-Verse-Self-Healing
# Self-Healing Scraper: Books to Scrape

This project was built for the Scrape-Verse Hackathon to demonstrate a resilient, self-healing data pipeline using the Bright Data CLI.

## Architecture
Instead of hardcoding a scraper that breaks when a website updates, this pipeline relies on Scraper Studio to autonomously repair itself.
1. **Initial Generation:** Created a Collector ID targeting a bookstore catalog using an AI prompt.
2. **Simulated Breakage:** Intentionally sabotaged the CSS selectors (`.product_pod` to `.broken_product`) in the IDE and deployed to production to simulate a UI update.
3. **Healing Loop:** Utilized the `bdata scraper heal` CLI command to allow the AI to analyze the empty array output, find the correct DOM elements, and deploy a hotfix without manual coding.

## Tech Stack
* Bright Data CLI
* Bright Data Scraper Studio
