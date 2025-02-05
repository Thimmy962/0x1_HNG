#!/bin/bash
while true; do
    # Send request and store HTTP status
    STATUS=$(curl -s -o /dev/null -w "%{http_code}" "https://zerox1-hng.onrender.com/api/classify-number?number=0")

    # Check if request was successful (HTTP 200)
    if [ "$STATUS" -eq 200 ]; then
        echo "Request successful: $STATUS"
    else
        echo "Request failed: $STATUS"
    fi

    # Wait before the next request
    sleep 300  
done
