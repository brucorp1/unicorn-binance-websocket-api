#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# File: dev_test_full.py
#
# Part of ‘UNICORN Binance WebSocket API’
# Project website: https://github.com/unicorn-data-analysis/unicorn-binance-websocket-api
# Documentation: https://www.unicorn-data.com/unicorn-binance-websocket-api.html
# PyPI: https://pypi.org/project/unicorn-binance-websocket-api/
#
# Author: UNICORN Data Analysis
#         https://www.unicorn-data.com/
#
# Copyright (c) 2019, UNICORN Data Analysis
# All rights reserved.
#
# Permission is hereby granted, free of charge, to any person obtaining a
# copy of this software and associated documentation files (the
# "Software"), to deal in the Software without restriction, including
# without limitation the rights to use, copy, modify, merge, publish, dis-
# tribute, sublicense, and/or sell copies of the Software, and to permit
# persons to whom the Software is furnished to do so, subject to the fol-
# lowing conditions:
#
# The above copyright notice and this permission notice shall be included
# in all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS
# OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABIL-
# ITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT
# SHALL THE AUTHOR BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY,
# WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS
# IN THE SOFTWARE.

from unicorn_binance_websocket_api.unicorn_binance_websocket_api_manager import BinanceWebSocketApiManager
import logging
import time
import threading
import os

# https://docs.python.org/3/library/logging.html#logging-levels
logging.basicConfig(filename=os.path.basename(__file__) + '.log')
logging.getLogger('websockets').addHandler(logging.StreamHandler())
logging.getLogger('websockets').setLevel(logging.ERROR)

# create instance of BinanceWebSocketApiManager and catch every unhandled error and log
try:
    binance_websocket_api_manager = BinanceWebSocketApiManager()
except Exception:
    logging.critical("ATTENTION! Unexpected error", exc_info=True)


ticker_all_stream_id = binance_websocket_api_manager.create_stream(["arr"], ["!ticker"])
miniticker_stream_id = binance_websocket_api_manager.create_stream(["arr"], ["!miniTicker"])
userdata_stream_id = binance_websocket_api_manager.create_stream(["arr"], ["!userData"])
markets = {'bnbbtc'}
aggtrade_stream_id = binance_websocket_api_manager.create_stream(["aggTrade"], markets)
trade_stream_id = binance_websocket_api_manager.create_stream(["trade"], markets)
kline_1m_stream_id = binance_websocket_api_manager.create_stream(["kline_1m"], markets)
ticker_bnbbtc_stream_id = binance_websocket_api_manager.create_stream(["ticker"], markets)
miniticker_stream_id = binance_websocket_api_manager.create_stream(["miniTicker"], markets)
kline_5m_stream_id = binance_websocket_api_manager.create_stream(["kline_5m"], markets)
depth5_stream_id = binance_websocket_api_manager.create_stream(["depth10"], markets)
depth_stream_id = binance_websocket_api_manager.create_stream(["depth"], markets)
markets = {'xrpusdt', 'rvnbtc', 'ltcusdt', 'adausdt', 'eosusdt', 'neousdt'}
aggtrade_stream_id = binance_websocket_api_manager.create_stream(["aggTrade"], markets)
trade_stream_id = binance_websocket_api_manager.create_stream(["trade"], markets)
kline_1m_stream_id = binance_websocket_api_manager.create_stream(["kline_1m"], markets)
ticker_bnbbtc_stream_id = binance_websocket_api_manager.create_stream(["ticker"], markets)
miniticker_stream_id = binance_websocket_api_manager.create_stream(["miniTicker"], markets)
kline_5m_stream_id = binance_websocket_api_manager.create_stream(["kline_5m"], markets)
depth5_stream_id = binance_websocket_api_manager.create_stream(["depth5"], markets)
depth_stream_id = binance_websocket_api_manager.create_stream(["depth"], markets)
channels = {'trade', 'kline_1', 'kline_5', 'kline_15', 'kline_30', 'kline_1h', 'kline_12h', 'kline_1w',
                'miniTicker', 'depth20', '!miniTicker', '!ticker'}
multi_multi_stream_id = binance_websocket_api_manager.create_stream(channels, markets)


def print_stream_data_from_stream_buffer(binance_websocket_api_manager):
    print("waiting 30 seconds, then we start flushing the stream_buffer")
    time.sleep(30)
    while True:
        oldest_stream_data_from_stream_buffer = binance_websocket_api_manager.pop_stream_data_from_stream_buffer()
        if oldest_stream_data_from_stream_buffer is False:
            time.sleep(0.01)
        else:
            try:
                # remove # to activate the print function:
                #print(oldest_stream_data_from_stream_buffer)
                pass
            except Exception:
                # not able to process the data? write it back to the stream_buffer
                binance_websocket_api_manager.add_to_stream_buffer(oldest_stream_data_from_stream_buffer)


# start a worker process to move the received stream_data from the stream_buffer to a print function
worker_thread = threading.Thread(target=print_stream_data_from_stream_buffer, args=(binance_websocket_api_manager,))
worker_thread.start()

# show an overview
while True:
    binance_websocket_api_manager.print_summary()
    time.sleep(1)