import datetime
#asking the user to input their birthdate
birthDate = input("Enter your birth date (dd/mm/yyyy)\n>>> ")
birthDate = datetime.datetime.strptime(birthDate, "%d/%m/%Y").date()
print("Your birthday is on "+ birthDate.strftime("%d") + " of " + birthDate.strftime("%B, %Y"))

currentDate = datetime.datetime.today().date()

#some calculations here 
age = currentDate.year - birthDate.year
monthVeri = currentDate.month - birthDate.month
dateVeri = currentDate.day - birthDate.day

#Type conversion here
age = int(age)
monthVeri = int(monthVeri)
dateVeri = int(dateVeri)

# some decisions
if monthVeri < 0 :
    age = age-1
elif dateVeri < 0 and monthVeri == 0:
    age = age-1
#lets print the age now
print("Your age is {0:d}".format(age))