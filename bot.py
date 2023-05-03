import pprint
import time
import MetaTrader5 as mt5 
from settings import Settings
from log_wrapper import LogWrapper
from timing import Timing
from dateutil.parser import *
from mt5_api import MT5API
from technicals import Technicals
from defs import NONE, BUY, SELL
from trade_manager import TradeManager

SLEEP = 10.0
GRANULARITY = granularity=mt5.TIMEFRAME_M1
class TradingBot():
    
    def __init__(self):
        self.log = LogWrapper("Bot")    
        self.log = LogWrapper("TradingBot")
        self.tech_log = LogWrapper("TechnicalsBot")
        self.trade_log = LogWrapper("Trade")
        self.trade_pairs = Settings.get_pairs()
        self.settings = Settings.load_settings()
        self.api = MT5API()
        
        self.trade_manager = TradeManager(self.api, self.settings, self.trade_log)
        self.timings = { p: Timing(self.api.last_complete_candle(p)) for p in self.trade_pairs }
        self.log_message(f"Bot started with\n{pprint.pformat(self.settings)}")
        self.log_message(f"Bot Timings\n{pprint.pformat(self.timings)}")
        
    def log_message(self, msg):
        self.log.logger.debug(msg)       
    
    def update_timings(self):        
        for pair in self.trade_pairs:
            current = self.api.last_complete_candle(pair)
            
            
            self.timings[pair].ready = False
            if current > self.timings[pair].last_candle:
                print(current,self.timings[pair].last_candle)
                self.timings[pair].ready = True
                self.timings[pair].last_candle = current
                self.log_message(f"{pair} new candle {current}")

    def process_pairs(self):
        trades_to_make =[]   
        for pair in self.trade_pairs:
            if self.timings[pair].ready == True:
                self.log_message(f"Ready to trade {pair}")
                # trading strategy
                techs = Technicals(self.settings[pair], self.api, pair, log=self.tech_log)
                decision = techs.get_trade_decision(self.timings[pair].last_candle)
                units = decision * self.settings[pair].units
                if units != 0:
                    trades_to_make.append({'pair': pair, 'units': units,'decision':decision})
        
        if len(trades_to_make) > 0:
            # print(trades_to_make)
            self.trade_manager.place_trades(trades_to_make)
    
    def run(self):
        mt5.initialize()
        while True:
            print('update_timings()...')
            self.update_timings()
            print('process_pairs()...')
            self.process_pairs()
            print('sleep()...')
            time.sleep(SLEEP)

    

if __name__ == "__main__":
    
    
    b = TradingBot()
    b.run()


