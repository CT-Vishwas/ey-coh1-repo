"""
This is a sample module
"""

principal = float(input("Enter the Principal: "))
time_in_months = int(input("Enter the time in months: "))
rate_of_interest = float(input("Enter the rate of interest in decimal(Eg: 7% is 0.07):"))

simple_interest = (principal * time_in_months * rate_of_interest) / 100
print(f"The Simple interest is: {simple_interest:.2f}",end="*****")
