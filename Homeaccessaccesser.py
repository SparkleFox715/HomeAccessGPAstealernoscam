import requests
page = requests.get("https://homeaccess.katyisd.org/HomeAccess/Account/LogOn?ReturnUrl=%2fHomeAccess%2f")
url = 'https://homeaccess.katyisd.org/HomeAccess/Account/LogOn?ReturnUrl=%2fHomeAccess%2f'
print(page.content)
values = {
    'username':'m0904314',
    'password':'pasew'
}
r=requests.post(url, data=values)
print(r.content)
