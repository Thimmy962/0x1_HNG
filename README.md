## **HNG JSON Response Project**

# Since this project requires only api, the views.py file
# will be in the same folder as the wsgi.py and asgi.py files

This project takes a number as string and returns a JSON response containing:
- ✅ the number as int
- ✅ is_prime: bool
- ✅ is_perfect: bool
- ✅ properties: a list containing armstrong and odd/even
- ✅ digit_sum of the number
- ✅ fun fact of the number

### If the not string is given or the string given contains non-digit, it returns 400 status code

---

### **🚀 Setup Instructions**

#### **1. Install Docker**
Install docker [here](https://www.docker.com/) if it has not been installed before

#### **2. Clone the Repository**
git clone https://github.com/Thimmy962/0x1_HNG
cd 0x1_HNG

#### **3. Create a .env file**
touch .env

#### **4. Open the .env file and add the following lines**
ALLOWED_HOSTS=localhost
DEBUG=True

#### **5. Build and Run the Docker Container**
##### docker build -t <image_name> .
##### docker run --name <container_name> -d -p 8080:8080 <image_name>

#### Once the container is running, you can access the JSON response by visiting: [here](http://localhost:8080)


# API Documentation

## Endpoint URL: https://hng-7y24.onrender.com/

##  Request format
        CLI: curl -X GET https://hng-7y24.onrender.com/api/
        Browser: https://hng-7y24.onrender.com/
        python: import requests
                response = requests.get("https://hng-7y24.onrender.com/api/")
                if response.status_code == 200:
                    print(response.json())
                else:
                    print("Failed to fetch data:", response.status_code)
    
### Response format: {
                    "email": "Oluwatimileyin962@gmail.Com",
                    "current_datetime": "2025-01-30T14:42:30Z",
                    "github_url": "https://github.com/Thimmy962/HNG"
                }
        
## Example usage:
        CLI: curl -X GET https://hng-7y24.onrender.com/


# HNG Backlink
If you're interested in hiring skilled Python developers, check out the [https://hng.tech/hire/python-developers](https://hng.tech/hire/python-developers).