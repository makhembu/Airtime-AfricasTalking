# works with both python 2 and 3
from __future__ import print_function
import africastalking
from pandas import *

# reading CSV file
data = read_csv("xyz_employees.csv")
#adding names to list
name = data['employee_name'].tolist()
#adding phone numbers to list
phone = data['employee_phone_number'].tolist()
#adding airtime to list
airtime = data['airtime_amount'].tolist()
formated_number = []

class AIRTIME:
    def __init__(self):
        # Set your AfricasTalking credentials
        self.username = "usenname"
        self.api_key = "password"

        # Initialize the SDK
        africastalking.initialize(self.username, self.api_key)

        # Get the airtime service
        self.airtime = africastalking.Airtime
    
    

    def send(self):
        #loop through phone numbers
        for i in range(0,len(phone)):
            # adding a try/catch to break the loop if an error is found
            try:
                # Set phone_number in international format
                phone_number = phone_number[i]

                # Set The 3-Letter ISO currency code and the amount
                amount = airtime[i]
                currency_code = "KES"

                try:
                    # That's it hit send and we'll take care of the rest
                    responses = self.airtime.send(phone_number=phone_number, amount=amount, currency_code=currency_code)
                    print (responses)
                except Exception as e:
                    print ("Encountered an error while sending airtime:%s" %str(e))
            except:
                break 

if __name__ == '__main__':
    AIRTIME().send()