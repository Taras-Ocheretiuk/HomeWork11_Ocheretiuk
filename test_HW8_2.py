import pytest
import HomeWork3_Ocheretiuk as H3

def test_human_date_positive ():
    h_date = H3.Human ()
    assert h_date.get_human_date() == "My name is Taras Ocheretiuk I was born 1.01.1990 my phone number 0674454612 I live in the country Ukraine in the city Makariv at the address Shevchenka strit"

def test_city_positive ():
    test_city = H3.City()
    assert test_city.get_your_city() == "I live in the city Makariv this is the Kyiv regine region, in our city live 4000000 residents, index 08000, phone code 027"

def test_country_positive ():
    test_country = H3.Country ()
    assert test_country.get_your_country() == "I live in a country True, located on True continent, population of my country True, telephone code True, capital True, city of my country True."

def test_fractions_plus_positive ():
    test_plus = H3.Fraction (9,3)
    assert test_plus.addition("+") == 12

def test_fractions_minus_positive ():
    test_minus = H3.Fraction (9,3)
    assert test_minus.addition("-") == 6

def test_fractions_mult_positive ():
    test_mult = H3.Fraction (9,3)
    assert test_mult.addition("*") == 27

def test_fractions_divis_positive ():
    test_divis = H3.Fraction (9,3)
    assert test_divis.addition("/") == 3