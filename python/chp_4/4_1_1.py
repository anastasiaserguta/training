t = str(round(float(input()) / 5, 1)).split('.')[1]

if int(t) <= 6:
    print('green')
else:
    print('red')