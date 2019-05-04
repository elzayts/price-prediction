import requests
from bs4 import BeautifulSoup
import pandas as pd

def get_html(url):
    res = requests.get(url)
    return res.text

def get_links(html):
    soup=BeautifulSoup(html, 'lxml')
    titles = soup.find('div', class_ = 'col-md-8').find_all('h2', class_ =  'catalog-item__title')
    links = []
    for title in titles:
        a = title.find('a').get('href')
        links.append('https://rieltor.ua'+a)
    return links

def get_price(html):
    soup=BeautifulSoup(html, 'lxml')
    try:
        prriice = soup.find('div', class_='ov-price')
    except:
        prriice = ''
        
    price = prriice.text
    price = price.replace(' ', '')
    value = price.split('\n')#список вартість + валюта
    return value

    
def get_type_house(html):
    url = 'https://rieltor.ua/flats-sale/'
    soup=BeautifulSoup(html, 'lxml')    
    try:
        all_params = soup.find('dl', class_ = 'ov-params-list')
    except:
        all_params = ''
    all_params = all_params.text
    all_params = all_params.replace(' ','')
    alp = all_params.split('\n')
    alp = [x for x in alp if x != '']
    leng_list = len(alp)
    try:
        type_house = alp[alp.index('Типдома:', 0, leng_list)+1]
    except:
        type_house = ''
    return type_house
def get_state(html):
    url = 'https://rieltor.ua/flats-sale/'
    soup=BeautifulSoup(html, 'lxml')    
    try:
        all_params = soup.find('dl', class_ = 'ov-params-list')
    except:
        all_params = ''
    all_params = all_params.text
    all_params = all_params.replace(' ','')
    alp = all_params.split('\n')
    alp = [x for x in alp if x != '']
    leng_list = len(alp)
    
   
    try:
        state = alp[alp.index('Состояние:', 0, leng_list)+1]
    except:
        state = ''
    return state
def get_rooms(html):
    soup=BeautifulSoup(html, 'lxml')    
    try:
        all_params = soup.find('dl', class_ = 'ov-params-list')
    except:
        all_params = ''
    all_params = all_params.text
    all_params = all_params.replace(' ','')
    alp = all_params.split('\n')
    alp = [x for x in alp if x != '']
    leng_list = len(alp)
    
    try:
        rooms = alp[alp.index('Комнаты:', 0, leng_list)+1][0]
    except:
        rooms = ''
    return rooms

def get_square(html):
    soup=BeautifulSoup(html, 'lxml')    
    try:
        all_params = soup.find('dl', class_ = 'ov-params-list')
    except:
        all_params = ''
    all_params = all_params.text
    all_params = all_params.replace(' ','')
    alp = all_params.split('\n')
    alp = [x for x in alp if x != '']
    leng_list = len(alp)
    try:
        square = alp[alp.index('Площадь:', 0, leng_list)+1]
    except:
        square = ''
    return square
    
def get_nextpage(html):
    soup=BeautifulSoup(html, 'lxml')
    tds = soup.find('ul', class_ = 'pagination_custom').find_all('li', class_ = 'pagination-nav-next')
    for td in tds:
        try:
            a = 'https://rieltor.ua' + td.find('a', class_ = 'pager-btn').get('href')
        except:
            a = ''
    return  a

def get_adress(html):
    soup=BeautifulSoup(html, 'lxml')
    all_title = soup.find_all('h2', class_ ='catalog-item__title')
    adress = []
    for i in all_title:
        adress.append(i.find('a').text)
    return adress









def write_csv (value, currency, square1, square2, square3, room, state, type_house, adress):
   data = {
        'square1': square1,
        'square2': square2,
        'square3': square3,
        'value':value,
        'currency':currency,
        'state':state,
        'type_house':type_house,
        'room':room,
        'adress':adress
        }
   df = pd.DataFrame(data, columns = ['square1', 'square2', 'square3', 'room', 'type_house', 'state','value', 'currency','adress'])
   df.to_csv('D:\parsing\data.csv')


def main():
    url = 'https://rieltor.ua/flats-sale/'
    all_links = get_links(get_html(url))
    html = get_html(url)
    rooms = []
    states = []
    types_house = []
    prices = []
    currency = []
    square1 = []
    square2 = []
    square3 = []
    next_link = get_nextpage(html)
    m = 1
    n = 0
    adres = get_adress(html)
    ##while next_link!='':
    while n<m:
        nex_html = get_html(next_link)
        all_links = all_links + get_links(nex_html)
        next_link = get_nextpage(nex_html)
        n=n+1
        adres = adres+get_adress(nex_html)
    for i in all_links:
        html= get_html(i)
        price = get_price(html)
        prices.append(price[0])
        currency.append(price[1])
        square = get_square(html)
        squares = square.split('/')
        square1.append(squares[0])
        square2.append(squares[1])
        square3.append(squares[2][:-2])
        room = get_rooms(html)
        state = get_state(html)
        type_house = get_type_house(html)
        rooms.append(room)
        states.append(state)
        types_house.append(type_house)
    write_csv(prices, currency, square1, square2, square3, rooms, states, types_house, adres,)   
     











if __name__ == '__main__':
    main()
