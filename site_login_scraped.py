import csv
#import urllib.request   don't actually need this anymore, requests works better!
import requests
from bs4 import BeautifulSoup


with requests.Session() as c:
    url = "http://app.leg.wa.gov/DistrictFinder/"
    addressStreet = "720 Reaney Way"
    addressCity = "Pullman"
    addressZip = "99163"
    verificationToken = "XMPzmDcYLw4EVTN-bmAyhIlosj3SpY7wQle6Y-XT7Hvpjrup5IRaEHRa35i5FiL5RNhVBMelMn2J2ZiJuJAsmXTTLtT1x7pukRddS2RIRKU1"
    c.get(url)
    
    current_data = {"Address.Street" : addressStreet,
                    "Address.City" : addressCity,
                    "Address.Zip" : addressZip,
                    "__RequestVerificationToken" : verificationToken
                    }

    print(current_data) #error testing
    page = c.post(url, data=current_data)
    response = page.text
    soup = BeautifulSoup(response, "html.parser")
    print(soup.find("li").next_element.next_element.next_element) #gets the <liL tag containing the info we want
    #print(soup.prettify()) #print the whole page to console
