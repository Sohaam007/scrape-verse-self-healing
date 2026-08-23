import json
import subprocess
import sys


def run_brightdata_scraper(collector_id: str, target_url: str):
    """Triggers the Bright Data CLI scraper and handles structured JSON output."""
    command = ["bdata", "scraper", "run", collector_id, target_url, "--pretty"]

    print(f"Running scraper '{collector_id}' against {target_url}...")

    try:
        # Execute the bdata CLI command
        result = subprocess.run(
            command, capture_output=True, text=True, check=True, shell=True
        )

        output_data = result.stdout.strip()
        print("\n--- Scraper Data Received Successfully ---")
        print(output_data)

        # Optionally save output locally
        with open("sample_output.json", "w", encoding="utf-8") as f:
            f.write(output_data)
        print("\nOutput saved to sample_output.json")

    except subprocess.CalledProcessError as error:
        print(
            f"Failed to execute CLI command: {error.stderr}", file=sys.stderr
        )
        sys.exit(1)


if __name__ == "__main__":
    COLLECTOR_ID = "c_mt4jg2ema3kazbv18"
    TARGET_URL = "http://books.toscrape.com/"

    run_brightdata_scraper(COLLECTOR_ID, TARGET_URL)
