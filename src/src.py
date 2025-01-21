from alpaca.trading.client import TradingClient
from alpaca.trading.enums import OrderSide, TimeInForce
from alpaca.data.historical import StockHistoricalDataClient
from alpaca.trading.requests import MarketOrderRequest
import config
import StockData

client = TradingClient(config.API_KEY, config.SECRET_KEY, paper=True)
historical_client = StockHistoricalDataClient(config.API_KEY, config.SECRET_KEY)

# Fetch latest SPY price
bars = historical_client.get_stock_bars(
    "SPY",
    timeframe = "minute",
    limit = 30  #price of the last 30 minutes
)
latest_price = bars.df['close'].iloc[-1]

strike_tolerance = 3.0  # within strike price
expiration_days = 7     # expiry date

def get_options_symbol(latest_price, direction):
    """
    Replace with API calls to dynamically fetch options data.
    """
    strike_price = round(latest_price + (3 if direction == "up" else -3), 1)
    expiration_date = "2025-01-26"  # Example expiration date
    options_symbol = f"SPY{expiration_date.replace('-', '')}{'C' if direction == 'up' else 'P'}{int(strike_price * 100)}"
    return options_symbol

# Simple prediction logic using moving averages
prices = bars.df['close']
sma_short = prices.rolling(window=5).mean().iloc[-1]
sma_long = prices.rolling(window=20).mean().iloc[-1]
prediction = "up" if sma_short > sma_long else "down"

# Get appropriate options symbol
options_symbol = get_options_symbol(latest_price, prediction)

# Function to place an options order
def place_options_order(symbol, side, qty=1):
    order_details = MarketOrderRequest(
        symbol=symbol,  # This should be the specific options symbol
        qty=qty,        # Number of contracts
        side=side,      # BUY or SELL
        time_in_force=TimeInForce.DAY,
    )
    try:
        order = client.submit_order(order_data=order_details)
        print(f"Options order submitted: {order}")
    except Exception as e:
        print(f"Failed to place order: {e}")

# Place the order based on prediction
if prediction == "up":
    print(f"Buying a CALL option: {options_symbol}")
    place_options_order(options_symbol, OrderSide.BUY)
elif prediction == "down":
    print(f"Buying a PUT option: {options_symbol}")
    place_options_order(options_symbol, OrderSide.BUY)
