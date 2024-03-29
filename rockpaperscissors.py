import random

def rock_paper_scissors():
  player = input("Pilihan - 'g' untuk gunting, 'b' untuk batu, dan 'k' untuk kertas:")
  choices = ['g', 'b', 'k']
  opponent = random.choice(choices)
  
  if player == opponent:
    return print(f"Seri! Lawan kamu adalah {opponent}")
  
  if check_win(player, opponent):
    return print(f"Yeii! Kamu menang! Lawan kamu adalah {opponent}")
  
  if check_win(player, opponent) != True:
    return print(f"Yahh! Kamu kalah! Lawan kamu adalah {opponent}")
  
def check_win(user, computer):
  if(user == 'b' and computer == 'g') or (user == 'k' and computer == 'b') or (user == 'g' and computer == 'k'):
    return True

rock_paper_scissors()