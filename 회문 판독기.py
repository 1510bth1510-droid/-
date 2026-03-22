while True:
    print("="*40)
    a = (input("입력=>"))
    print("="*40)
    if len(a) == 1: 
        print("한 글자 입니다.")
        print("="*40)
        b = int(input('다시 시작 = 1번\n종료 = 2번'))
        if b == 1:
            continue
        elif b == 2:
            break
        else:
            print('잘못된 입력')
    elif a == a[::-1]:
        print("회문입니다.")
        print("="*40)
        b = int(input('다시 시작 = 1번\n종료 = 2번'))
        if b == 1:
            continue
        elif b == 2:
            break
        else:
            print('잘못된 입력')
    else:
        print("회문이 아닙니다.")
        print("="*40)
        b = int(input('다시 시작 = 1번\n종료 = 2번'))
        if b == 1:
            continue
        elif b == 2:
            break
        else:
            print('잘못된 입력')