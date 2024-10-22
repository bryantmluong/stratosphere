import alpaca_trade_api as tradeapi
import os
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv("APCA_API_KEY_ID")
SECRET_KEY = os.getenv("APCA_API_SECRET_ID")
BASE_URL = os.getenv("APCA_API_BASE_URL")  # Use 'https://api.alpaca.markets' for live trading

api = tradeapi.REST(API_KEY, SECRET_KEY, BASE_URL, api_version='v2')

# Get account information
account = api.get_account()
print(f"Account status: {account.status}")
