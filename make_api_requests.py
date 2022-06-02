import requests
import configparser
import json

secret_config = configparser.ConfigParser()
secret_config.read('secret.ini')
authentication_token = secret_config['MAIN']['authenticationToken']
zone_id = secret_config['MAIN']['zoneId']
access_token = ""


def update_access_token():
    global access_token
    url = "https://api.voiapp.io/v1/auth/session"
    obj = {"authenticationToken": authentication_token}
    re = requests.post(url, json=obj)
    access_token_json = json.loads(re.text)
    access_token = access_token_json["accessToken"]
    # the invalid token response for invalid/expired access token is:
    # {"code":"401.2","detail":"Unauthorized, Token Invalid"}
    # <Response [401]>


def get_scooter_locations():
    url = f"https://api.voiapp.io/v2/rides/vehicles?zone_id={zone_id}"
    re = requests.get(url, headers={"x-access-token": access_token})
    if re.status_code == 401:
        update_access_token()
        re = requests.get(url, headers={"x-access-token": access_token})
    if re.status_code == 200:
        return json.loads(re.text)