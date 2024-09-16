def fizzbuzz(n):
    """
    Takes in a positive integer (n) and returns
    what the player should say at that value.
    fizzbuzz(3) returns "Fizz"
    fizzbuzz(15) returns "Fizzbuzz"
    fizzbuzz(2) returns 2
    """
    if n % 3 == 0 and n % 5 == 0:
        return "Fizzbuzz"
    elif n % 3 == 0:
        return "Fizz"
    elif n % 5 == 0:
        return "Buzz"
    else:
        return n

def main():
    MAX_VALUE = 17  # We want to play Fizz Buzz up to 17
    for i in range(1, MAX_VALUE + 1):
        # Call fizzbuzz on every number from 1 to MAX_VALUE
        to_say = fizzbuzz(i)
        print(to_say)

if __name__ == '__main__':
    main()
