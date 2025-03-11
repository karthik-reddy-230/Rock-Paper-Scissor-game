
import random 
rock='''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper='''
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
'''

scissors='''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''
game_images=[rock,paper,scissors]
user_choice=int(input("\ntype 0 for rock\ntype 1 for paper\ntype2 for scissors\nwhat do you choose ? "))
if user_choice>=0 and user_choice<=2:
    print()
    print("My choice :")
    print(game_images[user_choice])
    print()

    computer_choice=random.randint(a=0,b=2)
    print("computer chooses")
    print(game_images[computer_choice])
    if user_choice>=3 and user_choice<=0:
        print("enter a valid number")
    elif user_choice==0 and computer_choice==2:
        print("you win!")
    elif user_choice==2 and computer_choice==0:
        print("you lose!")
    elif user_choice>computer_choice:
        print("You win!")
    elif user_choice<computer_choice:
        print("you lose!")
    elif user_choice==computer_choice:
        print("draw")
 
else:
    print("Enter valid move")


