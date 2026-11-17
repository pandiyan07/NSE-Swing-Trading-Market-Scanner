eqList = ["ABB.NS", "ACC.NS","APLAPOLLO.NS", "AUBANK.NS", "ADANIENSOL.NS", "ADANIENT.NS", "ADANIGREEN.NS", "ADANIPORTS.NS", "UNITDSPR.NS",
"ADANIPOWER.NS", "ATGL.NS", "ABCAPITAL.NS", "ABFRL.NS", "ALKEM.NS", "AMBUJACEM.NS", "APOLLOHOSP.NS", "APOLLOTYRE.NS", "ASHOKLEY.NS", 
"ASIANPAINT.NS", "ASTRAL.NS", "AUROPHARMA.NS", "DMART.NS", "AXISBANK.NS", "BSE.NS", "BAJAJ-AUTO.NS", "BAJFINANCE.NS", "BAJAJFINSV.NS", 
"BAJAJHLDNG.NS", "BALKRISIND.NS", "BANDHANBNK.NS", "BANKBARODA.NS", "BANKINDIA.NS", "MAHABANK.NS", "BERGEPAINT.NS", "BDL.NS",  
"BHARATFORG.NS", "BHEL.NS", "BPCL.NS", "BHARTIARTL.NS", "BIOCON.NS", "BOSCHLTD.NS", "BRITANNIA.NS", "CGPOWER.NS", "CANBK.NS", "CHOLAFIN.NS", 
"CIPLA.NS", "COALINDIA.NS", "COFORGE.NS", "COLPAL.NS", "CONCOR.NS", "CUMMINSIND.NS", "DLF.NS", "DABUR.NS", "DALBHARAT.NS", "DEEPAKNTR.NS", 
"DELHIVERY.NS", "DIVISLAB.NS", "DIXON.NS", "LALPATHLAB.NS", "DRREDDY.NS", "EICHERMOT.NS", "ESCORTS.NS", "NYKAA.NS", "FEDERALBNK.NS", 
"FACT.NS", "FORTIS.NS", "GAIL.NS", "GMRINFRA.NS", "GLAND.NS", "GODREJCP.NS", "GODREJPROP.NS", "GRASIM.NS", "GUJGASLTD.NS", "HCLTECH.NS", 
"HDFCAMC.NS", "HDFCBANK.NS", "HDFCLIFE.NS", "HAVELLS.NS", "HEROMOTOCO.NS", "HINDALCO.NS", "HAL.NS", "HINDPETRO.NS", "HINDUNILVR.NS", 
"ICICIBANK.NS", "ICICIGI.NS", "ICICIPRULI.NS", "IDBI.NS", "IDFCFIRSTB.NS", "ITC.NS", "INDIANB.NS", "INDHOTEL.NS", "IOC.NS", "SIEMENS.NS",
"IRFC.NS", "IGL.NS", "INDUSTOWER.NS", "INDUSINDBK.NS", "NAUKRI.NS", "INFY.NS", "INDIGO.NS", "IPCALAB.NS","JSWENERGY.NS", "JSWINFRA.NS",
"JSWSTEEL.NS", "JINDALSTEL.NS", "JIOFIN.NS", "JUBLFOOD.NS", "KPITTECH.NS", "KALYANKJIL.NS","BEL.NS","IRCTC.NS","PNB.NS","M&MFIN.NS",
"KOTAKBANK.NS", "LTF.NS", "LTTS.NS", "LICHSGFIN.NS", "LTIM.NS", "LT.NS", "LAURUSLABS.NS", "LICI.NS", "LUPIN.NS", "MRF.NS", "LODHA.NS", 
"M&M.NS", "MANKIND.NS", "MARICO.NS", "MARUTI.NS", "MFSL.NS", "MAXHEALTH.NS", "MPHASIS.NS", "NHPC.NS", "NMDC.NS", "NTPC.NS",
"NESTLEIND.NS", "OBEROIRLTY.NS", "ONGC.NS", "OIL.NS", "PAYTM.NS", "OFSS.NS", "POLICYBZR.NS", "PIIND.NS", "PAGEIND.NS", "PATANJALI.NS",
"PERSISTENT.NS", "PETRONET.NS", "PIDILITIND.NS", "PEL.NS", "POLYCAB.NS", "POONAWALLA.NS", "PFC.NS", "POWERGRID.NS", "PRESTIGE.NS", 
"RECLTD.NS", "RVNL.NS", "RELIANCE.NS", "SBICARD.NS", "SBILIFE.NS", "SJVN.NS", "SRF.NS", "MOTHERSON.NS", "SHREECEM.NS", "SHRIRAMFIN.NS", 
"SONACOMS.NS", "SBIN.NS", "SAIL.NS", "SUNPHARMA.NS", "SUNTV.NS", "SUPREMEIND.NS", "SUZLON.NS", "SYNGENE.NS", "TVSMOTOR.NS", "TATACHEM.NS",
"TATACOMM.NS", "TCS.NS", "TATACONSUM.NS", "TATAELXSI.NS", "TATAMTRDVR.NS", "TATAMOTORS.NS", "TATAPOWER.NS", "TATASTEEL.NS", "TATATECH.NS",
"TECHM.NS", "TITAN.NS", "TORNTPHARM.NS", "TORNTPOWER.NS", "TRENT.NS", "TIINDIA.NS", "UPL.NS", "ULTRACEMCO.NS", "UNIONBANK.NS", "ZYDUSLIFE.NS",
"VBL.NS", "VEDL.NS", "IDEA.NS", "VOLTAS.NS", "WIPRO.NS", "YESBANK.NS", "ZEEL.NS", "ZOMATO.NS", "MAZDOCK.NS"]


from jugaad_data.nse import NSELive
import multiprocessing
import time
import sys
from datetime import datetime
from nselib import capital_market
import yfinance as yf
import pandas as pd


date_volume_dict = {}

current_process = multiprocessing.current_process()
process_name = current_process.name
event = multiprocessing.Event()

try:
  n = NSELive()
except Exception as e:
  print ('\n\n',repr(e))
  print ('There is NO INTERNET CONNECTION...!!')
  sys.exit(1)

def JUGAAD_DATA(n,lock,jg_stock_quote,eq,Stock_jg,l):
  def FETCHER(n,eq,l):
    l+=1
    try:
      jg_data = n.stock_quote(eq)
      return jg_data
    except Exception as e:
      print ('\n\n',repr(e))
      print ('\n\nERROR = Couldnt reach the NSE server for the STOCK QUOTE,\nSo retrying again to fetch the data...')
      if l < 5:
        FETCHER(n,eq,l)
  
  jg_data = FETCHER(n,eq,l)
  
  #q['priceInfo']['weekHighLow']  =  {'min': 543.2, 'minDate': '26-Oct-2023', 'max': 912, 'maxDate': '03-Jun-2024', 'value': 839.2}
  
  try:
    with lock:
      Stock_jg.append(jg_data['info']['symbol'])
      jg_stock_quote.update({jg_data['info']['symbol']:jg_data['priceInfo']['weekHighLow']})
  except Exception as e:
    print ('\n\n',repr(e))
    print (f' ERROR = The Stock {eq} data is not available.....!!')
    print ('So appending all the fetched values as 0')
    print ('\n\n')
    with lock:
      Stock_jg.append(eq)
      jg_stock_quote.update({eq:0})
  
  event.set()    #1
  return True

def ORB(eq,event,yf_close_list,jg_stock_quote,lock,orb,orb_min_max_date):
  curr_price = yf_close_list[-1]
  price_info = jg_stock_quote[eq]
  idLow = float(price_info['min'])
  idHigh = float(price_info['max'])

  if curr_price > 0:
    a = curr_price - idLow 
    b = idHigh - idLow
    c = ((b-a)/b)*100
    if c > 50:
      orb_perc = round(100 - c,1)
      orb_date = str(f"{price_info['maxDate']} maxDate") 
    else:
      orb_perc = round(c,1)
      orb_date = str(f"{price_info['minDate']} minDate") 
  else:
    orb_perc = 100
    orb_date = 0
    
  with lock:
    orb.append(orb_perc)
    orb_min_max_date.append(orb_date)
  
  event.set()    #2
  return True



def DATA_FETCHER(eq,yf_close_list,lock,jg_stock_quote,Stock_jg,orb,orb_min_max_date):
  l = 0
  
  '''    JUGAAD DATA    '''
  JUGAAD_DATA(n,lock,jg_stock_quote,eq.replace(".NS", ""),Stock_jg,l)       # Jugaad data downloading
  event.wait()    #1
  
  '''    ORB    '''
  ORB(eq.replace(".NS", ""),event,yf_close_list,jg_stock_quote,lock,orb,orb_min_max_date)
  event.wait()    #2
  
  return True


def OUTPUT_CALCULATOR(o,avg,tf,l,eqname,eq,Stock_vol_spike,date_and_time,total_quantity,volume_avg,times_of_spike,time_frame_list,lock):
  x = date_volume_dict[o]

  with lock:
    Stock_vol_spike.append(eq)
    time_frame_list.append(tf)
    date_and_time.append(x[1])
    total_quantity.append(f'{x[0]:,}')
    volume_avg.append(avg)
    times_of_spike.append(round(x[0]/avg,2))
  


def ABNORMAL_VOLUME_FINDER(tfd,market_open_days,remaining_days,yf_vol_list,tf,eqname,eq,lock,
                        Stock_vol_spike,date_and_time,total_quantity,volume_avg,times_of_spike,time_frame_list):
  a = len(yf_vol_list)            # indexing the list items
  l = 0

  for v in range(0,tfd):       # First week/month and then looping on further one by one, one at a time
    time_frame_data = []
    for b in range(a-market_open_days,a):   
      x = date_volume_dict[b]
      time_frame_data.append(x[0])
    
    avg = sum(time_frame_data) / market_open_days 
    #print ('timefraeme original = ',time_frame_data)
    #print ('week/month = ',v)
    for b in range(a-market_open_days,a):
      #print ('b =',b)
      x = date_volume_dict[b]
      if x[0] > 3*avg:
        OUTPUT_CALCULATOR(b,round(avg,2),tf,l,eqname,eq,Stock_vol_spike,date_and_time,total_quantity,volume_avg,times_of_spike,time_frame_list,lock)
        l+=1
    a-=market_open_days

  if remaining_days != 0:
    for v in range(0,remaining_days):
      time_frame_data = []
      x = date_volume_dict[v]
      time_frame_data.append(x[0])
    
    avg = sum(time_frame_data) / len(time_frame_data)
    #print ('timefraeme remaining = ',time_frame_data)
    for v in range(1,remaining_days):
      x = date_volume_dict[v]
      if x[0] > 3*avg:
        #print('remaining')
        OUTPUT_CALCULATOR(v,round(avg,2),tf,l,eqname,eq,Stock_vol_spike,date_and_time,total_quantity,volume_avg,times_of_spike,time_frame_list,lock)
        l+=1
  l = 0

def WEEKLY_AVERAGE(yf_vol_list,eqname,eq,Stock_vol_spike,date_and_time,total_quantity,volume_avg,times_of_spike,lock,time_frame_list):
  market_open_days = 5
  weeks = len(yf_vol_list) // market_open_days
  remaining_days = len(yf_vol_list) % market_open_days
  tf = 'weekly'
  ABNORMAL_VOLUME_FINDER(weeks,market_open_days,remaining_days,yf_vol_list,tf,eqname,eq,lock,
                        Stock_vol_spike,date_and_time,total_quantity,volume_avg,times_of_spike,time_frame_list)


def MONTHLY_AVERAGE(yf_vol_list,eqname,eq,Stock_vol_spike,date_and_time,total_quantity,volume_avg,times_of_spike,lock,time_frame_list):
  market_open_days = 21
  months = len(yf_vol_list) // market_open_days
  remaining_days = len(yf_vol_list) % market_open_days
  tf = 'monthly'
  ABNORMAL_VOLUME_FINDER(months,market_open_days,remaining_days,yf_vol_list,tf,eqname,eq,lock,
                        Stock_vol_spike,date_and_time,total_quantity,volume_avg,times_of_spike,time_frame_list)

def ONE_DATA_DOWNLOADER(eqList,p,d,event):
  yf_all_stocks_data = yf.download(eqList, group_by='Ticker', period=p, interval=d)    # yfdata fetching
  event.set()    #3
  return yf_all_stocks_data

def THE_MAIN(start,end,Stock_block,Stock_bulk,Stock_jg,lock,orb,eqList,event,n,jg_stock_quote,volume_sum_block_eqi,
            block_date_list,volume_sum_bulk_eqi,bulk_date_list,block_deal_df,bulk_deal_df,orb_min_max_date,
            Stock_vol_spike,date_and_time,total_quantity,volume_avg,times_of_spike,time_frame_list):
  yf_all_stocks_data = ONE_DATA_DOWNLOADER(eqList,'1mo','1d',event)
  event.wait()    #3
  
  for i in range(start, end):
    
    '''    YF DATA    '''
    stock_df = yf_all_stocks_data[(eqList[i])]
    yf_vol_list = stock_df[('Volume')].tolist()
    yf_date_list = stock_df.index.tolist()
    yf_close_list = stock_df[('Close')].tolist()
    DATA_FETCHER(eqList[i],yf_close_list,lock,jg_stock_quote,Stock_jg,orb,orb_min_max_date)


    '''    JUGAAD DATA VOLUME SPIKE CALCULATOR    '''
    for vd in range(len(yf_date_list)):
      date_volume_dict.update({vd:[yf_vol_list[vd],yf_date_list[vd]]})
    
    eqname = 0
    WEEKLY_AVERAGE(yf_vol_list,eqname,eqList[i].replace(".NS", ""),Stock_vol_spike,date_and_time,total_quantity,volume_avg,times_of_spike,lock,time_frame_list)
    MONTHLY_AVERAGE(yf_vol_list,eqname,eqList[i].replace(".NS", ""),Stock_vol_spike,date_and_time,total_quantity,volume_avg,times_of_spike,lock,time_frame_list)
    
    
    
    '''    BLOCK VOLUME CALCULATOR    '''
    df_block_eqi = block_deal_df[block_deal_df['Symbol'] == eqList[i].replace(".NS", "")]
    df_block_buy = df_block_eqi[df_block_eqi['Buy/Sell'] == 'BUY']
    df_block_sell = df_block_eqi[df_block_eqi['Buy/Sell'] == 'SELL']
    
    num_of_block_buy_rows = len(df_block_buy)
    num_of_block_sell_rows = len(df_block_sell)
    
    if num_of_block_buy_rows < num_of_block_sell_rows:
      df_block_buy_sell = df_block_buy
    else:
      df_block_buy_sell = df_block_sell
      
    if df_block_buy_sell.empty:
      pass
    else:
      if eqList[i].replace(".NS", "") not in Stock_block:
        Stock_block.append(eqList[i].replace(".NS", ""))
        volume_sum_block_eqi.append(df_block_buy_sell['QuantityTraded'].sum())
        block_date_list.append(df_block_buy_sell[('Date')].tolist())
        #block_buy_sell = df_block_eqi[('Buy/Sell')].tolist()
    
    
    '''    BULK VOLUME CALCULATOR    '''
    df_bulk_eqi = bulk_deal_df[bulk_deal_df['Symbol'] == eqList[i].replace(".NS", "")] 
    df_bulk_buy = df_bulk_eqi[df_bulk_eqi['Buy/Sell'] == 'BUY']
    df_bulk_sell = df_bulk_eqi[df_bulk_eqi['Buy/Sell'] == 'SELL']
    
    num_of_bulk_buy_rows = len(df_bulk_buy)
    num_of_bulk_sell_rows = len(df_bulk_sell)
    
    if num_of_bulk_buy_rows < num_of_bulk_sell_rows:
      df_bulk_buy_sell = df_bulk_buy
    else:
      df_bulk_buy_sell = df_bulk_sell
    
    if df_bulk_buy_sell.empty:
      pass
    else:
      if eqList[i].replace(".NS", "") not in Stock_bulk:
        Stock_bulk.append(eqList[i].replace(".NS", ""))
        volume_sum_bulk_eqi.append(df_bulk_buy_sell['QuantityTraded'].sum())
        bulk_date_list.append(df_bulk_buy_sell[('Date')].tolist())
        #bulk_buy_sell = df_bulk_eqi[('Buy/Sell')].tolist()



if __name__ == '__main__':
    multiprocessing.freeze_support()
    manager = multiprocessing.Manager()
    
    print ('\n\nthe code has started to run.......')
    
    orb = manager.list()
    orb_min_max_date = manager.list()
    Stock_block = manager.list()
    Stock_bulk = manager.list()
    Stock_jg = manager.list()
    last_three_volume = manager.list()
    volume_sum_block_eqi = manager.list()
    volume_sum_bulk_eqi = manager.list()
    block_date_list = manager.list()
    bulk_date_list = manager.list()
    Stock_vol_spike = manager.list()
    date_and_time = manager.list()
    total_quantity = manager.list()
    volume_avg = manager.list()
    times_of_spike = manager.list()
    time_frame_list = manager.list()
    
    jg_stock_quote = manager.dict()
    
    lock = manager.Lock()
    
    processes = []

    l=0
    def FETCHER(l):
      l+=1
      try:
        '''    NSE LIBRARY    '''
        block_deal_df = capital_market.block_deals_data(period='1W')   # from_date=start_date, to_date=end_date
        bulk_deal_df = capital_market.bulk_deal_data(period='1W')     # from_date=start_date, to_date=end_date
        return block_deal_df,bulk_deal_df
      except Exception as e:
        print ('\n\n',repr(e))
        print ('\n\nERROR = Couldnt reach the NSE server for the STOCK QUOTE,\nSo retrying again to fetch the data...')
        if l < 5:
          FETCHER(l)
  
    block_deal_df,bulk_deal_df = FETCHER(l)
    # Remove commas and convert to integer using errors='coerce' to handle non-numeric values
    block_deal_df['QuantityTraded'] = pd.to_numeric(block_deal_df['QuantityTraded'].str.replace(',', ''), errors='coerce')
    bulk_deal_df['QuantityTraded'] = pd.to_numeric(bulk_deal_df['QuantityTraded'].str.replace(',', ''), errors='coerce')
    print ('block & bulk deal data in capital_market from the nselib has been downloaded')
    
    i=0
    num_processor_cores = multiprocessing.cpu_count()
    chunk_size = len(eqList) // num_processor_cores
    
    for i in range(num_processor_cores):            
      start = i * chunk_size
      end = start + chunk_size if i < num_processor_cores - 1 else len(eqList)
      
      data_processing_process = multiprocessing.Process(
          target=THE_MAIN,                         # APPENDER.py file
          args=(start,end,Stock_block,Stock_bulk,Stock_jg,lock,orb,eqList,event,n,jg_stock_quote,volume_sum_block_eqi,
                block_date_list,volume_sum_bulk_eqi,bulk_date_list,block_deal_df,bulk_deal_df,orb_min_max_date,
                Stock_vol_spike,date_and_time,total_quantity,volume_avg,times_of_spike,time_frame_list))
      processes.append(data_processing_process)
      data_processing_process.start()

    for process in processes:
      process.join()
    
    block_deal_dict = {}
    bulk_deal_dict = {}
    volume_spike_dict = {}
    orb_dict = {}
    
    '''    BLOCK DEAL    '''
    block_deal_dict.update({'Stock':list(Stock_block)})
    block_deal_dict.update({'Traded quantity':list(volume_sum_block_eqi)})
    block_deal_dict.update({'Date':list(block_date_list)})
    blockd_df = pd.DataFrame(block_deal_dict)
    blockd_df = blockd_df.reset_index(drop=True)
    blockd_df = blockd_df.set_index('Stock')
    print ('\nMy BLOCK DEAL dataframe =')
    print (blockd_df)
    
    '''    BULK DEAL   ''' 
    bulk_deal_dict.update({'Stock':list(Stock_bulk)})
    bulk_deal_dict.update({'Traded quantity':list(volume_sum_bulk_eqi)})
    bulk_deal_dict.update({'Date':list(bulk_date_list)}) 
    
    bulkd_df = pd.DataFrame(bulk_deal_dict)
    bulkd_df = bulkd_df.reset_index(drop=True)
    bulkd_df = bulkd_df.set_index('Stock')
    print ('\nMy BULK DEAL dataframe =')
    print (bulkd_df)
    
    '''    ORB   ''' 
    orb_dict.update({'Stock':list(Stock_jg)})
    orb_dict.update({'ORB %':list(orb)})
    orb_dict.update({'ORB Date':list(orb_min_max_date)})
    
    orb_df = pd.DataFrame(orb_dict)
    orb_df = orb_df.sort_values(by='ORB %', ascending=True)
    orb_df = orb_df.iloc[:10]
    orb_df['ORB %'] = [f"{perc} %" for perc in orb_df['ORB %']]
    orb_df = orb_df.reset_index(drop=True)
    orb_df = orb_df.set_index('Stock')
    print ('\nORB dataframe =')
    print (orb_df)
    
    
    '''    VOLUME SPIKE    ''' 
    volume_spike_dict.update({'Stock':list(Stock_vol_spike)})
    volume_spike_dict.update({'Date & Time':list(date_and_time)})
    volume_spike_dict.update({'Total Quantity':list(total_quantity)})
    volume_spike_dict.update({'Avg vol':list(volume_avg)})
    volume_spike_dict.update({'Time frame':list(time_frame_list)})
    volume_spike_dict.update({'Times of Spike':list(times_of_spike)})
    
    
    volume_spike_df = pd.DataFrame(volume_spike_dict)
    volume_spike_df = volume_spike_df.sort_values(by='Times of Spike', ascending=False)
    volume_spike_df['Times of Spike'] = [f"{perc} times" for perc in volume_spike_df['Times of Spike']]
    volume_spike_df = volume_spike_df.reset_index(drop=True)
    volume_spike_df = volume_spike_df.set_index('Stock')
    volume_spike_weekly_df = volume_spike_df[volume_spike_df['Time frame'] == 'weekly']
    volume_spike_monthly_df = volume_spike_df[volume_spike_df['Time frame'] == 'monthly']
    
    print ('\nVolume Spike WEEKLY dataframe =')
    print (volume_spike_weekly_df.iloc[:50])
    print ('\nVolume Spike MONTHLY dataframe =')
    print (volume_spike_monthly_df.iloc[:50])
