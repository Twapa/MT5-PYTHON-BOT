import datetime as dt
from dateutil.parser import *

def time_utc():
    # t =dt.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    tm =parse(dt.datetime.now().strftime('%Y-%m-%d %H:%M')) + dt.timedelta(hours=3)
    # t = dt.datetime.utcnow().replace(tzinfo=dt.timezone.utc)
    return tm

def get_utc_dt_from_string(date_str):
    d = parse(date_str)
    return d.replace()

if __name__ == "__main__":
    t =parse(dt.datetime.now().strftime('%Y-%m-%d %H:%M')) + dt.timedelta(hours=1)
    
    # tm =dt.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    

    print(t)
    # print(tm)
    