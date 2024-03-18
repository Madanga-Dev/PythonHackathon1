def main():
    try:
        age = int(input("Please enter your age: "))
        if age >= 18:
            print("You are eligible to vote.")
        else:
            print("You are not eligible to vote.")
    except ValueError:
        print("Please enter a valid age as a number.")

if __name__ == "__main__":
    main()
