import subprocess
import json

def run_scraper(collector_id, url):
    print("Initiating self-healing pipeline...")
    command = f'bdata scraper run {collector_id} "{url}" --pretty'
    
    try:
        result = subprocess.run(command, shell=True, check=True, capture_output=True, text=True)
        print("Data successfully extracted!")
        print(result.stdout)
    except subprocess.CalledProcessError as e:
        print("Pipeline failed. Run 'bdata scraper heal' in terminal.")
      
run_scraper("c_mt4jg2ema3kazbv18", "http://books.toscrape.com/")
