import dataloadKuCoin as dataload
import funcs as funcs
from tickers import tickers_crypto_KuCoin

#main function

def Candle_Search (ticker):
    
    open_list, high_list, low_list, close_list = dataload.Load_HP(ticker)[0], dataload.Load_HP(ticker)[1], dataload.Load_HP(ticker)[2], dataload.Load_HP(ticker)[3]
    
    short_list = close_list[210:260]
    print(short_list)
    skeleton1 = funcs.skeleton_founder(short_list, 1, 50, 8)
    print(skeleton1)
    likelihood_dict1 = funcs.find_nature(skeleton1)[2]
    print(likelihood_dict1)
    
    short_list = close_list[246:260]
    skeleton2 = funcs.skeleton_founder(short_list, 1, 14, 2)
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