import random

correctPassword = "1234"
wrongPasswords = set()
chars = "1234567890"
run = True
while run:
    password = ""
    for i in range(len(correctPassword)):
        password += random.choice(chars)
    if password not in wrongPasswords:
        if password != correctPassword:
            wrongPasswords.add(password)
            print(password)
        else:
            run = False
print(password + " is correct")



correctPassword = 9457

for i in range(1, 10000):

    if i == correctPassword:
        print(f' {i} is correct ')


password = input('Введите ваш пароль:')
start_time = time.time()
chars = '0123456789abcdefghijklmnopqrstuvwxyz'
for i in product(chars,repeat=len(password)):
    if ''.join(i) == password:
        print('\nВаш пароль:',''.join(i),'\nПотребовалось времени:',round(float("%s" % (time.time() - start_time)),2),'секунд')
        break




