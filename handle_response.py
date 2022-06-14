import json
import os
from datetime import datetime
from pathlib import Path

current_date_string_precise_to_hour = ""


def put_inside_data_file(date_string_precise_to_hour, record_json):
    global current_date_string_precise_to_hour

    if current_date_string_precise_to_hour != "" and \
            current_date_string_precise_to_hour != date_string_precise_to_hour:
        with open(Path(f"data/location_data/scooter_data_{current_date_string_precise_to_hour}.json"), 'ab+') as f:
            f.seek(-3, os.SEEK_END)
            f.truncate()
        with open(Path(f"data/location_data/scooter_data_{current_date_string_precise_to_hour}.json"), 'a', newline='\n') as f:
            f.write("\n]\n")
    current_date_string_precise_to_hour = date_string_precise_to_hour

    data_file_path = Path(f"data/location_data/scooter_data_{date_string_precise_to_hour}.json")
    if not data_file_path.is_file():
        with open(data_file_path, 'w', newline='\n') as f:
            f.write("[\n")
    with open(data_file_path, 'a', newline='\n') as f:
        f.write(json.dumps(record_json))
        f.write(",\n")

    print(f"Placed data of {record_json['time_stamp']} in a file")


def store_response(response_json):
    scooter_list = response_json["data"]["vehicle_groups"][0]["vehicles"]
    vehicle_data = []
    for scooter in scooter_list:
        # vehicle_data_item = {
        #     'short': scooter['short'],
        #     'battery': scooter['battery'],
        #     'lng': scooter['location']['lng'],
        #     'lat': scooter['location']['lat'],
        #     'locked': scooter['locked']
        # }
        vehicle_data_item = [scooter['short'], scooter['battery'], scooter['location']['lng'],
                             scooter['location']['lat']]
        vehicle_data.append(vehicle_data_item)

    iso_time = datetime.now().isoformat()

    record = {
        'time_stamp': iso_time,
        'vehicle_count': len(scooter_list),
        'data_format': ["short", "battery", "lng", "lat"],
        'vehicle_data': vehicle_data
    }

    put_inside_data_file(iso_time[:13], record)