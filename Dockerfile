# Use Python 3.11.2 as the base image
FROM python:3.11.2-slim-buster

# Set the working directory to /app
WORKDIR /app

# Copy the requirements file to the container
COPY requirements.txt .

# Install the required packages
RUN pip install --no-cache-dir -r requirements.txt

# Copy the demo.py script to the container
COPY demo.py .

# Set the command to run the demo.py script with the specified arguments
CMD ["python", "demo.py", "highrise", "Ansh:Bot", "641594f85b41ee085ed62db0", "98b2a2bf950cfc7fd4e6261203bc8279b3ed8b877c1bb7e73b404f9c4d459f7a"]
