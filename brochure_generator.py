from web_scraper import Website
from llm_client import get_relevant_links, query_llm
import logging

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def get_all_details(url):
    """
    Fetches the landing page and other relevant pages' contents for a given URL.
    """
    try:
        website = Website(url)
        details = "Landing page:\n" + website.get_contents()
    except Exception as e:
        logging.error(f"Failed to fetch landing page for {url}. Error: {e}")
        return f"Could not fetch the landing page for {url}. Error: {e}"

    try:
        links = get_relevant_links(website)
    except Exception as e:
        logging.error(f"Failed to fetch relevant links for {url}. Error: {e}")
        return details + f"\n\nCould not fetch links. Error: {e}"

    for link in links["links"]:
        try:
            details += f"\n\n{link['type']}:\n"
            details += Website(link["url"]).get_contents()
        except Exception as e:
            logging.warning(f"Could not fetch details for {link['url']}. Error: {e}")
            details += f"\n\nCould not fetch details for {link['url']}. Error: {e}\n"

    return details


def generate_brochure(company_name, url):
    """
    Generates a brochure for a company based on its website content.
    """
    system_prompt = (
        "You are an assistant that analyzes the contents of several relevant pages from a company website "
        "and creates a short brochure about the company for customers, investors, and recruits."
    )

    content = get_all_details(url)[:5000]

    messages = [
        {"role": "system", "content": system_prompt},
        {"role": "user", "content": f"Company: {company_name}\n{content}"}
    ]

    return query_llm(messages)