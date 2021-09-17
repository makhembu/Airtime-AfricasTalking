import africastalking #send airtime API
import csv  #python inbuild csv module
import re # regex library

username = "sandbox" #AfricasTalking username
api_key = "36061b0a6786f5561d5a01c9fe5ecbea09ab096597ba49fff2989c873ff6f4d1" #Africastalking password


phone = [] #list to collect phone numbers from csv
airtime_amount = [] #list to collect airtime amount from csv
formatted_number = [] #list to store formatted format numbers
formatted_airtime_amount = [] #list to store cleaned up amount 

# wrting csv data into the lists above
with open('xyz_employees.csv', 'r') as csv_file:
    reader = csv.DictReader(csv_file, delimiter=',') # using dict reader because csv has columns
    for lines in reader:
        phone.append(lines['employee_phone_number']) #appending phone numbers to list
        airtime_amount.append(lines['airtime_amount']) #appending airtime amount to list

#function to convert phone number to international format which is needed by AfricasTalking
def format_international():
    for num in phone: #iterate list
        num = re.sub("[^0-9]", "", num) #regex to extract digits in the phone number string 
        x=num.startswith('254') #checks number prefix
        y =num.startswith('0')  #checks number prefix
        z = num.startswith('7') or num.startswith('1')  #checks number prefix

        if x is True:   #validates  xprefix condition
            form = '+' + num    #adds a + prefix to the number
            if (len(form) == 13):   #checks if number is valid
                formatted_number.append(form)
                print('formatted: ' + str(form))
            else:
                print(form + ' is an invalid number please check again!')

        elif y is True:     #validates y prefix condition
            num = num[1:]   #removes first digit of number
            form = '+254' + num #adds a +254 prefix
            if (len(form) == 13): #checks if number is valid
                formatted_number.append(form)
                print('formatted: ' + str(form))
            else:
                print(form + ' is an invalid number please check again!')

        elif z is True: #validates z prefix condition
            form = '+254' + num #adds a +254 prefix
            if (len(form) == 13):   #checks if number is valid
                formatted_number.append(form)
                print('formatted: ' + str(form))
            else:
                print(form + ' is an invalid number please check again!')

format_international()

#function to cleanup the amount data. extract numbers
def clean_amount(): 
    for i in airtime_amount:
        regex = '[+-]?[0-9]+\.[0-9]+' # regex to check for floats
        if (re.search(regex, i)):   #check if float condition is True
            #removes any character that's not a digit or a decimal point
            i = re.sub("[^0-9.]", "", i)
            formatted_airtime_amount.append(i)  #appends amount to list
        else:
            i =  re.sub("[^0-9]", "", i)    #if number is not a float, extract only digits
            formatted_airtime_amount.append(i)


clean_amount()  #call function

# Initialize the SDK
africastalking.initialize(username, api_key)


# Get the airtime service
airtime = africastalking.Airtime

i=0
for i in range(0,len(formatted_number)):
    # phone_number in international format
    phone_number = formatted_number[i]

    # Set The 3-Letter ISO currency code and the cleaned amount
    currency_code = "KES"
    amount = formatted_airtime_amount[i]

    try:
        # Send data to API
        response = airtime.send(phone_number=phone_number, amount=amount, currency_code=currency_code)
        print(response)
    except Exception as e:
        print(f"Encountered an error while sending airtime. More error details below\n {e}")


