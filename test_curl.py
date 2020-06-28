import pycurl
import sys
import json
from io import BytesIO

buffer = BytesIO()

token = ""

def main():
    for arg in sys.argv[1:]:
        print(arg)

if __name__ == "__main__":
    main()

c = pycurl.Curl()
c.setopt(c.URL, 'https://app.netatmo.net/syncapi/v1/setstate')

c.setopt(c.HTTPHEADER, ['Accept: application/json,text/plain,*/*',
                        'Content-Type: application/json;charset=utf-8',
                        'Authorization: Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiIsImtpZCI6InpIajdFaFByOHVGY0N1ZkxEVXVJWWdGY293ckFDcVlQOExRVHhYMlVFa2sifQ.eyJpc3MiOiJodHRwczovL2xvZ2luLmVsaW90YnlsZWdyYW5kLmNvbS8wZDg4MTZkNS0zZTdmLTRjODYtODIyOS02NDUxMzdlMGYyMjIvdjIuMC8iLCJleHAiOjE1OTMzNTEwMTQsIm5iZiI6MTU5MzM0NzQxNCwiYXVkIjoiODQ0OWYyMjctN2NiYi00NmMzLWE0YjQtNTAzZjIyMjZkZDYzIiwic3ViIjoiZGJiMTM4YjYtN2U4OC00OWFhLWIzMDYtMTJiOGM4ZDE4ZmU5Iiwib2lkIjoiZGJiMTM4YjYtN2U4OC00OWFhLWIzMDYtMTJiOGM4ZDE4ZmU5IiwiY291bnRyeSI6ImZyIiwiZW1haWxzIjpbImxsLmp1c3NlYXVtZUB5YWhvby5mciJdLCJ0aWQiOiIwZDg4MTZkNS0zZTdmLTRjODYtODIyOS02NDUxMzdlMGYyMjIiLCJ0ZnAiOiJCMkNfMUFfSG9tZUNvbnRyb2wtU2lnbnVwT3JTaWduaW5fZGVzayIsImF6cCI6Ijg0NDlmMjI3LTdjYmItNDZjMy1hNGI0LTUwM2YyMjI2ZGQ2MyIsInZlciI6IjEuMCIsImlhdCI6MTU5MzM0NzQxNH0.fjz3mPf0AwaJTaiLgviKwW-AEJjdi-GdX6QQmw1BhZheuLKZT-Hkt4a0_Uki0v_iNvh0rdHEpTG_nJgbKSvo4jtrQEWxjGsW8bJBKrpaXWS6itC1rHzDBMNnQE2FlyDa3byik6SbaPPoeL6dhJwPg1KGYFbknc3sj-IgznOnKcASR0YbxA0_9cEJwx00XwAGYAaqMPp0GGQ83UY4z6OYSIpS4Z_zq1dooJtqe3D6IHot63YmJ1oN3tI5nYNXmu5tsUuePA7UoGSLRsYPhmD9_0nBiAe3085d473qbRVXQVifRIbeq8GJUFfcjEuU0_lIPtwYoI2dsDQFikjlGHpUeg',
                        '--compressed'])

f = open("data.json", "r")
data = f.read()
print(data)

c.setopt(c.POSTFIELDS, data)
c.setopt(c.WRITEDATA, buffer)

c.perform()
c.close()

body = buffer.getvalue()
print(body)


