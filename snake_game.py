'''
1 for snake
-1 for water
0 for gun

'''
import random
random_number= random.choice([-1,0,1])

computer= random_number
youstr = input("Enter your choice: ")
youDict = {"s":1,"w":-1,"g":0}
you=youDict[youstr]
reverseDict= {1:"Snake",-1:"Water",0:"Gun"}

print(f"You chose {reverseDict[you]}\nComputer chose {reverseDict[computer]}")


# if(computer== -1 and you ==1):
#     print("You Win! ")

# elif(computer== -1 and you==0):
#     print("You Lose! ")
# elif(computer==you):
#     print("Its a draw!!")       
# elif(computer==1 and you==-1):
#     print("You Lose! ") 
# elif(computer== 1 and you==0):
#     print("You Win! ")
# elif(computer==0 and you==1):
#     print("You Lose! ")
# elif(computer==0 and you== -1):
#     print("You Lose! ")

if((computer - you)== -1 or (computer - you)== 2):
    print("You Lose! ")
else:
    print('You Win! ')
