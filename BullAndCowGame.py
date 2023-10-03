from random import randint
def random():
    while True:
        rnum = str(randint(100,999))
        if not(rnum[0] == rnum[1] or rnum[1] == rnum[2] or rnum[0] == rnum[2]):
            return rnum

name = input("Welcome to the cows and bulls games\n Pleasw enter your name.")
print("Hi", name)
chances = 7
cows = 0
bulls = 0
num = str(random())
while chances > 0 :
    print("your have {} chances left".format(chances))
    n = str(input("Enter your guess number : "))
    if num == n:
        print("Great!{} You got it right.".format(name))
        break
    else:
        for i in range(0,3):
            if n[i] == num[i]:
                bulls += 1
            elif n[i] in num:
                cows += 1
        print("Keep going. You have {} bulls and {} cows".format(bulls,cows))
        bulls = 0
        cows = 0
        chances -= 1
print("The correct answer is {}".format(num))





