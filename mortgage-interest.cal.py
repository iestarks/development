def calculate_mortgage(principal, interest_rate, years):
    # Convert annual interest rate to monthly and decimal format
    
    print("principal: ", principal)
    print("interest_rate: ", interest_rate)
    print("years: ", years)
    
    monthly_rate = interest_rate / 100 / 12

    # Convert years to months
    months = years * 12

    # Calculate monthly payment
    payment = principal * (monthly_rate / (1 - (1 + monthly_rate) ** -months))

    return payment

# Test the function
principal = 180000  # loan amount
interest_rate = 7  # interest rate in percent
years = 30  # loan term in years

monthly_payment = calculate_mortgage(principal, interest_rate, years)

print(f"The monthly payment is: ${monthly_payment:.2f}")