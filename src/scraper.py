import requests
from config.config import BASE_URL, HEADERS

def fetch_page(url):
    """Fetch the HTML content of a given URL."""
    try:
        response = requests.get(url, headers=HEADERS)
        response.raise_for_status()
        return response.text
    except requests.exceptions.RequestException as e:
        print(f"Error fetching {url}: {e}")
        return None

if __name__ == "__main__":
    html_content = fetch_page(BASE_URL)
    if html_content:
        print("Successfully fetched the main page.")
    else:
        print("Failed to fetch the main page.")
