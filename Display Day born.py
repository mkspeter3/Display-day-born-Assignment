     #   Mukasa Peter


import calendar

cur_year = 2017

date = input("Enter birth date (1-31)\n")

endings = ["st", "nd", "rd"]+ 17*["th"] + ["st", "nd", "rd"] + 7*["th"] + ["st"]

days = ['Monday','Tuesday','Wednesday',
        'Thursday','Friday','Saturday',
        'Sunday']

month = int(input("Enter month you were born in(1-12)\n"))

month_names = ['January','February','March',
                'April','May','June',
                'July','August','September',
                'October','November','December']

age = int(input("How old are you now? \n"))

vari1 = month_names[month-1]
vari2 = int(date)
vari3 = (cur_year-age)
vari4 = date+endings[vari2-1]
vari5 = calendar.weekday(vari3,month,vari2)
vari6 = days[vari5]

print("You were born on",vari6 ,vari4, vari1,"of the year " ,vari3)
