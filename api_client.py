import requests
from requests.exceptions import HTTPError, Timeout, RequestException
import logging

logging.basicConfig(level=logging.INFO)


class APIClient:
    """
    A reusable API client implementation with comprehensive error handling.

    Attributes:
        base_url (str): The base URL for the API.
        headers (dict): Default headers to include in every request.
        timeout (int): Timeout duration for requests in seconds.
    """

    def __init__(self, base_url, headers=None, timeout=10):
        """
        Initializes the APIClient with the given base URL, headers, and timeout.

        Args:
            base_url (str): The base URL for the API.
            headers (dict, optional): Default headers to include in every request. Defaults to None.
            timeout (int, optional): Timeout duration for requests in seconds. Defaults to 10.
        """
        self.base_url = base_url
        self.headers = headers if headers is not None else {}
        self.timeout = timeout

    def _handle_response(self, response):
        """
        Handles the HTTP response and raises appropriate errors if necessary.

        Args:
            response (requests.Response): The HTTP response object.

        Returns:
            dict: JSON response if the request was successful.

        Raises:
            HTTPError: If the HTTP request returned an unsuccessful status code.
        """
        try:
            response.raise_for_status()
        except HTTPError as http_err:
            logging.error(f'HTTP error occurred: {http_err}')
            raise
        except Exception as err:
            logging.error(f'Other error occurred: {err}')
            raise
        else:
            return response.json()

    def get(self, endpoint, params=None):
        """
        Sends a GET request to the specified endpoint.

        Args:
            endpoint (str): The API endpoint to send the GET request to.
            params (dict, optional): URL parameters to include in the request. Defaults to None.

        Returns:
            dict: JSON response from the API.
        """
        url = f"{self.base_url}/{endpoint}"
        try:
            response = requests.get(url, headers=self.headers, params=params, timeout=self.timeout)
            return self._handle_response(response)
        except Timeout:
            logging.error('The request timed out')
            raise
        except RequestException as req_err:
            logging.error(f'Request exception occurred: {req_err}')
            raise

    def post(self, endpoint, data=None):
        """
        Sends a POST request to the specified endpoint.

        Args:
            endpoint (str): The API endpoint to send the POST request to.
            data (dict, optional): The data to include in the POST request. Defaults to None.

        Returns:
            dict: JSON response from the API.
        """
        url = f"{self.base_url}/{endpoint}"
        try:
            response = requests.post(url, headers=self.headers, json=data, timeout=self.timeout)
            return self._handle_response(response)
        except Timeout:
            logging.error('The request timed out')
            raise
        except RequestException as req_err:
            logging.error(f'Request exception occurred: {req_err}')
            raise

    def put(self, endpoint, data=None):
        """
        Sends a PUT request to the specified endpoint.

        Args:
            endpoint (str): The API endpoint to send the PUT request to.
            data (dict, optional): The data to include in the PUT request. Defaults to None.

        Returns:
            dict: JSON response from the API.
        """
        url = f"{self.base_url}/{endpoint}"
        try:
            response = requests.put(url, headers=self.headers, json=data, timeout=self.timeout)
            return self._handle_response(response)
        except Timeout:
            logging.error('The request timed out')
            raise
        except RequestException as req_err:
            logging.error(f'Request exception occurred: {req_err}')
            raise

    def delete(self, endpoint):
        """
        Sends a DELETE request to the specified endpoint.

        Args:
            endpoint (str): The API endpoint to send the DELETE request to.

        Returns:
            dict: JSON response from the API.
        """
        url = f"{self.base_url}/{endpoint}"
        try:
            response = requests.delete(url, headers=self.headers, timeout=self.timeout)
            return self._handle_response(response)
        except Timeout:
            logging.error('The request timed out')
            raise
        except RequestException as req_err:
            logging.error(f'Request exception occurred: {req_err}')
            raise


if __name__ == "__main__":
    # Example usage
    client = APIClient(base_url="https://jsonplaceholder.typicode.com", headers={"Content-Type": "application/json"})

    # GET request example
    try:
        response = client.get("posts/1")
        logging.info(response)
    except Exception as e:
        logging.error(f"An error occurred: {e}")

    # POST request example
    try:
        response = client.post("posts", data={"title": "foo", "body": "bar", "userId": 1})
        logging.info(response)
    except Exception as e:
        logging.error(f"An error occurred: {e}")

    # PUT request example
    try:
        response = client.put("posts/1", data={"id": 1, "title": "foo", "body": "bar", "userId": 1})
        logging.info(response)
    except Exception as e:
        logging.error(f"An error occurred: {e}")

    # DELETE request example
    try:
        response = client.delete("posts/1")
        logging.info(response)
    except Exception as e:
        logging.error(f"An error occurred: {e}")