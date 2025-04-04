import random
dice_A = [1,2,3,4,5,6]
dice_B =[1,2,3,4,5,6]
li = []
for i in range(len(dice_A)):
    for j in range(len(dice_B)):
        li.append((dice_A[i], dice_B[j]))
print(li)

dict = {}
for i in range(2,13):
    count = 0
    for j in li:
        if i == j[0]+j[1]:
            count += 1
    dict[str(i)] = count/len(li)
print(dict)

R = int(input("enter num of rounds: "))
player1_wins = 0
player2_wins = 0
for i in range(R):
    p1_num1 = random.randint(1,6)
    p1_num2 = random.randint(1,6)
    p2_num1 = random.randint(1,6)
    p2_num2 = random.randint(1,6)

    p1_sum = p1_num1+p1_num2
    p2_sum = p2_num1+p2_num2
    print(p1_sum,p2_sum)
    
    if dict[str(p1_sum)] > dict[str(p2_sum)]:
        print("player1 wins this round")
        player1_wins += 1
    elif dict[str(p1_sum)] < dict[str(p2_sum)]: 
        print("player2 wins this round")
        player2_wins += 1
    else:
        print("This round is draw")

if player1_wins > player2_wins:
    print("Player1 wins the game")
elif player2_wins > player1_wins:
    print("Player2 wins the game")
else:
    print("It's a draw")