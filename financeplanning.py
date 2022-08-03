import maincategory
from maincategory import *

def Primary_Category_Prepare():
    print("Savings, Credit, Budgeting")
    Prepare_Secondary_Category = str(input(""))

    if Prepare_Secondary_Category == "Savings":
        Secondary_Category_Savings()
    elif Prepare_Secondary_Category == "Credit":
        Secondary_Category_Credit()
    elif Prepare_Secondary_Category == "Budgeting":
        Prepare_Secondary_Budgeting()
    elif Prepare_Secondary_Category == "return":
        maincategory.Primary_Category()
    else:
        return maincategory.Primary_Category()

def Secondary_Category_Credit():
    print("Sure thing! We have plenty of resources that can help you get familiar with credit. Take a look at these articles!")
    print("top 5 things to do for credit planning: https://northwesternmutual.com")
    return Primary_Category_Prepare()