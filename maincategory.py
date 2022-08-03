import sys
from financeplanning import Primary_Category_Prepare

def Primary_Category():
    print("Prepare, Grow, Protect")
    Primary_Category = input("")
    if Primary_Category == "Prepare":
        print("Great, so you're looking to begin strategizing and planning your finances!")
        print("I can provide information on a few subjects that will be great first steps for your path")
        print("What would you like to learn about?")
        Primary_Category_Prepare()
    elif Primary_Category == "Grow":
        Primary_Category_Grow()
    elif Primary_Category == "Protect":
        Primary_Category_Protect()
    else:
        sys.exit(0)