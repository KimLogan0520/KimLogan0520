import datetime

now = datetime.datetime.now()
print(now)

output_a = now.strftime("%Y.%m.%d %H:%M:%S")
output_b = "{}년 {}월 {}일 {}시 {}분 {}초".format(now.year, now.month, now.day, now.hour, now.minute, now.second)
output_c = now.strftime("%Y{}.%m{}.%d{} %H{}:%M{}:%S{}".format(*"년월일시분초"))
print(output_a)
print(output_b)
print(output_c)

after = now + datetime.timedelta(
    weeks=1,
    days=1,
    hours=1,
    minutes=1,
    seconds=1)
print(now.strftime("%Y{}.%m{}.%d{} %H{}:%M{}:%S{}".format(*"년월일시분초")))
print(after.strftime("%Y{}.%m{}.%d{} %H{}:%M{}:%S{}".format(*"년월일시분초")))

output = now.replace(year=(now.year+1))
print(output)