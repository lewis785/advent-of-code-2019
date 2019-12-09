def calculate_password(start, end):
    total_passwords = 0
    for i in range(start, end):
        if valid_password(i):
            print(i)
            total_passwords += 1
    return total_passwords


def valid_password(password):
    password_string = str(password)
    password = [int(x) for x in str(password)]
    contains_double = False
    for i in range(0, 5):
        if int(password[i]) > int(password[i+1]):
            return False

        if password_string.count(str(password[i])) > 2:
            continue

        if (not contains_double) and (password[i] == password[i+1]):
            contains_double = True

    return contains_double


def main():
    with open("input.txt") as inputFile:
        password_range = inputFile.readline().split('-')
        print(calculate_password(int(password_range[0]), int(password_range[1])))


if __name__ == '__main__':

    main()
