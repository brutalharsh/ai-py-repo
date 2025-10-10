import requests
import logging
from requests.exceptions import HTTPError, ConnectionError, Timeout
from time import sleep

logging.basicConfig(level=logging.INFO)

class APIClient:
    """
    A utility class for interacting with APIs.

    Attributes:
        base_url (str): The base URL for the API.
        headers (dict): Default headers to include in each request.
        auth (tuple): Authentication credentials (optional).

    Methods:
        get(endpoint, params): Sends a GET request to the specified endpoint.
        post(endpoint, data): Sends a POST request to the specified endpoint.
        put(endpoint, data): Sends a PUT request to the specified endpoint.
        delete(endpoint, params): Sends a DELETE request to the specified endpoint.
        patch(endpoint, data): Sends a PATCH request to the specified endpoint.
        head(endpoint, params): Sends a HEAD request to the specified endpoint.
    """

    def __init__(self, base_url, headers=None, auth=None):
        """
        Initializes the APIClient with a base URL, optional headers, and authentication.

        Parameters:
            base_url (str): The base URL for the API.
            headers (dict): Default headers to include in each request (optional).
            auth (tuple): Authentication credentials (optional).
        """
        self.base_url = base_url
        self.headers = headers if headers else {}
        self.auth = auth
    
    def _handle_response(self, response):
        """Handles the API response, raising exceptions for errors."""
        try:
            response.raise_for_status()
        except HTTPError as http_err:
            logging.error(f'HTTP error occurred: {http_err} - Response: {response.text}')
            raise
        except Exception as err:
            logging.error(f'Other error occurred: {err}')
            raise
        try:
            return response.json()
        except ValueError:
            return response.text

    def _request_with_retries(self, method, endpoint, retries=3, **kwargs):
        """Handles the request with retries for rate limiting."""
        for attempt in range(retries):
            try:
                response = requests.request(method, self.base_url + endpoint, headers=self.headers, auth=self.auth, **kwargs)
                return self._handle_response(response)
            except (ConnectionError, Timeout) as err:
                logging.warning(f'Attempt {attempt + 1} failed: {err}')
                if attempt < retries - 1:
                    sleep(2 ** attempt)  # Exponential backoff
                else:
                    raise
            except HTTPError as err:
                if response.status_code in [429, 503]:  # Rate limit or service unavailable
                    logging.warning(f'Rate limit error, attempt {attempt + 1}')
                    if attempt < retries - 1:
                        sleep(2 ** attempt)  # Exponential backoff
                    else:
                        raise
                else:
                    raise
            except Exception as err:
                logging.error(f'Unexpected error: {err}')
                raise

    def get(self, endpoint, params=None):
        """
        Sends a GET request to the specified endpoint.

        Parameters:
            endpoint (str): The API endpoint.
            params (dict): Query parameters (optional).

        Returns:
            dict: The JSON response.
        """
        return self._request_with_retries('GET', endpoint, params=params)

    def post(self, endpoint, data=None):
        """
        Sends a POST request to the specified endpoint.

        Parameters:
            endpoint (str): The API endpoint.
            data (dict): The body data (optional).

        Returns:
            dict: The JSON response.
        """
        return self._request_with_retries('POST', endpoint, json=data)

    def put(self, endpoint, data=None):
        """
        Sends a PUT request to the specified endpoint.

        Parameters:
            endpoint (str): The API endpoint.
            data (dict): The body data (optional).

        Returns:
            dict: The JSON response.
        """
        return self._request_with_retries('PUT', endpoint, json=data)

    def delete(self, endpoint, params=None):
        """
        Sends a DELETE request to the specified endpoint.

        Parameters:
            endpoint (str): The API endpoint.
            params (dict): Query parameters (optional).

        Returns:
            dict: The JSON response.
        """
        return self._request_with_retries('DELETE', endpoint, params=params)
    
    def patch(self, endpoint, data=None):
        """
        Sends a PATCH request to the specified endpoint.

        Parameters:
            endpoint (str): The API endpoint.
            data (dict): The body data (optional).

        Returns:
            dict: The JSON response.
        """
        return self._request_with_retries('PATCH', endpoint, json=data)
    
    def head(self, endpoint, params=None):
        """
        Sends a HEAD request to the specified endpoint.

        Parameters:
            endpoint (str): The API endpoint.
            params (dict): Query parameters (optional).

        Returns:
            dict: The headers from the response.
        """
        return self._request_with_retries('HEAD', endpoint, params=params)

if __name__ == "__main__":
    # Example usage:
    api_client = APIClient(
        base_url='https://api.example.com',
        headers={'Authorization': 'Bearer YOUR_API_TOKEN'}
    )

    # GET request example
    try:
        response = api_client.get('/resource', params={'param1': 'value1'})
        print(response)
    except Exception as e:
        logging.error(f'Error during GET request: {e}')

    # POST request example
    try:
        response = api_client.post('/resource', data={'key': 'value'})
        print(response)
    except Exception as e:
        logging.error(f'Error during POST request: {e}')