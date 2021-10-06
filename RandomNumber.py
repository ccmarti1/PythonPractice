import random

# x=random.randrange(1, 10)

# if x<=5:
# 	print(x,' is less than 5')
# else:
# 	print(x,' is more than 5')


# print()
# print()
# print()

# Was going to ask for personas gender to entegrate response into special scene in story

# Showman='(✿❦ ͜ʖ ❦)Showman: Good choice young {}'
# userinput=input('a) Male or b) Female? ')
# gender=userinput

survive=0
death=1
demon=6
map:10,30,50,70,90
potion= 20,40,60,80,100
List_All=potion, map, demon, death
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

# as long as userinput is y program will run
    while userinput.upper()=='Y':
        # if any special numbers a sellect this program willl filter which attribute is attained
        if x==List_All:
             # if statement for if player dies
            if y ==death:
                print('*you died')
                print('(✿❦ ͜ʖ ❦)Showman: Wellcome to hell!')
                print('Meters Crossed: ', survive) #prints players progress to screen
                break
            # Potion discovery item to boost potioning
            if y== potion:
                print('You dicovered a telleportation potion in the forest')
                survive=survive+10
                continue
            # map discovery item boost player positioning
            if y==map:
                print('You dicovered a map in the forest and find a short-cut')
                survive=survive+5
                continue
            #player runs into demon but manages to escape
            if y==demon:
                print("Oh no its a demon")
                print('You barely escaped alive and was push back a few meters')
                survive=survive-3
                continue
            print('Meters Crossed: ', survive) #prints players progress to screen
            continue



# addes to player progress
        survive=survive+1
        print('Meters Crossed: ', survive) #prints players progress to screen
        # userinput=input('Type y to travel another meter') # ask player to continue traveling or to quit
# if player decides to quite game
        if userinput.upper()=='n':
            print("You've chosen the easy way out")
            break
# if player gets to 100 meters the win game
        if survive==100:
            print('(✿❦ ͜ʖ ❦)Showman: Congradulations contestant you have Won!')
            print('You have won |100| SOULS (✿❦ ͜ʖ ❦)')
            break
# if player travels more than 100 meters he get a special response that continues his story
        if survive > 100:
            print("(‡▼益▼)Warrior: I like your ambition lad, why don't come join the Kings Vangaurd?")
            print('(✿❦ ͜ʖ ❦)Showman: Wow what an over achiever, we Showmen could use a fella like you. What do you say?')
            print()
            print('What is your decision?')
            print("a) Join Vangaurd")
            print("b) Join Showmen")
            print("c) Take price money and go your seporate ways")
            
            userinput=input('Answer') # allows user to give there answer to mpc's request
            if userinput.upper()=='A':
                print('(‡▼益▼)Warrior: Welcome to the Kings Vangaurd we ride to the castle at dawn')
            if userinput.upper()=='B':
                print("(✿❦ ͜ʖ ❦)Showman: Good choice young man, we'll meet with the boss before dawn")
            if userinput.upper()=='C':
                print('(✿❦ ͜ʖ ❦)Showman: Thats too bad, heres your prize')
                print('You have won |100| SOULS')
            break

else:
    print("Incorrect response, Restart Game ")
