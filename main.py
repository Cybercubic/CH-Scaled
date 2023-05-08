import dataloadKuCoin as dataload
import funcs as funcs
from tickers import tickers_crypto_KuCoin

#main function

def Candle_Search (ticker):
    
    open_list, high_list, low_list, close_list = dataload.Load_HP(ticker)[0], dataload.Load_HP(ticker)[1], dataload.Load_HP(ticker)[2], dataload.Load_HP(ticker)[3]
    
    timeframe1 = 100
    short_list1 = close_list[(260-timeframe1):260]
    print(short_list1)
    end_price, start_price, step = funcs.timeframe_slice(timeframe1)
    #print(end_price, start_price, step)
    skeleton1 = funcs.skeleton_founder(short_list1, end_price, start_price, step)
    likelihood_dict1 = funcs.find_nature(skeleton1)[2]
    print(likelihood_dict1)
    
    timeframe2 = 20
    short_list2 = close_list[(260-timeframe2):260]
    print(short_list2)
    end_price, start_price, step = funcs.timeframe_slice(timeframe2)
    #print(end_price, start_price, step)
    skeleton2 = funcs.skeleton_founder(short_list2, end_price, start_price, step)
    likelihood_dict2 = funcs.find_nature(skeleton2)[2]
    print(likelihood_dict2)
    
    my_array = funcs.pl_preprocessing(open_list, high_list, low_list, close_list)
    
    isto_array = funcs.make_isto(my_array)
    
    emotion_array = funcs.final_isto(isto_array)
    
    k = funcs.calculate_k(likelihood_dict1, likelihood_dict2, emotion_array)
    
    result = [k, ticker]
    
    return result

ticker_list = tickers_crypto_KuCoin

top_dict = {}

for ticker in ticker_list:
    try:
        a = Candle_Search(ticker)
        print(a)
        
        dict_score = a[0]
        dict_ticker = a[1]
        
        top_dict[dict_ticker] = round(dict_score, 2)
    
    except Exception:
        print(ticker, '- NOPE')
        
top_dict = sorted(top_dict.items(), key=lambda x:x[1], reverse=True)

print(top_dict)