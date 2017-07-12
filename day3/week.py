print("do you want month or day name")
y=str(raw_input())
if (y=='day')
    days=['sunday','monday','tuesday','wednesday','thursday','friday','saturday']
    print("enter the day number you want")
    x=str(raw_input())
    if x.lower() not in days :
      print("day is not available")
    else:
      num=days.index(x.lower())
      print(num+1)
if(y=='month')
    month=['january','february','march','april','may','june','july','august','september','october','november']
    print("enter the day number you want")
    x=str(raw_input())
    if x.lower() not in days :
      print("day is not available")
    else:
      num=month.index(x.lower())
      print(num+1)
      
