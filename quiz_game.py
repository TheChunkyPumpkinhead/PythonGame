#this is the -print function-
print("Welcome to my computer quiz game!")

#varaiable that uses the input funtion 
playing = input("Do you want to play? ")

#if statement answering the playing variable with a quit function
if playing.lower() != "yes":
    quit()

print("Awesome! Let's do this") 

#variable to keep score
score = 0 


#variable to get input from user and an if statement
answer = input("Are you using a computer? ")
if answer.lower() == "yes":
    print("Correct!")
    score += 1
else:
    print("Incorrect")

answer = input("Is the sky up? ")
if answer.lower() == "yes":
    print("Correct!")
    score += 1
else:
    print("Incorrect")

answer = input("Do cats meow? ")
if answer.lower() == "yes":
    print("Correct!")
    score += 1
else:
    print("Incorrect")

answer = input("Do dogs bark? ")
if answer.lower() == "yes":
    print("Correct!")
    score += 1
else:
    print("Incorrect")

answer = input("Do turtles swim? ")
if answer.lower() == "yes":
    print("Correct!")
    score += 1
else:
    print("Incorrect")
  
print("You got " + str(score) + " questions correct!")
print("You got " + str((score / 5) * 100) + "%.")



