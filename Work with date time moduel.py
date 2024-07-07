import datetime
import pytz



# d1 = datetime.date(2023, 11, 12)
# print(d1)
# d2 = datetime.date.today()
# print(d2)
# #
# tdelta = datetime.timedelta(days=7)
# exact_time = d2 + tdelta
# print(exact_time)
#
# bday = datetime.date(1995, 11, 15)
# till_date = d2 - bday
# print(till_date.total_seconds())
#
# time_t = datetime.time(9, 30, 12, 1000)
# print(time_t)
#
# both_date_time = datetime.datetime(2023, 11, 15, 12, 45, 23, 10000)
# print(both_date_time)
# print(both_date_time.date())
# print(both_date_time.time())
# print(both_date_time.now())
# both_date_time_timedelta = datetime.timedelta(days=2)
# print(both_date_time_timedelta + both_date_time)
#
#
# # Working with the today, now, utctimezone
#
# time_today = datetime.datetime.today()
# time_now  = datetime.datetime.now()
# time_utc = datetime.datetime.utcnow()
#
# #Difference between now and today
# #Today is basoically is used to return current local date time with timezone = None
# #Now gives us a option to add timezone .. so if we leave timezome empty then both .today and .now will similar
#
# print(time_today)
# print(time_now)
# print(time_utc)
#
# # lets work with UTC and Pytz module#
#
# Pytzz = datetime.datetime(2023, 11, 14, 10, 58, 24, tzinfo=pytz.UTC)
# print(Pytzz)
#
# dt_utcnow = datetime.datetime.now(tz=pytz.UTC)
# print(dt_utcnow)
#
# dt_mtn = dt_utcnow.astimezone(pytz.timezone('Asia/Kolkata'))
# print(dt_mtn)


for all_are_time_zone in pytz.all_timezones:
    print(all_are_time_zone)


# dt1 = datetime(2023, 1, 1, 12, 0, 0)
# dt2 = datetime(2023, 1, 2, 12, 0, 0)
# duration = dt2 + dt1
# print(duration)