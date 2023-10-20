import pytest
import requests
from bs4 import BeautifulSoup

BASE_URL = 'https://markets.businessinsider.com/stocks/cmg-stock'


@pytest.fixture
def soup():
    response = requests.get(BASE_URL)
    return BeautifulSoup(response.text, 'lxml')
