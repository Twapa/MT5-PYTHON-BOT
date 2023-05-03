from utils import get_utc_dt_from_string, time_utc
import datetime as dt

class Timing():
    def __init__(self, last_candle):
        self.last_candle = last_candle
        if last_candle is None:
            self.last_candle = time_utc()  - dt.timedelta(minutes=1)
        self.ready = False
        
    def __repr__(self):
        return str(vars(self))
