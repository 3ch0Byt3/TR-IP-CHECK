import requests
def get_ip_info(ip_address):
   
    url = f"http://ipinfo.io/{ip_address}?token=3c9355c23d88d9"
    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()
        return data
    else:
        return None
    
def display_ip_info(ip_info):
    if ip_info:
        print(f"IP Address: {ip_info.get('ip')}")
        print(f"City: {ip_info.get('city')}")
        print(f"Region: {ip_info.get('region')}")
        print(f"Country: {ip_info.get('country')}")
        print(f"Location: {ip_info.get('loc')}")
        print(f"Organization: {ip_info.get('org')}")
        print(f"Timezone: {ip_info.get('timezone')}")
    else:
        print("Failed to retrieve IP information.")

if __name__ == "__main__":
    ip_address = input("Enter the IP address: ")
    ip_info = get_ip_info(ip_address)
    display_ip_info(ip_info)

