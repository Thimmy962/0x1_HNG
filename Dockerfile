# start from the official Python slim image
FROM python:3.10-slim

# Disable buffering to ensure logs are immediately visible
ENV PYTHONUNBUFFERED=1

# Set the working directory inside the container
WORKDIR /app


#    copy the requirement file alone here, in case where there are modifications in the folder but no the requirement.txt file
#   this layer would be cached and there wont be any reason to install the requirements again which makes docker building faster
 
COPY requirements.txt .

# Install dependencies using the requirements.txt located in /app
RUN pip install -r requirements.txt

# Copy the entire project (including the library_management folder)
COPY . .

# Expose port 8080 for the application
EXPOSE 8080

# Start the application using Gunicorn
CMD ["./bash"]
