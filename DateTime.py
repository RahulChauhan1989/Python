import datetime
#import pytz 

d=datetime.date(2019,9,23)
print("Manual Date : {} ".format(d))
print("Automated Date : {},Date {},Month {},Year {} ".format(datetime.date.today(),datetime.date.today().day,datetime.date.today().month,datetime.date.today().year))

today=datetime.date.today()

##moment().isoWeekday(1); // Monday
#moment().isoWeekday(7); // Sunday
#moment().isoWeekday("Sunday");
#moment().isoWeekday("Monday");

print(today.weekday())
print(today.isoweekday())
print(today.strftime("%A"))

tdelta=datetime.timedelta(days=11)
print(today+tdelta)
print(datetime.date(2020,8,11)-datetime.date.today())

print(datetime.time(9,30,45,100000))
tdelta1=datetime.timedelta(hours=11)
print(datetime.datetime(2019,11,20,9,30,45,100000))
