def fibonacci(n):
    if n <= 1:
        return n
    else:
        return fibonacci(n-1) + fibonacci(n-2)

        
def main():

    n = 10
    for i in range(n):
        print(fibonacci(i))

if __name__ == "__main__":
    main()
