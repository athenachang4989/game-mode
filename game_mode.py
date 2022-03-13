while True:
    mode = input('請輸入遊戲模式：')
    if mode == 'q': # quit
        break
    elif mode == '1':
        print('將啟動模式一')
    elif mode == '2':
        print('將啟動模式二')
    else:
        print('請輸入 q/1/2')