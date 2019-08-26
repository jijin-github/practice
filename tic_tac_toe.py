def print_board():
    print("_____")
    print(choices[0]+"|"+choices[1]+"|"+choices[2])
    print("_____")
    print(choices[3]+"|"+choices[4]+"|"+choices[5])
    print("_____")
    print(choices[6]+"|"+choices[7]+"|"+choices[8])
    print("_____")

choices = [str(i) for i in range(0,9)]    

win = False
first_person = True
print_board()
while not win:
    if first_person:
        select_choice = int(input("Enter First Person Choice:- "))
    else:
        select_choice = int(input("Enter Second Person Choice:- "))
    print(select_choice)
    if choices[select_choice] in ['A', 'B']:
        print("Already selected")
    else:
        choices[select_choice] = 'A' if first_person else 'B'

    if choices[0] == choices[1] == choices[2] or choices[3] == choices[4] == choices[5] or choices[6] == choices[7] == choices[8]:
        win = True
    if choices[0] == choices[3] == choices[6] or choices[1] == choices[4] == choices[7] or choices[2] == choices[5] == choices[8]:
        win = True
    if choices[0] == choices[4] == choices[8] or choices[6] == choices[4] == choices[2]:
        win = True
    if win:
        if first_person:
            print("First person win the Game!!")
        else:
            print("Second person win the Game!!")  
    print_board()
    first_person = not first_person
