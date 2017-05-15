      #   MUKASA PETER
      #   [16/U/671]
      #   B. Electrical engineering


import datetime,calendar #1 importing the modules am going to use in the program ie calendar module and datetime module

cur_year = int(datetime.date.today().strftime('%Y')) #2 checking the system year which is now 2017 and saved in the variable as an integer

date = input("Enter birth date (1-31)\n") #3 prompts the user to enter day of the month he was born

endings = ["st", "nd", "rd"]+ 17*["th"] + ["st", "nd", "rd"] + 7*["th"] + ["st"] #4 creating a list of day endings in most cases written as superscripts

days = ['Monday',                  #5 creating a list of days of the week
        'Tuesday',
        'Wednesday',      
        'Thursday',
        'Friday',
        'Saturday',
        'Sunday']

month = int(input("Enter month you were born in(1-12)\n")) #6 prompts the user to enter month they were born and it's converted to an integer

month_names = ['January',     #7 creating a list of months of the year
               'February',
               'March',   
               'April',
               'May',
               'June',
               'July',
               'August',
               'September',
               'October',
               'November',
               'December']

age = int(input("How old are you now? \n")) #8 prompting the user for his age and the value being converted into an integer

vari1 = month_names[month-1] #9 indexing from the month_names list for the month the user was born
vari2 = int(date)
vari3 = (cur_year-age)
vari4 = date+endings[vari2-1]
vari5 = calendar.weekday(vari3,month,vari2)
vari6 = days[vari5]

print("You were born on",vari6 ,vari4, vari1,"of the year " ,vari3)
