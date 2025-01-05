from surmount.base_class import Strategy, TargetAllocation
from surmount.technical_indicators import RSI
from surmount.data import Asset
from surmount.logging import log

class TradingStrategy(Strategy):
    def __init__(self):
        self.tickers = ["SPX500"]  # Assuming "SPX500" is the symbol for S&P 500 index in the package

    @property
    def interval(self):
        return "1day"  # Adjust accordingly if a different time frame for the RSI calculation is desired

    @property
    def assets(self):
        return self.tickers

    @property
    def data(self):
        return []  # No additional data required beyond OHLCV for RSI calculation

    def run(self, data):
        allocation_dict = {}

        # Calculate RSI for SPX500
        rsi_values = RSI("SPX500", data["ohlcv"], length=14)  # Default RSI period length is 14

        if rsi_values is not None and len(rsi_values) > 0:
            latest_rsi = rsi_values[-1]
            log(f"Latest RSI for SPX500: {latest_rsi}")

            # Implementing the strategy logic based on RSI value
            if latest_rsi > 70:
                # Assuming a reduction in allocation represents a sell action; 
                # the actual value should be tailored to your portfolio's need.
                # This simple example sets allocation to 0 to illustrate action.
                allocation_dict["SPX500"] = 0  # Represents selling off the position; adjust as per actual strategy
            else:
                # Maintain or establish a position in SPX500
                allocation_dict["SPX500"] = 1  # This example goes all-in, but adjust the allocation as needed
        else:
            # No RSI calculation available, take no action or default action
            log("RSI calculation not available; taking no action.")
            allocation_dict["SPX500"] = 0  # Example default action, adjust as needed

        return TargetAllocation(allocation_dict)