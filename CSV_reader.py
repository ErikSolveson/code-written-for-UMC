# WSU Student Legislative district finder
# Author: Erik Solveson
# Date: 12 March 2017


import csv
import requests
from bs4 import BeautifulSoup
from datetime import datetime


# Main function whose loop readers input, gets district number, then writes all to output file
def getData_csv(a):
    i = 0
    startDateTime = datetime.now()
    print("STARTING LOOP AT:", startDateTime)
    with open(a, newline='', encoding='utf-8') as file:
        for row in csv.reader(file, delimiter=',', quotechar='"'):
            statusTag = row[0]
            number = row[1]
            Street = row[2]
            City = row[3]
            State = row[4]
            Zip = row[5]
            districtNumber = webData(Street, City, Zip)
            #print(districtNumber)
            writeCSV(statusTag, Street, City, State, Zip, districtNumber)
            i = i+1
    endDateTime = datetime.now()
    print("ENDING LOOP AT:", endDateTime)
    print("Time Delta: ", str(endDateTime - startDateTime)) # , " difference (end - start)"
    print("Loop Count: " + str(i)) # time calculations


# Pass address data to WA State API and returns the district number
def webData(street, city, zipcode):
    with requests.Session() as c:
        url = "http://app.leg.wa.gov/DistrictFinder/"
        addressStreet = street
        addressCity = city
        addressZip = zipcode
        verificationToken = "XMPzmDcYLw4EVTN-bmAyhIlosj3SpY7wQle6Y-XT7Hvpjrup5IRaEHRa35i5FiL5RNhVBMelMn2J2ZiJuJAsmXTTLtT1x7pukRddS2RIRKU1"
        c.get(url)
        
        current_data = {"Address.Street" : addressStreet,
                        "Address.City" : addressCity,
                        "Address.Zip" : addressZip,
                        "__RequestVerificationToken" : verificationToken
                        }

        page = c.post(url, data=current_data)
        response = page.text
        soup = BeautifulSoup(response, "html.parser")
        districtString = soup.find("li").next_element.next_element.next_element #gets the <liL tag containing the info we want
        districtNumber = parseWebData(districtString)
        #print(districtNumber)
        return districtNumber


# Get the district number from the API's returned string
def parseWebData(string):
    string = str(string)
    if( string.find("</li>") == 34):
        districtNumber_1digit = string[33]
        return districtNumber_1digit
    elif( string.find("</li>") == 35):
        districtNumber_2digit = string[33] + string [34]
        return districtNumber_2digit
    else:
        districtNumber = "unexpected input (district number at wrong index)"
        # xxx Note: else case has not been tested


# Writes input string data with district number appended to output file
def writeCSV(statusTag, Street, City, State, Zip, districtNumber):
            with open("Test_out.csv", "a") as f:  # , encoding='utf-8'
                w = csv.writer(f, delimiter=',',quotechar='"', quoting=csv.QUOTE_NONNUMERIC) 
                rowString = statusTag + "," + Street + "," + City + "," + State + "," + Zip + "," + str(districtNumber)
                print(rowString)         #debug
                w.writerow([statusTag, Street, City, State, Zip, districtNumber])


# Call the main function    
getData_csv("Test.csv")
