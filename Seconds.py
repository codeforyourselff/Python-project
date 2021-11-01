seconds = int(input("Enter seconds from here:"))

minutes = seconds//60
seconds = seconds%60
hours = minutes//60
print("hours"+ str(hours)+"minutes"+ str(minutes)+"seconds:"+ str(seconds))
# seconds = seconds%60
# hours = minutes//60;
# print(hours,minutes,seconds)