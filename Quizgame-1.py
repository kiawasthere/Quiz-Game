

print("welcome to my computer game")

playing = input("Do you want to play? ")

if playing.lower() != "yes":
    quit()

print("Okay! Let's play: )") 

answer = input("what does CPU stand for? ").lower()
if answer == "central processing unit":
    print('Correct!')
    score +- 1
    
else: 
    print("Incorrect!")


answer = input("what does GPU stand for? ").lower()
if answer == "graphics processing unit":
    print('Correct!')
    score +- 1
else: 
    print("Incorrect!")

answer = input("what does RAM stand for? ").lower()
if answer == "random access memory":
    print('Correct!')
    score +- 1
else: 
    print("Incorrect!")

print("You got " + str(score) + " questions correct!")
print("You got " + str((score / 4) * 100) + " %.")
