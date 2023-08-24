import requests

def get_location(ip_address):
    url = f"http://ip-api.com/json/{ip_address}"
    response = requests.get(url)
    data = response.json()
    return data

if __name__ == "__main__":
    ip_address = input("Enter the IP address: ")
    location_data = get_location(ip_address)
    
    print("Location Details:")
    print(f"IP Address: {ip_address}")
    
    if location_data["status"] == "success":
        print(f"Country: {location_data['country']}")
        print(f"City: {location_data['city']}")
    else:
        print("No location information found.")

