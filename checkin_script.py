import logging
import requests
from unittest.mock import patch, Mock

# Setup logging
logging.basicConfig(level=logging.INFO)

# Configuration (normally from config.py)
APIKey = "mock-api-key"
biUsername = "mock-user"
BIServer = "mockserver.beyondtrustcloud.com"
BASE_URL = f"https://{BIServer}/BeyondTrust/api/public/v3"

# Construct headers
AUTH_HEADER = {
    'Authorization': f'PS-Auth key={APIKey}; runas={biUsername};',
    'Content-type': 'application/json'
}

def sign_in(session):
    url = f"{BASE_URL}/Auth/SignAppin"
    response = session.post(url, verify=False)
    response.raise_for_status()
    logging.info("Signed in successfully.")

def get_open_requests(session):
    url = f"{BASE_URL}/Requests"
    response = session.get(url, verify=False)
    response.raise_for_status()
    return response.json()

def checkin_request(session, request_id):
    url = f"{BASE_URL}/Requests/{request_id}/Checkin"
    reason = { "Reason": "Demo Complete" }
    response = session.put(url, json=reason, verify=False)

    if response.status_code == 204:
        logging.info(f"Request {request_id} checked in successfully.")
    else:
        logging.warning(f"Failed to check in request {request_id}. Status: {response.status_code}")

# Main function with mocks
@patch('requests.Session.post')
@patch('requests.Session.get')
@patch('requests.Session.put')
def main(mock_put, mock_get, mock_post):
    # Mock API responses
    mock_post.return_value = Mock(status_code=200)
    mock_get.return_value = Mock(status_code=200)
    mock_get.return_value.json.return_value = [
        {'RequestID': '12345'},
        {'RequestID': '67890'}
    ]
    mock_put.return_value = Mock(status_code=204)

    session = requests.Session()
    session.headers.update(AUTH_HEADER)

    try:
        sign_in(session)
        open_requests = get_open_requests(session)
        for req in open_requests:
            checkin_request(session, req['RequestID'])
    except requests.exceptions.RequestException as e:
        logging.error(f"API error occurred: {e}")

if __name__ == "__main__":
    main()
