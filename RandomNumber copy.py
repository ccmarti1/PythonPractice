import random

# x=random.randrange(1, 10)

# if x<=5:
# 	print(x,' is less than 5')
# else:
# 	print(x,' is more than 5')


# print()
# print()
# print()

start=
survive=0
y=random.randrange(0, 100)
userinput=input('Type START to start game')
# value=userinput.upper()

print('Welcome to the Monkey House')
print('Sellect a game:')
print('a) Death Game')
print('b) I do not wish to play game')
userinput=input('Type a to start')
if userinput.upper()=='A':
    print('Death Game')
    print('How to Play:')
    print('You must travers 100 meters to make it to the other side')
    print('There may be tools and boost allot the journey that may help you')

    print('Showman: Hello Contestants you have chosen "DEATH GAME!".')

    print('(✿❦ ͜ʖ ❦)Showman:')
    print('You must travel through the forest of death to claim your prize.')
    print('Lucky for you, you have a survival rating of 99%')

    print('(✿❦ ͜ʖ ❦)Showman:')
    print('But there is a "1%" change you will run into a demon that will kill you!!')
    print('And must fight for your life')
    print('(✿❦ ͜ʖ ❦)Showman: bhahah! (Laughs Moniacally)') 
    print('Would you like to test your merit?')
    userinput=input('Y-yes N-no')

    while userinput.upper()=='Y':
        if y ==1:
            print('*you died')
            print('(✿❦ ͜ʖ ❦)Showman: Wellcome to hell!')
            break
        survive=survive+1
        print('Times Survived: ', survive)
        userinput=input('Would you like to try again?')
        if survive==100:
            print('(✿❦ ͜ʖ ❦)Showman: Congradulations contestant you have Won!')
            print('You have won |100| SOULS (✿❦ ͜ʖ ❦)')
            break
    else:
            userinput=input('Incorrect response, type y-yes or n-no')

            continue
else:
    print("Incorrect response, Restart Game ")
        