def gen_fibonacci(n):
    fibonacci_sequence = [0, 1]  # Initialize the sequence with the first two terms
    for i in range(2, n):
        next_term = fibonacci_sequence[-1] + fibonacci_sequence[-2]
        fibonacci_sequence.append(next_term)
    return fibonacci_sequence[:n]

def main():
    try:
        n = int(input("Enter the number of terms for the Fibonacci sequence: "))
        if n <= 0:
            print("Please enter a positive integer.")
        else:
            fibonacci_sequence = gen_fibonacci(n)
            print("Fibonacci Sequence:")
            print(fibonacci_sequence)
    except ValueError:
        print("Please enter a valid integer.")

if __name__ == "__main__":
    main()
