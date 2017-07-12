days=['sunday','monday','tuesday','wednesday','thursday','friday','saturday']
print("enter the day number you want")
x=str(raw_input())
if x.lower() not in days :
      print("day is not available")
else:
      num=days.index(x.lower())
      print(num+1)
      
