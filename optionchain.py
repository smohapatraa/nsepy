
import requests
import pandas as pd
from pandas import DataFrame

url = 'https://www.nseindia.com/api/option-chain-indices?symbol=NIFTY'


headers = {
    'user-agent':
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/128.0.0.0 Safari/537.36',
    'accept-encoding':
    'gzip, deflate, br, zstd',
    'accept-language':
    'en-US,en;q=0.9'
}

session = requests.Session()
request = session.get(url,headers=headers)
print(request)
cookies = dict(request.cookies)


def dataframe():
    response = session.get(url, headers=headers, cookies=cookies).json()
    rawdata = pd.DataFrame(response)
    rawop = pd.DataFrame(rawdata['filtered']['data']).fillna(0)
    rawdata.to_excel("rawdata.xlsx")
    data = []
    for i in range(0, len(rawop)):
        calloi = callcoi = cltp = putoi = putcoi = pltp = 0
        stp = rawop['strikePrice'][i]
        if (rawop['CE'][i] == 0):
            calloi = callcoi = 0
        else:
            calloi = rawop['CE'][i]['openInterest']
            callcoi = rawop['CE'][i]['changeinOpenInterest']
            cltp = rawop['CE'][i]['lastPrice']
        if (rawop['PE'][i] == 0):
            putoi = putcoi = 0
        else:
            putoi = rawop['PE'][i]['openInterest']
            putcoi = rawop['PE'][i]['changeinOpenInterest']
            pltp = rawop['PE'][i]['lastPrice']
        opdata = {
            'CALL OI': calloi, 'CALL CHNG OI': callcoi, 'CALL LTP': cltp, 'STRIKE PRICE': stp,
            'PUT OI': putoi, 'PUT CHNG OI': putcoi, 'PUT LTP': pltp
        }

        data.append(opdata)
    optionchain = pd.DataFrame(data)
    return optionchain


optionchain = dataframe()
optionchain.to_excel("optionchain.xlsx")



