from homework10.parser import (company_code, company_name,
                               company_potentional_profit, company_price,
                               company_price_earnings_ratio)


def test_company_name(soup):
    assert company_name(soup) == "Chipotle Mexican Grill Inc."


def test_company_code(soup):
    assert company_code(soup) == "CMG"


def test_company_price(soup):
    assert company_price(soup)


def test_company_price_earnings_ratio(soup):
    assert company_price_earnings_ratio(soup) == 68.75


def test_company_potentional_profit(soup):
    assert company_potentional_profit(soup) == 0.53
