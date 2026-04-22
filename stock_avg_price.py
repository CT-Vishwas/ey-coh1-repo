# var = value
# while cond:
#     #statements
#     var inc or dec

while True:
    print("AVG Calculator\n1.Calcuate\n2.Quit")
    print("-"*50)

    choice = input("Enter Choice: ")
    if not (choice.isdigit() and int(choice) <=2):
        print("Enter a valid choice")
        print("Exiting......")
        break

    if choice == '1':
        close_prices = list(map(float, input("Enter close prices seperated by space: ").split()))
        avg_price = sum(close_prices) / len(close_prices)
        print(f"Average of prices:{close_prices} is {avg_price}")
    elif choice == '2':
        print("Exiting....")
        break
    else:
        print("Invalid Choice...")
        break