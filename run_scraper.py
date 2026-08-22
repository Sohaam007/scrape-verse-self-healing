import subprocess
import json

def run_scraper(collector_id, url):
    print("Initiating ScrapeVerse AI pipeline...\n")

    command = f'bdata scraper run {collector_id} "{url}" --pretty'

    try:
        result = subprocess.run(
            command,
            shell=True,
            check=True,
            capture_output=True,
            text=True
        )

        data = json.loads(result.stdout)

        with open("books.json", "w", encoding="utf-8") as f:
            json.dump(data, f, indent=2)

        print("Success! books.json created.")

    except subprocess.CalledProcessError as e:
        print("Scraper failed!")
        print(e.stderr)

run_scraper(
    "c_mt4jg2ema3kazbv18",
    "http://books.toscrape.com/"
)
