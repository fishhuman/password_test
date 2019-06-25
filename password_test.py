password = 'a123456'
n = 2
while True:
    password_1 = input('請輸入密碼，最多輸入三次' )
    if password_1 == password:
        print('登入成功' )
        break
    else:
        if n >= 1:
            print('密碼錯誤! 還有', n, '次機會' )
            n = n-1
        else:
            print('輸入已達三次，將永久鎖定' )
            break
                     


