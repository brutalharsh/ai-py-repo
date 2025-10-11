# web_scraping_utils.py

import requests
from requests.exceptions import HTTPError, ConnectionError, Timeout, RequestException
from bs4 import BeautifulSoup
import time

def fetch_html(url, retries=3, delay=2):
    """
    Fetch HTML content from the specified URL.

    Args:
        url (str): The URL of the web page to fetch.
        retries (int): Number of retries for failed requests. Default is 3.
        delay (int): Delay between retries in seconds. Default is 2 seconds.

    Returns:
        str: HTML content of the web page.

    Raises:
        HTTPError: If an HTTP error occurs.
        ConnectionError: If a connection error occurs.
        Timeout: If the request times out.
        RequestException: If any other request-related error occurs.
    """
    attempt = 0
    while attempt < retries:
        try:
            response = requests.get(url, timeout=10)
            response.raise_for_status()
            return response.text
        except HTTPError as http_err:
            print(f"HTTP error occurred: {http_err}")
        except ConnectionError as conn_err:
            print(f"Connection error occurred: {conn_err}")
        except Timeout as timeout_err:
            print(f"Timeout error occurred: {timeout_err}")
        except RequestException as req_err:
            print(f"General error occurred: {req_err}")
        
        attempt += 1
        time.sleep(delay)
    
    raise Exception(f"Failed to fetch HTML content from {url} after {retries} attempts")

def parse_html(html_content):
    """
    Parse the HTML content using BeautifulSoup.

    Args:
        html_content (str): The HTML content to parse.

    Returns:
        BeautifulSoup: Parsed HTML content as a BeautifulSoup object.
    """
    return BeautifulSoup(html_content, 'html.parser')

# Example usage
if __name__ == "__main__":
    url = "https://example.com"
    try:
        html_content = fetch_html(url)
        soup = parse_html(html_content)
        print(soup.prettify())
    except Exception as e:
        print(f"An error occurred: {e}")