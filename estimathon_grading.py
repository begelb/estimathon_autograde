import math

answers_dict = {
    1: 3_400_000_000,
    2: 1_029,
    3: 5_815,
    4: 56_000_000,
    5: 10_566_880,
    6: 330,
    7: 17_072,
    8: 435_949_100,
    9: 148,
    10: 0,
    11: 39,
    12: 2001,
    13: 343_128
}

while True:

    user_input = input("Enter the problem number (or type 'exit' to stop): ")
    
    if user_input.lower() == 'exit':
        print("Exiting the code.")
        break

    problem_num = int(user_input)

    intvl_min = input("Enter min: ")
    intvl_max = input("Enter max: ")

    print(f"You entered for the problem number: {problem_num}")
    
    try:
        int_min = float(intvl_min)
        formatted_number = f"{int_min:,.0f}"
        print(f"You entered for the min: {formatted_number}")

        int_max = float(intvl_max)
        formatted_number = f"{int_max:,.0f}"
        print(f"You entered for the max: {formatted_number}")

    except:
        print("Invalid input. Please enter a valid number.")

    # Check if the min is less than the max
    if int_max < int_min:
        print("The min value should be less than the max value. Please try again.")

    # Check if the user input is within the range of the answer
    elif int_min <= answers_dict[problem_num] <= int_max:
        print("GOOD interval!")
        # compute score = floor(max/min)
        result = math.floor(int_max / int_min)
        print(f"Score: {result}")

    else:
        print("BAD interval!")

    

