#!/bin/bash
while true; do
    curl -s http://localhost:8080/api/classify-number?number=0 > /dev/null
    sleep 300  # Wait for 5 minutes before pinging again
done