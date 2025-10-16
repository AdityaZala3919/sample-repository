import random

def generate_random_numbers(count, lower=1, upper=100):
    return [random.randint(lower, upper) for _ in range(count)]

def main():
    numbers = generate_random_numbers(10)
    print("Random Numbers:", numbers)
    print("Sum:", sum(numbers))
    print("Average:", sum(numbers) / len(numbers))

if __name__ == "__main__":
    main()