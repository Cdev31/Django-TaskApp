import pyrebase
from .config import config

config = {
    "apiKey": config['api_key'],
    "authDomain": config['auth_domain'],
    "projectId": config['project_id'],
    "storageBucket": config['storage_bucket'],
    "messagingSenderId": config['messaging_sender_id'],
    "appId": config['app_id'],
    "databaseURL" : ""
}

firebase = pyrebase.initialize_app(config)
storage = firebase.storage()