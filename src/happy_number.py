def check_happiness(num: int) -> bool:
    """
    Determines if a number is 'happy' using mathematical digit extraction 
    and a history tracker to prevent infinite loops.


    A happy number is a number defined by the following process:
    Starting with any positive integer, replace the number by the sum
    of the squares of its digits in base-ten, and repeat the process
    until the number either equals 1 (where it will stay), or it loops
    endlessly in a cycle that does not include 1. Those numbers for
    which this process ends in 1 are happy numbers.
    """
    history = set()

    while num != 1 and num not in history:
        history.add(num)
        
        # Calculate sum of squares using divmod instead of string conversion
        total_sum = 0
        while num > 0:
            num, digit = divmod(num, 10)
            total_sum += digit ** 2
        
        num = total_sum

    return num == 1

def main():
    user_input = input("Enter a positive integer: ")
    
    try:
        val = int(user_input)
        result = check_happiness(val)
        
        # Display results with clear formatting
        status = "a Happy Number! :)" if result else "not a Happy Number. :("
        print(f"The number {val} is {status}")
        
    except ValueError:
        print("Invalid input. Please enter an integer.")

if __name__ == "__main__":
    # Test Suite
    test_cases = {7: True, 45: False, 44: True, 69: False}
    
    for number, expected in test_cases.items():
        assert check_happiness(number) == expected
    
    print("Verification successful: All internal tests passed.")
    main()