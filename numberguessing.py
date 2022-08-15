import random
n = random.randint(0, 50)

print("No of attempts you have is : 5\n")

attempts = 5
point = 20

while attempts > 0:
    guess_num = int(input(f"\nEnter your guess:"))
    if guess_num == n:
        print(f"You have guessed it right.\n You scored {point} points!\n")
        break
    elif guess_num < n:
        print(f"Original number is greater!\n")
        point = point - 1
    else:
        print(f"Original number is smaller!\n")
        point = point - 1
    attempts = attempts - 1

if attempts == 0:
    print(f"Oops! you finished all your chances")
