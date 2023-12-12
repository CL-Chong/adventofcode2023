def readvalue(s):
    letters = "abcdefghijklmnopqrstuvwxyz"
    mydict = {ord(x): "" for x in letters}
    strim = s.translate(mydict)
    # print(strim)
    if len(strim) == 0:
        return 0
    return 10 * int(strim[0]) + int(strim[-1])


def catchwords_left(s):
    letter_dict = {
        "one": 1,
        "two": 2,
        "three": 3,
        "four": 4,
        "five": 5,
        "six": 6,
        "seven": 7,
        "eight": 8,
        "nine": 9,
    }
    number_dict = {
        "1": 1,
        "2": 2,
        "3": 3,
        "4": 4,
        "5": 5,
        "6": 6,
        "7": 7,
        "8": 8,
        "9": 9,
    }
    letter_dict.update(number_dict)
    for i in range(0, len(s)):
        for k in list(letter_dict.keys()):
            if i + len(k) <= len(s) and s[i : i + len(k)] == k:
                return letter_dict[k]
    return 0


def catchwords_right(s):
    srev = s[::-1]
    letter_dict = {
        "one": 1,
        "two": 2,
        "three": 3,
        "four": 4,
        "five": 5,
        "six": 6,
        "seven": 7,
        "eight": 8,
        "nine": 9,
    }
    number_dict = {
        "1": 1,
        "2": 2,
        "3": 3,
        "4": 4,
        "5": 5,
        "6": 6,
        "7": 7,
        "8": 8,
        "9": 9,
    }
    letter_dict.update(number_dict)
    for i in range(0, len(srev)):
        for k in list(letter_dict.keys()):
            if i + len(k) <= len(srev) and srev[i : i + len(k)] == k[::-1]:
                return letter_dict[k]
    return 0


def readvalue_b(s):
    return 10 * catchwords_left(s) + catchwords_right(s)


def day01(filename):
    count = 0
    with open(filename, "r") as file:
        for line in file:
            count += readvalue(line.rstrip())
    return count


def day01b(filename):
    count = 0
    with open(filename, "r") as file:
        for line in file:
            count += readvalue_b(line.rstrip())
    return count


print(day01("day01/input.txt"))
print(day01b("day01/input.txt"))
