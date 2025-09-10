from dotenv import load_dotenv
import os

load_dotenv('.env')
API_KEY = os.getenv('API_KEY')
USERNAME = os.getenv('USERNAMEE')

print(f"API_KEY: {API_KEY}")
print(f"USERNAME: {USERNAME}")
PASSWORD = os.getenv('PASSWORD')
print(f"PASSWORD: {PASSWORD}")

print("Environment variables loaded successfully.")
for var in ['API_KEY', 'USERNAME', 'PASSWORD']:
    if os.getenv(var) is None:
        print(f"Warning: {var} is not set.")

a= 2+2
from dotenv import load_dotenv
b= 3+3