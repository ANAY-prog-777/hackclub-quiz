print("Welcome to the quiz!!!!!!!!!!")

print("TOPIC --> HACKCLUB")
print("RULES")
print("1. You will be given 10 questions.")
print("2. 1 QUESTION = 1 POINT AND NO NEGTIVE MARKING")
print("LET'S START THE QUIZ")




quiz = input("DO U WANT TO PLAY THE QUIZ?? (YES OR NO)").upper()

if quiz == "YES":
    print("LET'S START THE QUIZ")
    
    score = int(0)
else:
    print("OKAY, SEE U ANOTHER TIME ;}")
    exit()
    
 
question = input("Who are the two co-founders of Hack Club? ").upper()
if question == "ZACH LATTA AND SARA MAHMOUD".upper():
    print("CORRECT ANSWER")
    score = score + 1
else:
    print("WRONG ANSWER")


question = input("What is the name of the handheld game console created by Hack Club that was distributed for free to teen makers?  ").upper()
if question == "sprig".upper():
    print("CORRECT ANSWER")
    score = score + 1
else:
    print("WRONG ANSWER")




question = input("Which communication platform does the Hack Club community use for daily discussions and project sharing? ").upper()
if question == "SLACK".upper():
    print("CORRECT ANSWER")
    score = score + 1
else:
    print("WRONG ANSWER")




question = input("What does 'HCB' stand for in the context of Hack Club's financial tools?  ").upper()
if question == "hack club bank".upper():
    print("CORRECT ANSWER")
    score = score + 1
else:
    print("WRONG ANSWER")





question = input("What is the primary mission of Hack Club regarding teenagers and technology? ").upper()
if question == "To help teens gain technical skills through open-source projects, friendships, and adventures".upper():
    print("CORRECT ANSWER")
    score = score + 1
else:
    print("WRONG ANSWER")





question = input("What is the name of the teen volunteers who help new members navigate the Slack community? ").upper()
if question == "gardeners".upper():
    print("CORRECT ANSWER")
    score = score + 1
else:
    print("WRONG ANSWER")




question = input("What is the name of the summer engineering challenge launched by Hack Club, AMD, and NASA in 2026? ").upper()
if question == "STARDANCE".upper():
    print("CORRECT ANSWER")
    score = score + 1
else:
    print("WRONG ANSWER")





question = input("What is the name of the Hack Club channel where members share their work-in-progress projects? ").upper()
if question == "scrapbook".upper():
    print("CORRECT ANSWER")
    score = score + 1
else:
    print("WRONG ANSWER")






question = input("What is the name of the Hack Club team responsible for moderation and upholding the Code of Conduct? ").upper()
if question == "Fire Department".upper():
    print("CORRECT ANSWER")
    score = score + 1
else:
    print("WRONG ANSWER")




question = input("In which U.S. state is the Hack Club headquarters located?  ").upper()
if question == "VERMONT".upper():
    print("CORRECT ANSWER")
    score = score + 1
else:
    print("WRONG ANSWER")


print("YOUR FINAL SCORE OUT OF 10 IS--->", score)
if score >= 5:
    print("Congrats, you got some ball knowledge about Hack clubs!!")
else:
    print("You did great but you can do better, try again to get a higher score!!")





print("Thank you for playing the quiz!")

print("MADE BY ANAY")
print("Hope, we meet again in another project :))")
print("BYE BYE!!")