\# 🥠 Digital Fortune Cookie



A small web application built with Python and Flask and containerized using Docker.



The application generates random digital fortunes. Its behavior can be configured using the `APP\_MOOD` environment variable.



\## Available moods



\- `mysterious`

\- `funny`

\- `motivational`



\## Technologies



\- Python

\- Flask

\- HTML

\- CSS

\- JavaScript

\- Docker



\## Build the Docker image



From the project directory run:



```bash

docker build -t digital-fortune-cookie .



\## Run the container



Default mysterious mode:



```bash

docker run -d --name fortune-cookie -p 8081:5000 digital-fortune-cookie



Open:



http://localhost:8081



\## Run with an environment variable



Funny mode:



```bash

docker run -d --name fortune-cookie -p 8081:5000 -e APP\_MOOD=funny digital-fortune-cookie



Motivational mode:



```bash

docker run -d --name fortune-cookie -p 8081:5000 -e APP\_MOOD=motivational digital-fortune-cookie



Mysterious mode:



```bash

docker run -d --name fortune-cookie -p 8081:5000 -e APP\_MOOD=mysterious digital-fortune-cookie





Stop and remove the container



```bash

docker stop fortune-cookie

```bash

docker rm fortune-cookie



Or:



```bash

docker rm -f fortune-cookie





\## Docker configuration



The Flask application listens on port 5000 inside the container.



Docker maps host port 8081 to container port 5000:



8081:5000

HOST:CONTAINER



The APP\_MOOD environment variable changes which category of fortunes is generated without requiring changes to the source code.

