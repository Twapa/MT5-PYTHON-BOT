import json

class Settings():
    def __init__(self, pair, units, short_ma, long_ma):
        self.pair = pair
        self.units = units
        self.short_ma = short_ma
        self.long_ma = long_ma

    def __repr__(self):
        return str(vars(self))
    
    @classmethod
    def from_file_ob(cls, ob):
        return Settings(ob['pair'],ob['units'],ob['short_ma'],ob['long_ma'])
    
    @classmethod
    def load_settings(cls):
        data = json.loads(open('settings.json', 'r').read())
        return { k:cls.from_file_ob(v) for k,v in data.items() }
    
    @classmethod
    def get_pairs(cls):
        return list(cls.load_settings().keys())

if __name__ == "__main__":
    [print(k,v) for k,v in Settings.load_settings().items()]
    print(Settings.get_pairs())

    # "GBPJPY" :  { "pair" :  "GBPJPY", "units": 1000, "short_ma": 2, "long_ma": 8 },
    # "AUDUSD" :  { "pair" :  "AUDUSD", "units": 1000, "short_ma": 2, "long_ma": 8 },
    # "GBPUSD" :  { "pair" :  "GBPUSD", "units": 1000, "short_ma": 2, "long_ma": 8 },
    # "EURCHF" :  { "pair" :  "EURCHF", "units": 1000, "short_ma": 2, "long_ma": 8 },
    # "EURGBP" :  { "pair" :  "EURGBP", "units": 1000, "short_ma": 2, "long_ma": 8 }