# Dockerfile for the Python 3.10 image
FROM python:3.10

# Set the working directory in the container
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . /app

# Install the required packages
RUN pip install -r requirements.txt

EXPOSE 3000

# Run the application
CMD [ "python", "app.py" ]
