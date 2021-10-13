


def gcf(x, n):

    for i in range (n, 0, -1):
        if ((x % i == 0) and (n % i == 0)):
            return i
    
def quantum_thing(n, guess):
    diffs = []
    p=1
    for i in range (0,20000):
        diff = guess**i % n 
        try:
            last_same = diffs.index(diff)
            p = i - last_same
            break
        except:
            diffs.append(diff)
    return p


if __name__ == "__main__":

    n = int(input("N: "))

    guess = int(input("Guess: "))
    p = quantum_thing(n, guess)
    print(p)
    if p%2 == 0:    
        half_p = p//2
        
        maybe_factor_1 = guess**half_p - 1
        maybe_factor_2 = guess**half_p + 1

        factor_1 = gcf(maybe_factor_1, n)
        factor_2 = gcf(maybe_factor_2, n)
        if (factor_1 * factor_2 == n) : 
            print(factor_1, factor_2)
        else:
            print("retry")
    else:
        print("guess not giving something")