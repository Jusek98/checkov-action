
# Flask App

This is a simple Flask application called "Flask App". This guide explains how to set up and launch the application using Docker Compose.
You have 2 main ways to run the application Locally or via Containers. You also have 2 databases a local one and a production one.  

## Project Structure

```
zoo-zone-flask-app/
│
├── app/
│   ├── __init__.py
│   ├── routes.py
│
├── requirements.txt
├── run.py
├── Dockerfile
└── docker-compose.yml
```

## Files and Directories

- **app/**: Directory containing the Flask application code.
  - **__init__.py**: Initializes the Flask app.
  - **routes.py**: Contains the route definitions for the app.
- **requirements.txt**: Lists the Python dependencies for the Flask app.
- **run.py**: Entry point for running the Flask app.
- **Dockerfile**: Defines the Docker image for the Flask app.
- **docker-compose.yml**: Defines the Docker Compose services.

## Requirements

- Docker
- Docker Compose
- Python 11


## Local Setup


### 1. Clone the project 


### 2. Enviromment variable file 

- Create a .env file 

- Add these environmment variables  and replace ```username``` and ```password``` by the actual values 
```bash
MONGO_URI_PROD=mongodb+srv://<username>:<password>@cluster0.kfeir2a.mongodb.net/ZooZone?retryWrites=true&w=majority&appName=Cluster0
MONGO_URI_DEV=mongodb://localhost:27017/ZooZone
FLASK_ENV=development
```
To connect to your local Database you can launch the mongodb container with this command.

```bash 
docker-compose up -d db
```

If you want to use the production database in the .env file replace the value of the ```FLASK_ENV``` variable by ```production```

### 3. Run the application 

To run the application you can use this command at the root of your directory 

```bash 
python run.py 
```
You should get something like this in the terminal 
```bash 
MongoDB connection successful
 * Serving Flask app 'app' (lazy loading)
 * Environment: development
 * Debug mode: on
 * Running on all addresses.
   WARNING: This is a development server. Do not use it in a production deployment.
 * Running on http://10.0.0.166:5000/ (Press CTRL+C to quit)
 * Restarting with stat
 * Debugger is active!
 * Debugger PIN: 194-337-520
```

## Container Setup

### 1. Environment Variable File

1. **Create a `.env` file** in the root of your project directory.
2. **Add environment variables** to the `.env` file. Make sure to update `MONGO_URI_DEV` as follows:

```env
MONGO_URI_DEV=mongodb://db:27017/ZooZone
```

The `MONGO_URI_DEV` uses `db` instead of `localhost` to refer to the MongoDB service. This is because `db` is the service name defined in the Docker Compose configuration, allowing the Flask application container to communicate with the MongoDB container.
### 2. Build and Run with Docker Compose

Navigate to the project directory:

```bash
cd zoo-zone-flask-app
```

Build and start the services:

```bash
docker-compose up --build
```

This command will build the Docker image and start the Flask application in a container. The application will be accessible at `http://localhost:5000`.






### 2. Stopping the Application

To stop the application, press `Ctrl+C` in the terminal where `docker-compose` is running. To remove the containers, run:

```bash
docker-compose down
```

### Check everything is working

### 1. Check via the broswer 
Go to the adreess given in the terminal.

You should see this message 
```bash 
Welcome to ZooZone Flask App!
```

### 2. Check via the logs 

Run this command to check the logs 
``` bash 
docker logs -f zoo-zone-flask-app_web_1 
```
You should see something like this 
```bash 
MongoDB connection successful
 * Serving Flask app 'app' (lazy loading)
 * Environment: development
 * Debug mode: on
 * Running on all addresses.
   WARNING: This is a development server. Do not use it in a production deployment.
 * Running on http://10.0.0.166:5000/ (Press CTRL+C to quit)
 * Restarting with stat
 * Debugger is active!
 * Debugger PIN: 194-337-520
```


## Check production Database
To check if the production database works correctly you can go the url given by the terminal and add  ```/membres```


You should see this 
```bash 
[{"name":"junior"}]
```
