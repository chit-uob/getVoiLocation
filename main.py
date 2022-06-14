import time
import handle_response
import make_api_requests

while True:
    response = make_api_requests.get_scooter_locations()
    handle_response.store_response(response)
    time.sleep(60)