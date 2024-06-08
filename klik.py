import requests
import random
import time
import json
from colorama import Fore, Style

# URL endpoints
login_url = "https://api.yescoin.gold/user/login"
game_info_url = "https://api.yescoin.gold/game/getGameInfo"
special_box_info_url = "https://api.yescoin.gold/game/getSpecialBoxInfo"
collect_special_box_coin_url = "https://api.yescoin.gold/game/collectSpecialBoxCoin"
collect_coin_url = "https://api.yescoin.gold/game/collectCoin"

# Headers for login
login_headers = {
    "Accept": "application/json, text/plain, */*",
    "Accept-Encoding": "gzip, deflate, br",
    "Accept-Language": "en-US,en;q=0.9",
    "Content-Type": "application/json",
    "Origin": "https://www.yescoin.gold",
    "Priority": "u=1, i",
    "Referer": "https://www.yescoin.gold/",
    "Sec-Ch-Ua": "\"Not_A Brand\";v=\"99\", \"Google Chrome\";v=\"109\", \"Chromium\";v=\"109\"",
    "Sec-Ch-Ua-Mobile": "?1",
    "Sec-Ch-Ua-Platform": "\"Android\"",
    "Sec-Fetch-Dest": "empty",
    "Sec-Fetch-Mode": "cors",
    "Sec-Fetch-Site": "same-site",
    "User-Agent": "Mozilla/5.0 (Linux; Android 8.0.0; SM-G955U Build/R16NW) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.141 Mobile Safari/537.36"
}

# Function to login and get token
def login_and_get_token(login_payload):
    response = requests.post(login_url, headers=login_headers, json=login_payload)
    response_data = response.json()
    token = response_data['data']['token']
    return token

# Function to get game info
def get_game_info(token):
    game_info_headers = {
        "Accept": "application/json, text/plain, */*",
        "Accept-Encoding": "gzip, deflate, br",
        "Accept-Language": "en-US,en;q=0.9",
        "Content-Type": "application/json",
        "Origin": "https://www.yescoin.gold",
        "Priority": "u=1, i",
        "Referer": "https://www.yescoin.gold/",
        "Sec-Ch-Ua": "\"Not_A Brand\";v=\"99\", \"Google Chrome\";v=\"109\", \"Chromium\";v=\"109\"",
        "Sec-Ch-Ua-Mobile": "?1",
        "Sec-Ch-Ua-Platform": "\"Android\"",
        "Sec-Fetch-Dest": "empty",
        "Sec-Fetch-Mode": "cors",
        "Sec-Fetch-Site": "same-site",
        "User-Agent": "Mozilla/5.0 (Linux; Android 8.0.0; SM-G955U Build/R16NW) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.141 Mobile Safari/537.36",
        "Token": token
    }
    
    response = requests.get(game_info_url, headers=game_info_headers)
    response_data = response.json()
    
    coin_pool_total = response_data['data']['coinPoolTotalCount']
    coin_pool_left = response_data['data']['coinPoolLeftCount']
    
    return coin_pool_total, coin_pool_left

# Function to get special box info
def get_special_box_info(token):
    special_box_info_headers = {
        "Accept": "application/json, text/plain, */*",
        "Accept-Encoding": "gzip, deflate, br",
        "Accept-Language": "en-US,en;q=0.9",
        "Content-Type": "application/json",
        "Origin": "https://www.yescoin.gold",
        "Priority": "u=1, i",
        "Referer": "https://www.yescoin.gold/",
        "Sec-Ch-Ua": "\"Not_A Brand\";v=\"99\", \"Google Chrome\";v=\"109\", \"Chromium\";v=\"109\"",
        "Sec-Ch-Ua-Mobile": "?1",
        "Sec-Ch-Ua-Platform": "\"Android\"",
        "Sec-Fetch-Dest": "empty",
        "Sec-Fetch-Mode": "cors",
        "Sec-Fetch-Site": "same-site",
        "User-Agent": "Mozilla/5.0 (Linux; Android 8.0.0; SM-G955U Build/R16NW) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.141 Mobile Safari/537.36",
        "Token": token
    }
    
    response = requests.get(special_box_info_url, headers=special_box_info_headers)
    return response.text

# Function to collect special box coin
def collect_special_box_coin(token):
    collect_special_box_coin_headers = {
        "Accept": "application/json, text/plain, */*",
        "Accept-Encoding": "gzip, deflate, br",
        "Accept-Language": "en-US,en;q=0.9",
        "Content-Type": "application/json",
        "Origin": "https://www.yescoin.gold",
        "Priority": "u=1, i",
        "Referer": "https://www.yescoin.gold/",
        "Sec-Ch-Ua": "\"Not_A Brand\";v=\"99\", \"Google Chrome\";v=\"109\", \"Chromium\";v=\"109\"",
        "Sec-Ch-Ua-Mobile": "?1",
        "Sec-Ch-Ua-Platform": "\"Android\"",
        "Sec-Fetch-Dest": "empty",
        "Sec-Fetch-Mode": "cors",
        "Sec-Fetch-Site": "same-site",
        "User-Agent": "Mozilla/5.0 (Linux; Android 8.0.0; SM-G955U Build/R16NW) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.141 Mobile Safari/537.36",
        "Token": token
    }
    
    coin_count = random.randint(250, 500)
    collect_special_box_coin_payload = {
        "boxType": 1,
        "coinCount": coin_count
    }
    
    response = requests.post(collect_special_box_coin_url, headers=collect_special_box_coin_headers, json=collect_special_box_coin_payload)
    return response.text

# Function to collect coin
def collect_coin(token):
    collect_coin_headers = {
        "Accept": "application/json, text/plain, */*",
        "Accept-Encoding": "gzip, deflate, br",
        "Accept-Language": "en-US,en;q=0.9",
        "Content-Type": "application/json",
        "Origin": "https://www.yescoin.gold",
        "Referer": "https://www.yescoin.gold/",
        "Sec-Ch-Ua": "\"Not_A Brand\";v=\"99\", \"Google Chrome\";v=\"109\", \"Chromium\";v=\"109\"",
        "Sec-Ch-Ua-Mobile": "?1",
        "Sec-Ch-Ua-Platform": "\"Android\"",
        "Sec-Fetch-Dest": "empty",
        "Sec-Fetch-Mode": "cors",
        "Sec-Fetch-Site": "same-site",
        "User-Agent": "Mozilla/5.0 (Linux; Android 8.0.0; SM-G955U Build/R16NW) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.141 Mobile Safari/537.36",
        "Token": token
    }
    
    collect_coin_payload = random.randint(50, 200)
    
    response = requests.post(collect_coin_url, headers=collect_coin_headers, json=collect_coin_payload)
    return response.text


# Main function to execute the flow
def main():
    with open('data.json', 'r') as file:
        login_data_list = json.load(file)
    
    while True:
        for login_payload in login_data_list:
            token = login_and_get_token(login_payload)
            coin_pool_total, coin_pool_left = get_game_info(token)
            
            special_box_info_response = get_special_box_info(token)
            collect_special_box_coin_response = collect_special_box_coin(token)
            
            username = login_payload["code"].split('"username":"')[1].split('","')[0]
            
            print(f"{Fore.GREEN}==================YES===============")
            print(f"{Style.RESET_ALL}Username: {username}")
            print(f"{Fore.YELLOW}==============Game Info=============")
            print(f"{Style.RESET_ALL}Coin Pool: {coin_pool_total}")
            print(f"Coin Pool Left: {coin_pool_left}")
            print(f"-------------------------------------")
            print(f"{Fore.YELLOW}=============Special Box===============")
            print(f"{Style.RESET_ALL}Get Box: {special_box_info_response}")
            print(f"Claim Box: {collect_special_box_coin_response}")
            print(f"-------------------------------------")
            
            print(f"-------------------------------------")
            print(f"{Fore.YELLOW}=============Main Game===============")
            
            # Wait until coin_pool_left is greater than 1000
            while coin_pool_left <= 100:
                time.sleep(5)  # Delay 5 seconds before checking again
                coin_pool_total, coin_pool_left = get_game_info(token)
                
            collect_coin_response = collect_coin(token)
            print(f"Collect Coin: {collect_coin_response}")
            print(f"{Fore.GREEN}==================YES===============")
        
        time.sleep(random.randint(1, 10))  # Random sleep between 1 to 10 seconds

if __name__ == "__main__":
    main()


