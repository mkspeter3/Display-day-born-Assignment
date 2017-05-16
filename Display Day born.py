      #   MUKASA PETER
      #   [16/U/671]
      #   B. Electrical engineering


import datetime,calendar #1 importing the modules am going to use in the program ie calendar module and datetime module

cur_year = int(datetime.date.today().strftime('%Y')) #2 checking and getting the system year which is now 2017 and saved in the variable as an integer

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

born_month = month_names[month-1] #9 indexing from the month_names list for the month the user was born

date_int = int(date) #10 converting the day of birth to an integer data type

year_born = (cur_year-age) #11 calculating the year the user was born

conc_date = date+endings[date_int-1] #12 concatenating the date the user was born with the respective ending 

day_num = calendar.weekday(year_born,month,date_int) #13 Getting the number of the day corresponding to the given date arguments. Eg Monday is 0, Tuesday is 1....

part_day = days[day_num] #14 indexing from the days list the particular name of the day we have got from step 13

print("You were born on",part_day ,conc_date, born_month,"of the year " ,year_born)
