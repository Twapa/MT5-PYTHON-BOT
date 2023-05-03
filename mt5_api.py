
import pandas as pd
from dateutil.parser import *
import MetaTrader5 as mt5 
import utils
import sys
import json
from datetime import datetime
class MT5API():

    def __init__(self):
        pass
    
    
    
    
    def fetch_candles(self, pair_name, count =10, granularity=mt5.TIMEFRAME_M1):
        bars = mt5.copy_rates_from_pos(pair_name, granularity, 0, count)
        df = pd.DataFrame(bars)
        
        
        return df

    def last_complete_candle(self, pair_name, granularity=mt5.TIMEFRAME_M1):
        df = self.fetch_candles(pair_name, granularity=granularity)
        
        # df['time']=pd.to_datetime(df['time'], unit='ms',utc=True)
        # df["time"] = [datetime.utcfromtimestamp(float(x)) for x in df["time"]]
        if df is None or df.shape[0] == 0:
        
            return None
        candle =df.iloc[-1].time

        lastcandle = datetime.fromtimestamp(candle)
        
        
          
        return    lastcandle
    
   

        
    


if __name__ == "__main__":
    mt5.initialize()
    api = MT5API()
    df = api.fetch_candles("EURUSD")
    print(df)
    # print(api.last_complete_candle("EURUSD"))
    