import requests
from bs4 import BeautifulSoup

def get_html(url):
    res = requests.get(url)
    return res.text

def get_links(html):
    soup=BeautifulSoup(html, 'lxml')
    titles = soup.select('.catalog-item__title a')
    links = []
    i=0
    for title in titles:
        link = title.get('href')
        if i%2==0:
            links.append('https://rieltor.ua'+link)
        i+=1
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
    
def get_adress(html):
    soup=BeautifulSoup(html, 'lxml')
    try:
        td = soup.find('div', class_='description-wrap')
    except:
        td = ''
    try:
        a = td.find_all('dd', class_= 'description-text')
    except:
        a  = ''
    td = td.text
    td = td.replace(' ', '')  
    print (td)
    
def get_data(html):
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
    try:
        rooms = alp[alp.index('Комнаты:', 0, leng_list)+1][0]
    except:
        rooms = ''
    try:
        state = alp[alp.index('Состояние:', 0, leng_list)+1]
    except:
        state = ''
    try:
        type_house = alp[alp.index('Типдома:', 0, leng_list)+1]
    except:
        type_house = ''
    data = {
        'square' : square,
        'room': rooms,
        'state': state,
        'type_house': type_house
    }
    
    return data



















def main():
    url = 'https://rieltor.ua/flats-sale/'
    all_links = get_links(get_html(url))
    for i in all_links:
        print (i)
    for i in all_links:
        print(get_price(get_html(i)))
        print(get_data(get_html(i)))
        get_adress(get_html(i))












if __name__ == '__main__':
    main()
