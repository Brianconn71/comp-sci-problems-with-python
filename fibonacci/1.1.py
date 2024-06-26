def fib1(n: int) -> int:
    return fib1(n-1) + fib1(n - 2)

if __name__ == "__main__":
    print(fib1(5))
    
    # This will run forever as every call to fib1 resulkts in two more calls to fib1