from flask import Flask
from flask_pymongo import PyMongo
from dotenv import load_dotenv
import os

load_dotenv()  # take environment variables from .env.

app = Flask(__name__)

# Check if the environment is development
if os.getenv("ENV") == "dev":
    app.config["MONGO_URI"] = os.getenv("MONGO_URI_DEV")
else:
    app.config["MONGO_URI"] = os.getenv("MONGO_URI_PROD")

mongo = PyMongo(app)

try:
    # The ismaster command is cheap and does not require auth.
    mongo.db.command('ismaster')
    print("MongoDB connection successful")
except Exception as e:
    print("Failed to connect to MongoDB", e)

from app import routes  # Import routes at the end to avoid circular import