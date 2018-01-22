import requests
import json
import twitter

# zaif btc
res = requests.get('https://api.zaif.jp/api/1/ticker/btc_jpy')
root = res.json()
btc = root["last"]
sbtc = str(btc)

# zaif eth

re = requests.get('https://api.zaif.jp/api/1/ticker/eth_jpy')
roo = re.json()
eth = roo["last"]
seth = str(eth)



# binance btc

params = {"symbol":"XRPBTC"}
a = requests.get('https://api.binance.com/api/v3/ticker/price', params=params)
a = a.json()
a = a["price"]
a = float(a)
aa = btc * a
aa = "%.2f" % aa


## float
print(aa)

# end

## binance eth
params = {"symbol":"XRPETH"}
b = requests.get('https://api.binance.com/api/v3/ticker/price', params=params)
b = b.json()
b = b["price"]
b = float(b)
bb = eth * b
bb = "%.2f" % bb

## float
print(bb)

# end

# poloniex
d = requests.get('https://poloniex.com/public?command=returnTicker')
d = d.json()
d = d['BTC_XRP']['last']
d = float(d)
dd = btc * d
dd = "%.2f" % dd

## float
print(dd)
## end

# Hitbtc
c = requests.get('https://api.hitbtc.com/api/1/public/XRPBTC/ticker')
c = c.json()
c = c['last']
c = float(c)
cc = btc * c
cc = "%.2f" % cc

print(cc)


# まとめ

title = "【 $XRP 価格差 】"
Binance = "https://goo.gl/Z26zsC"
titleb = "【Binance登録はこちらから】"
HitBTC = "https://goo.gl/KcwRgZ"
titleh = "【HitBTC登録はこちらから】"

status = "%s\n" % title \
               + "Binance(BTC)  ¥%s\n" % aa \
               + "%s\n" % a \
               + "Binance(ETH)  ¥%s\n" % bb \
               + "%s\n" % b \
               + "Poloniex(BTC) ¥%s\n" % dd \
               + "%s\n" % d \
               + "HitBTC(BTC)   ¥%s\n" % cc \
               + "%s\n" % c \
               + "%s\n" % titleh \
               + "%s\n" % HitBTC 

print(status)


