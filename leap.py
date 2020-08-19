def fun(year):
   if year%4==0:
      if year%100!=0:
            if year%400:
               print('leap yaer')
            else:
               print('not a leap year')
      else:
         print('leap')
   else:
      print('not a leap')
year=int(input('enter a year'))
fun(year)
