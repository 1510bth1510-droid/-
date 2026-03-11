while True:
    a = (input("입력=>"))
    print("="*40)
    a[::-1]
    if len(a) == 1: 
        print("한 글자 입니다.")
        break
    elif a == a[::-1]:
        print("회문입니다.")
        break
    else:
        print("회문이 아닙니다.")
        break