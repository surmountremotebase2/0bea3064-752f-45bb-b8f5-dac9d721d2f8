from surmount.base_class import Strategy, TargetAllocation
from surmount.technical_indicators import RSI, EMA
from surmount.data import Asset  # Assuming this is how you access asset data

class TradingStrategy(Strategy):
    def __init__(self):
        # Assuming SPX500 is how you refer to the S&P 500 within this framework
        self.tickers = ["SPX500"]

    @property
    def interval(self):
        return "1day"  # Choose appropriate interval

    @property
    def assets(self):
        return self.tickers

    def run(self, data):
        # Initialize target allocation for SPX500 to maintain current position
        spx500_stake = 1.0  # Assume fully invested before the check

        # Calculate EMA and RSI for SPX500
        ema_spx500 = EMA("SPX500", data["ohlcv"], length=14)  # Example length for EMA
        rsi_spx500 = RSI("SPX500", data["ohlcv"], length=14)  # Example length for RSI

        # Check conditions: Adjust the condition for EMA based on your original intent
        if len(ema_spx500) > 0 and len(rsi_spx500) > 0 and rsi_spx500[-1] > 70:
            spx500_stake = 0.9  # Reduce allocation by adjusting the stake down, example adjustment

        # Return the new target allocation
        return TargetAllocation({"SPX500": spx500_stake})