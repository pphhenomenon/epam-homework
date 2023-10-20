import asyncio
import json
from collections import defaultdict

import aiohttp
import requests
from bs4 import BeautifulSoup

CBR_URL = 'http://www.cbr.ru/scripts/XML_daily.asp'
BASE_URL = 'https://markets.businessinsider.com'
SP500_URL = 'https://markets.businessinsider.com/index/components/s&p_500'


def dollar_rate():
    response = requests.get(CBR_URL)
    soup = BeautifulSoup(response.text, 'lxml')
    valute = soup.find('valute', {'id': 'R01235'})
    return float(valute.find('value').text.replace(',', '.'))


dollar = dollar_rate()


async def fetch(url):
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            return await response.text()


async def soup_object(url):
    html = await fetch(url)
    return BeautifulSoup(html, 'lxml')


def company_name(soup):
    section = soup.find('span', {'class': 'price-section__label'})
    return section.text.strip()


def company_code(soup):
    section = soup.find('span', {'class': 'price-section__category'})
    return section.find('span').text.replace(', ', '')


def company_price(soup):
    section = soup.find('span', {'class': 'price-section__current-value'})
    price = section.text.replace(',', '')
    return round(float(price) * dollar, 2)


def company_price_earnings_ratio(soup):
    snapshot = soup.find('div', {'class': 'snapshot__header'}, text='P/E Ratio')
    if snapshot is None:
        return float('inf')
    price_earniongs_ratio = snapshot.parent.text.split()[0].replace(',', '')
    return float(price_earniongs_ratio)


def company_potentional_profit(soup):
    snapshot_min = soup.find('div', {'class': 'snapshot__header'}, text='52 Week Low')
    snapshot_max = soup.find('div', {'class': 'snapshot__header'}, text='52 Week High')
    if snapshot_min is None or snapshot_max is None:
        return float('-inf')
    week_min = snapshot_min.parent.text.split()[0].replace(',', '')
    week_max = snapshot_max.parent.text.split()[0].replace(',', '')
    potentional_profit = (float(week_max) - float(week_min)) / float(week_min)
    return round(potentional_profit, 2)


def company_growth(soup):
    section = soup.find_all('td')[-1].find('span')
    if section is None:
        return float('-inf')
    return float(section.text.replace(',', ''))


async def company_page(url, stock):
    soup = await soup_object(url)
    await company_additional_data(soup, url, stock)


async def company_data(pagenum, stock):
    tasks = []
    soup = await soup_object('{}?p={}'.format(SP500_URL, pagenum))
    companies = soup.find('tbody', {'class': 'table__tbody'}).find_all('tr')
    for company in companies:
        url = '{}{}'.format(BASE_URL, company.find('td').find('a').get('href'))
        stock[url]['growth'] = company_growth(company)
        tasks.append(company_page(url, stock))
    await asyncio.gather(*tasks)


async def company_additional_data(company, url, stock):
    stock[url]['name'] = company_name(company)
    stock[url]['code'] = company_code(company)
    stock[url]['price'] = company_price(company)
    stock[url]['P/E'] = company_price_earnings_ratio(company)
    stock[url]['potentional profit'] = company_potentional_profit(company)


def record(filename, item, companies):
    with open("{}.json".format(filename), "w") as output:
        data = [
            {"name": company["name"], "code": company["code"], item: company[item]}
            for company in companies
        ]
        json.dump(data, output, indent=4)


async def company_stock():
    stock = defaultdict(dict)
    for pagenum in range(1, 12):
        await company_data(pagenum, stock)
    return stock


if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    stock = loop.run_until_complete(company_stock())

    companies = stock.values()

    record(
        'price', 'price',
        reversed(sorted(companies, key=lambda company: company['price'])[-10:])
    )

    record(
        'price_earnings_ratio', 'P/E',
        sorted(companies, key=lambda company: company['P/E'])[:10]
    )

    record(
        'growth', 'growth',
        reversed(sorted(companies, key=lambda company: company['growth'])[-10:])
    )

    record(
        'potentional_profit', 'potentional profit',
        reversed(sorted(companies, key=lambda company: company['potentional profit'])[-10:])  # noqa: E501
    )

    loop.close()
