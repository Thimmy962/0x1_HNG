import time
import requests

# URL to ping
url = "https://zerox1-hng.onrender.com/api/classify-number?number=0"

# Loop to keep pinging the website every 5 minutes
while True:
    try:
        # Send GET request
        response = requests.get(url)
        
        # Check if the request was successful (status code 200)
        if response.status_code == 200:
            continue
        else:
            continue
    except requests.exceptions.RequestException as e:
        # Print any errors if the request fails
        print(f"Error: {e}")

    # Wait for 5 minutes before pinging again
    time.sleep(300)  # 300 seconds = 5 minutes
