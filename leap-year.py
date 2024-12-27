import calendar

def is_leap_year(year):
    return calendar.isleap(year)

year_to_check=int(input("Enter year to check if its leap year or not!"))
result=is_leap_year(year_to_check)
print(f"{year_to_check} is a leap year? : {result}") 