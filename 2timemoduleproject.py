#Using time module print a clock and calendar
import time
timestamp=time.strftime('%H:%M:%S:%A:%B:%I:%p:%D')
print(timestamp)
#printing hour (%"H")
timestamp=int(time.strftime('%H'))
print(timestamp)
#printing minutes ("%M")
timestamp=int(time.strftime('%M'))
print(timestamp)
#printing seconds ("%S")
timestamp=int(time.strftime('%S'))
print(timestamp)
#printing days ("%A")
timestamp=time.strftime('%A')
print(timestamp)
#printing months ("%B")
timestamp=time.strftime('%B')
print(timestamp)
#printing time format to 12 hours ("%I")
timestamp=int(time.strftime('%I'))
print(timestamp)
#printing A.M OR P.M ("%p")
timestamp=time.strftime("%p")
print(timestamp)
#printing Date ("%D")
timestamp=time.strftime("%D")
print(timestamp)

#Output:23:36:40:Thursday:December:11:PM:12/29/22
# 23
# 36
# 40
# Thursday
# December
# 11
# PM
# 12/29/22