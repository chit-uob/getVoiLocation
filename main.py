import time
import handle_response
import make_api_requests

while True:
    try:
        response = make_api_requests.get_scooter_locations()
    except:
        print("Failed to get scooter locations, retrying in 5 seconds")
        time.sleep(5)
        continue
    try:
        handle_response.store_response(response)
    except:
        print("Failed to store response, will skip storing the response")
    time.sleep(60)