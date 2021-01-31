import Converter
import requests
import json

STEAM_API_KEY = os.environ['STEAM_API_KEY']

def lambda_handler(event, context):
    steam_id = Converter.to_steamID64("[U:1:{}]".format(event["steam_id"]), as_int=False)
    
    api_url = "https://api.steampowered.com/IPlayerService/GetOwnedGames/v0001/?key={}&steamid={}&format=json".format(STEAM_API_KEY, steam_id)
    steam_api_result = requests.get(api_url)
    steam_api_result.json()
    
    return {
        'statusCode': 200,
        'body': steam_api_result.json()
    }
