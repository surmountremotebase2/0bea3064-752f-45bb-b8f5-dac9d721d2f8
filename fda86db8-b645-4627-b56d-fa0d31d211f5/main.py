from surmount.base_class import Strategy, TargetAllocation
from surmount.technical_indicators import RSI
from surmount.logging import log

class TradingStrategy(Strategy):
    def __init__(self):
        # Although SPX500 is not directly supported via ticker in most APIs, it's represented with a proxy.
        # Typically, S&P 500 ETFs like SPY can be used as a proxy. Adjust based on available data.
        self.ticker = "SPY"
    
    @property
    def assets(self):
        # Return the ticker as the asset to include in the strategy
        return [self.ticker]

    @property
    def interval(self):
        # Interval set to 1day for daily RSI calculation
        return "1day"
        
    def run(self, data):
        # Initialize the allocation dictionary; no allocation by default
        allocation_dict = {self.ticker: 0}

        # Calculate the RSI for the SPX500 proxy, here assumed to be SPY
        rsi_values = RSI(self.ticker, data["ohlcv"], length=14)  # Using a 14-day period for RSI calculation
        
        if rsi_values:
            # Check the latest RSI value to decide on allocation
            latest_rsi = rsi_values[-1]
            log(f"Latest RSI for {self.ticker}: {latest_rsi}")
            
            if latest_rsi > 70:
                # If RSI is above 70, allocate a portion to SPX500 proxy (SPY)
                # The allocation percentage is conceptually equivalent to "buying $20 of SPX500" within constraint.
                # Note: The platform restricts us to ratios, not specific dollar values.
                allocation_dict[self.ticker] = 1  # Allocating fully to SPY; adjust ratio based on actual strategy needs
                
        return TargetAllocation(allocation_dict)