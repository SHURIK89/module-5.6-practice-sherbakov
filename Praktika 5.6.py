field = [['-'] * 3 for _ in range(3)]

def show_field(f):
    num ='  0 1 2'
    print(num)
    for row,i in zip(f,num.split()):
        print (f"{i} {' '.join(str(j) for j in row)}")

def users_input(f,user):
    while True:
        place=input(f"Ходит {user} .Введите две координаты через пробел:").split()
        if len(place)!=2:
            print('Координат должно быть две')
            continue
        if not(place[0].isdigit() and place[1].isdigit()):
            print('Координатой должно быть число!')
            continue
        x, y = map(int, place)
        if not(x>=0 and x<3 and y>=0 and  y<3):
            print('Вы за пределами заданного диапазона')
            continue
        if f[x][y]!='-':
            print('Клетка уже занята')
            continue
        break
    return x,y

def position(f,user):
    f_list=[]
    print(f)
    for a in f:
        f_list+=a
    print(f_list)
    positions=[[0,1,2],[3,4,5],[6,7,8],[0,3,6],[1,4,7],[2,5,8],[0,4,8],[2,4,6]]
    index = set([i for i, x in enumerate(f_list) if x == user])
    for b in positions:
        if len(index.intersection(set(b)))==3:
            return True
    return False

def start(field):
    count=0
    while True:
        show_field(field)
        if count%2==0:
            user='X'
        else:
            user = 'O'
        if count<9:
            x, y = users_input(field,user)
            field[x][y] = user

        elif count==9:
            print ('Ничья')
            break
        if position(field,user):
            print("---------------------------------------------")
            print(f"Выйграл игрок {user}")
            break
        count+=1

start(field)
