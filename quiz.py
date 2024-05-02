print("Welcome to the computer quiz game!")

playing = input("Do you want to play? ")

if playing.lower() != "yes":
    print("Goodbye")
    quit()
print("Great! Let's play!")

score= 0

#question 1
answer = input("What does CPU stand for? ")
if answer.lower() == "central processing unit":
    print("Correct!")
    score += 1
else:
    print("Incorect")

#question 2
answer = input("What does GPU stand for? ")
if answer.lower() == "graphics processing unit":
    print("Correct!")
    score += 1
else:
    print("Incorect")

#question 3
answer = input("What does RAM stand for? ")
if answer.lower() == "random access memory":
    print("Correct!")
    score += 1
else:
    print("Incorect")

#question 4
answer = input("What does PSU stand for? ")
if answer.lower() == "power supply":
    print("Correct!")
    score += 1
else:
    print("Incorect")


print(f"Thanks for playing! You got {score} questions correct!")
print(f"You got {(score/4 * 100)}% of the questions correct")

if score == 4:
    print("You receive a gold medal!")
if score == 3:
    print("You receive a silver medal")
if score == 2:
    print ("You receive a bronze medal")
if score <= 1:
    print("Sorry, no medal for you")