# Declare and prompt user for name and student id
name = input("What is your Name? ")
studentId = input("What is your Student Id? ")

# greet the user by name and student id
print(f"Hello {name} I see your student id is {studentId}")

# declare variables
number = 5
numOfTries = 0

# ask user for a guess
userGuess = int(input("Please guess a number between 1 and 10... "))
numOfTries += 1

# guessing loop
while userGuess != number:
    if userGuess < number:
        print("You guessed too low")
    else:
        print("You guessed too high")

    userGuess = int(input("Please guess a number between 1 and 10... "))
    numOfTries += 1

print(f"Congratulations, {name}! You guessed the number in {numOfTries} tries!")

# while loop increment section
print("\nOutput from the 'while' loop:")
increment = 1

while increment <= 5:
    print(f"{number} incremented by {increment} is {number + increment}")
    increment += 1

# for loop increment section
print("\nOutput from the 'for' loop:")

for increment in range(1, 6):
    print(f"{number} incremented by {increment} is {number + increment}")