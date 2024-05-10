import requests
import json
import yaml

def get_secrets():
    with open("steam_api.yml", 'r') as stream:
        data_loaded = yaml.safe_load(stream)
    return data_loaded
    
    f = open("steam_api.txt", "r")
    return f.read()

def get_data(api,params=None):
    response = requests.get(api,params)
    if response.status_code == 200:
        print("Successfully fetched the data")
        return(response.json())
    else:
        print(f"Error: {response.status_code}. Failed to fetch data.")
        print("Response content:", response.content)

def formatted_print(self, obj):
    text = json.dumps(obj, sort_keys=True, indent=4)
    print(text)

def app_list():
    get_apps='https://api.steampowered.com/ISteamApps/GetAppList/v2/'
    data=get_data(get_apps)
    return (data['applist']['apps'] )