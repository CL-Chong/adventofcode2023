import math
from collections import defaultdict


def process_line(s):
    tmp1 = s.split(": ")
    tmp2 = tmp1[0].replace("Card", "")
    qid = int(tmp2)
    tmp3 = tmp1[1].split(" | ")
    winnums = tmp3[0].split(" ")
    winnum_set = {int(x) for x in winnums if x != ""}
    havenums = tmp3[1].split(" ")
    havenum_list = [int(x) for x in havenums if x != ""]
    return qid, winnum_set, havenum_list


def points(winnum_set, havenum_list):
    count = sum(1 for x in havenum_list if x in winnum_set)
    return (2**count) // 2


def wins(winnum_set, havenum_list):
    count = sum(1 for x in havenum_list if x in winnum_set)
    return count


def day04(filename):
    count = 0
    with open(filename, "r") as file:
        for line in file:
            s = line.rstrip()
            _, winnum_set, havenum_list = process_line(s)
            count += points(winnum_set, havenum_list)
    return count


def day04b(filename):
    full = []
    with open(filename, "r") as file:
        for line in file:
            s = line.rstrip()
            full.append(process_line(s))
    # create dict for freq
    cfreq = defaultdict(lambda: -math.inf)
    for tup in full:
        cfreq[tup[0]] = 1
    # loop over full and deposit results in cfreq
    for tup in full:
        current_id = tup[0]
        id_wins = wins(tup[1], tup[2])
        for c in range(current_id + 1, current_id + id_wins + 1):
            cfreq[c] += cfreq[current_id]
    return sum(v for _, v in cfreq.items() if v != -math.inf)


print(day04("day04/test_input.txt"))
print(day04("day04/input.txt"))
print(day04b("day04/test_input.txt"))
print(day04b("day04/input.txt"))
