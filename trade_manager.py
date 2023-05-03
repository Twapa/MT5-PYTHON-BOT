import MetaTrader5 as mt5
class TradeManager():

    def __init__(self, api, settings, log=None):
        self.api = api
        self.log = log
        self.settings = settings

    def log_message(self, msg):
        if self.log is not None:
            self.log.logger.debug(msg)
            
    def close_trades(self, pairs_to_close):
        
        positions = mt5.positions_get()
        for pos in positions:
            tick = mt5.symbol_info_tick(pos.symbol)
            type_dict = {0: 1, 1: 0}  # 0 represents buy, 1 represents sell - inverting order_type to close the position
            price_dict = {0: tick.ask, 1: tick.bid}

            
            request = {
                "action": mt5.TRADE_ACTION_DEAL,
                "position": pos.ticket,
                "symbol": pos.symbol,
                "volume": pos.volume,
                "type": type_dict[pos.type],
                "price": price_dict[pos.type],
                # "deviation": DEVIATION,
                "magic": 100,
                "comment": "python close order",
                "type_time": mt5.ORDER_TIME_GTC,
                "type_filling": mt5.ORDER_FILLING_IOC,
            }

            order_result = mt5.order_send(request)
        

            self.log_message(f"TradeManager:closed_trade pairs_to_close:{order_result} ")

            


        

    def create_trades(self, trades_to_make):
        volume = 1.0
        for t in trades_to_make:
            
            tick = mt5.symbol_info_tick(t['pair'])
            
            order_dict = {1: 0, -1: 1}
            price_dict = {1: tick.ask, -1: tick.bid}

            request = {
                "action": mt5.TRADE_ACTION_DEAL,
                "symbol": t['pair'],
                "volume": volume,
                "type": order_dict[t['decision']],
                "price": price_dict[t['decision']],
                # "deviation": DEVIATION,
                "magic": 100,
                "comment": "python market order",
                "type_time": mt5.ORDER_TIME_GTC,
                "type_filling": mt5.ORDER_FILLING_IOC,
            }

            order_result = mt5.order_send(request)
            self.log_message(f"TradeManager:Opened {order_result} ")
            

        # return order_result


        
        # for t in trades_to_make:
        #     trade_id = self.api.place_trade(t['pair'], t['units'])
        #     if trade_id is not None:
        #         self.log_message(f"TradeManager:Opened {trade_id} {t}")
        #     else:
        #         self.log_message(f"TradeManager:FAILED TO OPEN {t}")
            
    def place_trades(self, trades_to_make):

        self.log_message(f"TradeManager:place_trades() {trades_to_make}")
        pairs = [x['pair'] for x in trades_to_make]

        pairs = [x['pair'] for x in trades_to_make]
        self.close_trades(pairs)

        self.create_trades(trades_to_make)

        



        self.log_message(f"TradeManager:place_trades() {trades_to_make}")
        pairs = [x['pair'] for x in trades_to_make]
        self.close_trades(pairs)
        self.create_trades(trades_to_make)