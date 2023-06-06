import dataloadKuCoin as dataload
import funcs as funcs
import tickers as tickers

#main function

def Candle_Search (ticker):
    
    open_list, high_list, low_list, close_list = dataload.Load_HP(ticker)[0], dataload.Load_HP(ticker)[1], dataload.Load_HP(ticker)[2], dataload.Load_HP(ticker)[3]
    
    anomaly_eval = funcs.anomaly_eval(dataload.Load_HP(ticker), 25, 1)
    
    timeframe1 = 100
    short_list1 = close_list[(260-timeframe1):260]
    print(short_list1)
    end_price, start_price, step = funcs.timeframe_slice(timeframe1)
    skeleton1 = funcs.skeleton_founder(short_list1, end_price, start_price, step)
    print(skeleton1)
    likelihood_dict1 = funcs.find_nature(skeleton1)[2]
    
    timeframe2 = 20
    short_list2 = close_list[(260-timeframe2):260]
    print(short_list2)
    end_price, start_price, step = funcs.timeframe_slice(timeframe2)
    skeleton2 = funcs.skeleton_founder(short_list2, end_price, start_price, step)
    likelihood_dict2 = funcs.find_nature(skeleton2)[2]
    
    my_array = funcs.pl_preprocessing(open_list, high_list, low_list, close_list)
    
    isto_array = funcs.make_isto(my_array)
    
    emotion_array = funcs.final_isto(isto_array)
    
    k = funcs.calculate_k(likelihood_dict1, likelihood_dict2, emotion_array)
    
    result = {}
    
    result['ticker'] = ticker
    result['k'] = k
    result['invest'] = emotion_array[260, 0]
    result['speculative'] = emotion_array[260, 1]
    result['tension'] = emotion_array[260, 2]
    result['optimism'] = emotion_array[260, 3]
    result['anomaly_eval'] = anomaly_eval
    result.update(likelihood_dict1)
    
    #print(result)
    print(ticker, k, anomaly_eval)
    
    return result

ticker_list = tickers.tickers_crypto_KuCoinAll
result_list = []

#making list with analysis

def assets_analysis(ticker_list):

    for ticker in ticker_list:
        try:
            a = Candle_Search(ticker)
            result_list.append(a)
    
        except Exception:
            print(ticker, '- NOPE')
            
    return result_list
            
result_list = assets_analysis(ticker_list)
#print(result_list)