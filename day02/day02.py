from collections import defaultdict


def process_line(s):
    t0 = s.split(": ")
    idstr = t0[0]
    gstr = t0[1]
    ids = int(idstr.split(" ")[1])
    gstr_pl = gstr.split("; ")
    glist = []
    for gs in gstr_pl:
        tmp = defaultdict(lambda: 0)
        gsl = gs.split(", ")
        for item in gsl:
            itemx = item.split(" ")
            tmp[itemx[1]] = int(itemx[0])
        glist.append(tmp)

    return ids, glist


def is_permissible(glist, truedict):
    for k, v in truedict.items():
        for d in glist:
            if d[k] > v:
                return False
    return True


def min_dict(glist):
    mindict = {"red": 0, "blue": 0, "green": 0}
    for d in glist:
        for k, v in d.items():
            mindict[k] = max(v, mindict[k])
    return mindict


def power(mindict):
    return mindict["red"] * mindict["blue"] * mindict["green"]


def day02(filename):
    count = 0
    truedict = {"red": 12, "blue": 14, "green": 13}
    with open(filename, "r") as file:
        for line in file:
            s = line.rstrip()
            ids, glist = process_line(s)
            if is_permissible(glist, truedict):
                count += ids
    return count


def day02b(filename):
    count = 0
    # truedict = {"red": 12, "blue": 14, "green": 13}
    with open(filename, "r") as file:
        for line in file:
            s = line.rstrip()
            _, glist = process_line(s)
            count += power(min_dict(glist))
    return count


print(day02("day02/input.txt"))
print(day02b("day02/input.txt"))
# s = "Game 4: 1 green, 3 red, 6 blue; 3 green, 6 red; 3 green, 15 blue, 14 red"
# ids, glist = process_line(s)
# truedict = {"red": 15, "blue": 20, "green": 10}
# print(is_permissible(glist, truedict))

# i = 0
# for d in glist:
#     i += 1
#     print(i)
#     for k, v in d.items():
#         print(k, v)
