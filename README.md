# Simple Flask Web Application with Docker and Debug
This repository contains a simple web application using Python Flask and Docker, designed to facilitate debugging in VSCode.

### Prerequisites
Make sure you have the following tools installed on your machine:
1. Docker
2. Docker Compose
3. VSCode
4. VSCode Dev Containers Extension

### Starting Your Flask App
1. Build images and start containers
```
docker-compose up -d --build
```
2. Start the web server
Navigate to the Remote Explorer tab, right-click the container, and select `Attach in New Window.`
Ensure the `src` folder is open in the Explorer tab.
Move to the Run and Debug tab and press the `Start debugging` button, selecting the `Python: Flask` option.

3. Open a browser and go to the following URL:
Example: http://127.0.0.1:5000