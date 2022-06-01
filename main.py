import time

import handle_response
import make_api_request

while True:
    response = make_api_request.get_scooter_locations()
    handle_response.store_response(response)
    time.sleep(60)