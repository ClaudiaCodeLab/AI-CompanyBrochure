import requests
from bs4 import BeautifulSoup
from config import HEADERS
import logging

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class Website:
    """
    A utility class to represent and scrape website content.
    """

    def __init__(self, url):
        self.url = url
        self.title = "No title found"
        self.text = ""
        self.links = []

        try:
            response = requests.get(url, headers=HEADERS)
            response.raise_for_status()
            self.body = response.content
            soup = BeautifulSoup(self.body, 'html.parser')

            self.title = soup.title.string if soup.title else "No title found"

            if soup.body:
                for irrelevant in soup.body(["script", "style", "img", "input"]):
                    irrelevant.decompose()
                self.text = soup.body.get_text(separator="\n", strip=True)

            links = [link.get('href') for link in soup.find_all('a')]
            self.links = [link for link in links if link]
        except requests.RequestException as e:
            logging.error(f"Error fetching URL {url}: {e}")

    def get_contents(self):
        """
        Returns the webpage title and text content.
        """
        return f"Webpage Title:\n{self.title}\nWebpage Contents:\n{self.text}\n\n"