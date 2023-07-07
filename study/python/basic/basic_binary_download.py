from urllib import request
import ssl
ssl._create_default_https_context = ssl._create_unverified_context

target = request.urlopen("https://www.hanbit.co.kr/images/common/logo_hanbit.png")
output = target.read()
print(output)

file = open("output.png", "wb")
file.write(output)
file.close()