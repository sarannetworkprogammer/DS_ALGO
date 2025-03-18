def fact(n):
    if n == 1:
        return 1
    return( n*fact(n-1))


def main():

    ans = fact(3)
    print(f"ans ={ans}")


main()