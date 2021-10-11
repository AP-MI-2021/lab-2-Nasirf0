def get_largest_prime_below(n):
    """
    input: integer
    returns the largest prime number below the given n
    """
    try:
        n = int(n)
    except:
        return None
    if n < 1:
        return None
    elif n == 1 or n == 2:
        return n
    for number in reversed(range(1, n)):
        if number % 2 != 0:
            prime = True
            for divisor in range(3, int(number / 2), 2):
                if number % divisor == 0:
                    prime = False
            if prime == True:
                return number


def is_palindrome(n):
    """
    input: integer
    return True if the given n is a palindrom, False otherwise
    """
    if int(n) < 0:
        n = 0 - int(n)
    n_copy = int(n)
    palindrom = 0
    while (n):
        digit = n % 10
        palindrom = palindrom * 10 + digit
        n = n // 10
    if palindrom == n_copy:
        return True
    return False

def is_antipalindrome(n) -> bool:
    """
    input: integer
    return True if the given n is an antipalindrom, False otherwise
    """
    try:
        n= int(n)
    except:
        return False
    copy = n
    length = 0
    list = []
    while copy != 0:
        length = length + 1
        copy = copy // 10
    copy = n
    if length == 1:
        return False
    for index in range(length):
        list.append(copy % 10)
        copy = copy // 10
    for index in range(length//2):
        if list[index] == list[length-index-1]:
            return False
    return True

def test_is_antipalindrom():
    assert (is_antipalindrome(2773) == False)
    assert (is_antipalindrome(2345) == True)
    assert (is_antipalindrome(1) == False)

def test_get_largest_prime_below():
    assert (get_largest_prime_below(39) == 37)
    assert (get_largest_prime_below(12) == 11)
    assert (get_largest_prime_below(121) == 113)


def test_is_palidrom():
    assert (is_palindrome(33) == True)
    assert (is_palindrome(121) == True)
    assert (is_palindrome(12) == False)


def main():
    test_get_largest_prime_below()
    test_is_palidrom()
    while True:
        print(
            "Alegeti o optiune:\n 1. Afisati cel mai mare numar prim mai mic decat x. \n 2.Verifica daca x este palindrom \n 3.Verifica daca x este antipalidnrom \n 4.exit")
        option = input("Optiunea voastra: ")
        if option == "1":
            number = input("Introduceti valoarea lui x: ")
            print(f"Cel mai mic numar prim mai mic decat {number} este {get_largest_prime_below(number)}")
        elif option == "2":
            number = int(input("Introduceti valoarea lui x: "))
            print(is_palindrome(int(number)))
        elif option == "3":
            number = input("Introduceti valoarea lui x: ")
            print(f"{number} == antipalindrom: {is_antipalindrome(number)}")
        elif option == "4":
            break
        else:
            print("Valoarea introdusa nu este corecta!")


if __name__ == "__main__":
    main()
