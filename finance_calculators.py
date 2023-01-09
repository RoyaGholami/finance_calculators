# this while continues asking the question till the user enter correct value
while True:
    print("investment - to calculate the amount of interest you'll earn on your investment")
    print("bond       - to calculate the amount you'll have to pay on a home loan")
    
    # ask user to choose between 'investment' and 'bond' and converted it to lowercase to accept any capitalize form of these two words
    calculation_type = input("Enter either \'investment\' or \'bond\' from the menu above to proceed: ").lower()

    # if user entered an invalid value an error message is shown
    if (calculation_type != "investment" and calculation_type != "bond"):
        print("Invalid input! please enter a valid value")
    else:
        break

# if user selects investment then ask relevant questions 
if (calculation_type == "investment"):
    deposit_amount = float(input("Enter amount of money that they are depositing: "))
    interest_rate = float(input("Enter interest rate: "))
    years = int(input("Enter number of years they plan on investing: "))

    # this while continues asking the question till the user enter correct value
    while True:         
        # ask user to choose between 'simple' and 'compound' and converted it to lowercase to accept any capitalize form of these two words
        interest = input("Do you want simple or compound interest? Enter either \'simple\' or \'compound\': ").lower()

        # if user entered an invalid value an error message is shown
        if (interest != "simple" and interest != "compound"):
            print("Invalid input! please enter a valid value")
        else:
            break

    # calculate total amount based on user selection
    if (interest == "simple"):
        total_amount = round(deposit_amount * (1 + (interest_rate / 100) * years), 2)
    else:
        total_amount = round(deposit_amount * (1 + (interest_rate / 100)) ** years, 2)

    print(f"The amount that they will get back after {years} years is R{total_amount}")

# if user selects bond then ask relevant questions   
else:
    present_value = float(input("Enter present value of the house: "))
    interest_rate = float(input("Enter interest rate: "))
    months = int(input("Enter number of months they plan to take to repay the bond: "))

    # calculate monthly rate
    monthly_interest_rate = (interest_rate / 100) / 12
    
    # calculate monthly repayment amount
    repayment = round((monthly_interest_rate * present_value) / (1 - (1 + monthly_interest_rate)**(-months)),2)

    print(f"The amount the user will have to repay each month is R{repayment}")

