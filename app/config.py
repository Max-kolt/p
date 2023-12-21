from dotenv import load_dotenv
import os

# Default settings
DEBUG = True
APP_NAME = "QuizzSite"
ACCESS_TOKEN_EXPIRE_MINUTES = 30

# Hidden env variables
load_dotenv()

APP_HOST = os.getenv('APP_HOST', '127.0.0.1')
APP_PORT = int(os.getenv('APP_PORT', '8000'))

DB_HOST = os.getenv('DB_HOST')
DB_PORT = int(os.getenv('DB_PORT'))
DB_NAME = os.getenv('DB_NAME')
DB_USER = os.getenv('DB_USER')
DB_PASSWORD = os.getenv('DB_PASSWORD')

REDIS_HOST = os.getenv('REDIS_HOST')
REDIS_PORT = int(os.getenv('REDIS_PORT'))

SECRET_AUTH_KEY = os.environ.get("SECRET_AUTH_KEY")
ALGORITHM = os.environ.get("ALGORITHM")
EXPIRE_DELTA_TOKEN_MINUTES = int(os.environ.get("EXPIRE_DELTA_TOKEN_MINUTES", 60))

SMTP_USER = os.environ.get("SMTP_USER")
SMTP_PASSWORD = os.environ.get("SMTP_PASSWORD")