#/usr/bin/env python
# vim: set fileencoding=utf-8

import urllib2
from bs4 import BeautifulSoup

'''
---------------------------------------------------------------
 Target: 
   종목 코드를 입력으로 받아 종가, 거래량 등을
   리턴한다.
   
 종근당 홀딩스
 http://finance.naver.com/item/main.nhn?code=001630 종합정보
 http://finance.naver.com/item/sise.nhn?code=001630 시셰
---------------------------------------------------------------
'''

# 기아차	유아이디	인포바인	현대홈쇼핑	미원에스씨	
# 아트라스BX	피제이전자	녹십자	        잉크테크*	종근당홀딩스	
# 아이원스*	데브시스터즈*	코스맥스비티아이	에이씨티*	메디아나*
codes = ['000270', '069330', '115310', '057050', '107590',
         '023890', '006140', '006280', '049550', '001630', 
         '114810', '194480', '044820', '138360', '041920']

def get_info(code):
    """
    Get information of price and trading amount for today
    """

    response = urllib2.urlopen('http://finance.naver.com/item/main.nhn?code=%s' %code)
    html = response.read()

    perf = []

    # automatic encoding!
    soup = BeautifulSoup(html)

    #######################
    # get price for today
    #######################
    today = soup.find('div', {'class': 'today'})
    price_today = today.find_next('span').text.strip()
    perf.append(price_today)

    #######################
    # get the amount of trading for today
    #######################
    today = soup.find('span', {'class': 'sptxt sp_txt9'})
    trade_today = today.find_next('span').text.strip()
    perf.append(trade_today)

    return perf


if __name__ == "__main__":
    prices = [];
    trades = [];
    for code in codes:
        ret = get_info(code)
        prices.append(ret[0]);
        trades.append(ret[1]);

    ########################################
    # TAB(\t)을 이용하면 spreadsheet에 붙여넣을 때 
    # 자동으로 셀별로 입력이 된다.
    ########################################
    for price in prices:
        print("%s\t" %price), 

    print ""

    for trade in trades:
        print("%s\t" %trade), 

    print ""
