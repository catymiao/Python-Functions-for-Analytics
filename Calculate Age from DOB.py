from datetime import date
 
def calculateAge(birthDate):
    today = date.today() ## date(2021,12,2)
    age = today.year - birthDate.year -((today.month, today.day) <
         (birthDate.month, birthDate.day))
 
    return age   
