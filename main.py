import random,os,time,sys
global board
board = [['⚪', '⚪', '⚪', '⚪', '⚪', '⚪','⚪'], 
         ['⚪', '⚪', '⚪', '⚪', '⚪', '⚪','⚪'], 
         ['⚪', '⚪', '⚪', '⚪', '⚪', '⚪','⚪'], 
         ['⚪', '⚪', '⚪', '⚪', '⚪', '⚪','⚪'], 
         ['⚪', '⚪', '⚪', '⚪', '⚪', '⚪','⚪'], 
         ['⚪', '⚪', '⚪', '⚪', '⚪', '⚪','⚪']]
'''
[r,y,r,y,y,y,y]
'''
'''
███╗   ███╗ █████╗ ██╗  ██╗███████╗    ███████╗██╗   ██╗██████╗ ███████╗               
████╗ ████║██╔══██╗██║ ██╔╝██╔════╝    ██╔════╝██║   ██║██╔══██╗██╔════╝               
██╔████╔██║███████║█████╔╝ █████╗      ███████╗██║   ██║██████╔╝█████╗                 
██║╚██╔╝██║██╔══██║██╔═██╗ ██╔══╝      ╚════██║██║   ██║██╔══██╗██╔══╝                 
██║ ╚═╝ ██║██║  ██║██║  ██╗███████╗    ███████║╚██████╔╝██║  ██║███████╗               
╚═╝     ╚═╝╚═╝  ╚═╝╚═╝  ╚═╝╚══════╝    ╚══════╝ ╚═════╝ ╚═╝  ╚═╝╚══════╝               
                                                                                       
 ██████╗ ██████╗ ███╗   ██╗███████╗ ██████╗ ██╗     ███████╗    ██╗███████╗            
██╔════╝██╔═══██╗████╗  ██║██╔════╝██╔═══██╗██║     ██╔════╝    ██║██╔════╝            
██║     ██║   ██║██╔██╗ ██║███████╗██║   ██║██║     █████╗      ██║███████╗            
██║     ██║   ██║██║╚██╗██║╚════██║██║   ██║██║     ██╔══╝      ██║╚════██║            
╚██████╗╚██████╔╝██║ ╚████║███████║╚██████╔╝███████╗███████╗    ██║███████║            
 ╚═════╝ ╚═════╝ ╚═╝  ╚═══╝╚══════╝ ╚═════╝ ╚══════╝╚══════╝    ╚═╝╚══════╝            
                                                                                       
███████╗██╗   ██╗██╗     ██╗         ███████╗ ██████╗██████╗ ███████╗███████╗███╗   ██╗
██╔════╝██║   ██║██║     ██║         ██╔════╝██╔════╝██╔══██╗██╔════╝██╔════╝████╗  ██║
█████╗  ██║   ██║██║     ██║         ███████╗██║     ██████╔╝█████╗  █████╗  ██╔██╗ ██║
██╔══╝  ██║   ██║██║     ██║         ╚════██║██║     ██╔══██╗██╔══╝  ██╔══╝  ██║╚██╗██║
██║     ╚██████╔╝███████╗███████╗    ███████║╚██████╗██║  ██║███████╗███████╗██║ ╚████║
╚═╝      ╚═════╝ ╚══════╝╚══════╝    ╚══════╝ ╚═════╝╚═╝  ╚═╝╚══════╝╚══════╝╚═╝  ╚═══╝
'''
def changeColor(first,second,third):
  return (f'{first}▄████████  ▄██████▄  ███▄▄▄▄   ███▄▄▄▄      ▄████████  ▄████████     ███             ▄████████  ▄██████▄  ███    █▄     ▄████████ \n' 
'███    ███ ███    ███ ███▀▀▀██▄ ███▀▀▀██▄   ███    ███ ███    ███ ▀█████████▄        ███    ███ ███    ███ ███    ███   ███    ███ \n'
'███    █▀  ███    ███ ███   ███ ███   ███   ███    █▀  ███    █▀     ▀███▀▀██        ███    █▀  ███    ███ ███    ███   ███    ███ \n'
f'{second}███        ███    ███ ███   ███ ███   ███  ▄███▄▄▄     ███            ███   ▀       ▄███▄▄▄     ███    ███ ███    ███  ▄███▄▄▄▄██▀ \n'
'███        ███    ███ ███   ███ ███   ███ ▀▀███▀▀▀     ███            ███          ▀▀███▀▀▀     ███    ███ ███    ███ ▀▀███▀▀▀▀▀ \n'   
'███    █▄  ███    ███ ███   ███ ███   ███   ███    █▄  ███    █▄      ███            ███        ███    ███ ███    ███ ▀███████████ \n'
f'{third}███    ███ ███    ███ ███   ███ ███   ███   ███    ███ ███    ███     ███            ███        ███    ███ ███    ███   ███    ███ \n'
'████████▀   ▀██████▀   ▀█   █▀   ▀█   █▀    ██████████ ████████▀     ▄████▀          ███         ▀██████▀  ████████▀    ███    ███\033[1;0m') 
sign = changeColor('\033[6;34m','\033[3;37m','\033[5;36m')

def write(text,tm = .06, nxt = True,ans=False):
  text += ' [CLICK_ENTER]' if nxt else ''
  for character in text:
    sys.stdout.write(character)
    sys.stdout.flush()
    time.sleep(tm)
  print()
  if nxt:
    input('\033[1A\033['+str(len(text))+'C')
  elif ans:
    return input('\033[1A\033['+str(len(text))+'C')
#Changes all the pieces to white aka null
def reset_board():
  for row in range(6):
    for col in range(7):
      board[row][col] = '⚪'
#Prints the board
def print_board(table):
  print('\033[5;34m┏'+('╾'*14)+'┓')
  for d in table:
    print('┃',end='')
    for dd in range(len(d)):
      print(d[dd],end='')
    print('┃')
  print('┗'+('━'*14)+'┛\n\033[1;0m 1 2 3 4 5 6 7')
#This updates the board after you chosed a non-full slot
def update_board(slot,piece,test=False):
  if board[0][slot] != '⚪':
    return 'full'
  for col in range(6):
    if board[col][slot] == '⚪':
      if not test:
        board[col][slot] = piece
        time.sleep(.3)
        os.system('clear')
        print(sign)
        print_board(board)
      if col+1 < 6 and board[col+1][slot] == '⚪' and not test:
        board[col][slot] = '⚪'
  return 'done'
#This is the function that actually check if u won or not
def quick_check(arr,other,piece):
  temp,cnt = ''.join(arr),0
  for p in range(len(temp)):
    cnt += 1 if temp[p] == piece else 0
    if temp[p] != piece and p >= 4:
      return False
    elif cnt >= 4:
        return True
#This function gathers various ways you could win and calls quick_check to see if u won
def check_win(piece) -> str:
  other = '🔴' if piece == '🟡' else '🟡'
  for row in range(7):
    if quick_check(board[0 if row == 6 else row ],other,piece):
      return 'wonh'
    else:
      temp = []
      for col in range(6):
        temp.append(board[col][row])
      if quick_check(temp,other,piece):
        return 'wonv'
      elif row <= 1:
        dia = []
        for r in range(4):
          low,high,nlow,nhigh,t,m = [],[],[],[],r,r + 3
          for c in range(6):
            s = c + 1
            if s < 6 and len(nlow) <= 3:
              nlow.append(board[s + 1 if r == 1 else s][t - 1 if r == 1 else t])
            if m >= 0:
              high.append(board[c][m])
            if m >= -1 and len(nhigh) <= 3:
              #print(board[s + 1 if r == 1 else s][m + (3 - r)],'s =',s + 1 if r == 1 else s,'m = ',m + (3 - r))
              nhigh.append(board[s + 1 if r == 1 else s][m + (3 - r)])
            low.append(board[c][t])
            t = t + 1 if t <= 5 else 0
            m -= 1
          dia.append(nlow)
          dia.append(low)
          dia.append(high)
          dia.append(nhigh)
        for d in dia:
          if quick_check(d,other,piece):
            return 'wond'
  return 'nothing'
def check_full(n,u,piece):
  while True:
    try:
      u = int(u) - 1
      board[0][u]
    except:
      try: 
        os.system('clear')
        u = int(write('Player'+str(n)+' choose a slot from [1-7]: ',.06,False,True)) - 1
        board[0][u]
        break
      except:
        write('You must what is in the brackets, try again!')
        continue
    try:
      if update_board(u,piece,True) != 'full':
        break
    except:
      try: 
        os.system('clear')
        u = int(write('Player'+str(n)+' choose a slot from [1-7]: ',.06,False,True)) - 1
        board[0][u]
        break
      except:
        write('You must what is in the brackets, try again!')
        continue
    if update_board(u,piece,True) == 'full':
      write('Pick another slot Player' +str(n)+', this slot is full!')
      os.system('clear')
    else:
      break
  return u
def check_player(u,piece):
  if 'won' in  check_win(piece):
    reset_board()
    write('Player'+str(u)+' you have won!')
    return 'won'
  return u
#Driver 
write('Hello and welcome to',.05,True)
write(sign,.004,False,False)
u = write('Would you like to play two player or comptuer mode?[2p/com]: ',.06,False,True).lower()
os.system('clear')
if u == 'com':
  while True: 
    print(sign)
    print_board(board)
    try:
      u = int(write('Choose a slot from [1-7]: ',.06,False,True)) - 1
      board[0][u]
    except:
      write('You must what is in the brackets, try again!')
      os.system('clear')
      continue
    if update_board(u,'🔴',True) == 'full':
      write('Pick another slot, this slot is full!')
      os.system('clear')
      continue
    update_board(u,'🔴')
    if 'won' in check_win('🔴'):
      os.system('clear')
      write('Congrats player you have beaten Computer!')
      sign = changeColor('\033[1;32m','\033[3;37m','\033[1;33m')
      if write('Would you like to play again?[yes/no]: ',.06,False,True) == 'yes':
        reset_board()
        continue 
      else:
        break
    com = random.randint(1,6)
    while update_board(com,'🟡',True) != 'done':
      com = random.randint(1,6)
    write('Computer chosed slot '+str(com+1)+'.')
    update_board(com,'🟡')
    os.system('clear')
    if 'won' in  check_win('🟡'):
      write('Player you have lost!')
      sign = changeColor('\033[1;31m','\033[3;37m','\033[1;30m')
      if write('Would you like to play again?[yes/no]: ',.06,False,True) == 'yes':
        reset_board()
        continue 
      else:
        break
  
elif u == '2p':
  while True:
    print(sign)
    print_board(board)
    p1 = check_full(1,write('Player 1 choose a slot from [1-7]: ',.06,False,True),'🔴')
    update_board(p1,'🔴')
    if check_player(1,'🔴') == 'won':
      if write('Would you like to play again?[yes/no]: ',.06,False,True).lower() == 'yes':
        os.system('clear')
        continue 
      else:
        break
    p2 = check_full(2,write('Player 2 choose a slot from [1-7]: ',.06,False,True),'🟡')
    update_board(p2,'🟡')
    if check_player(2,'🟡') == 'won':
      if write('Would you like to play again?[yes/no]: ',.06,False,True).lower() == 'yes':
        os.system('clear')
        continue 
      else:
        break
    os.system('clear')
sign = changeColor('\033[6;34m','\033[3;37m','\033[5;36m')
os.system('clear')
write("Thank you for playing, ")
write(sign,.001,False,False)
write('Hope you enjoyed it!')