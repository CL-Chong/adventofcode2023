# get input as matrix m[i][j] i: row index
# get a dict {(i,j) : num in string form}
# get a defaultdict{(i,j): True} for symbols
# get a function adjacent that gets a list of adjacent coords to a num

from collections import defaultdict


def getnum(m):
    numdict = {}
    num_charlist = set(["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"])
    for i, line in enumerate(m):
        isnewnumber = True
        for j, x in enumerate(line):
            if x in num_charlist:
                if isnewnumber is True:
                    current_hash = (i, j)
                    numdict[current_hash] = x
                    isnewnumber = False
                else:
                    numdict[current_hash] += x
            else:
                isnewnumber = True
    return numdict


def havenum(numdict):
    havenumdict = defaultdict(lambda: None)
    for k, v in numdict.items():
        for j in range(0, len(v)):
            havenumdict[(k[0], k[1] + j)] = v
    return havenumdict


def getsymbols(m):
    symdict = defaultdict(lambda: False)
    irrel_charlist = set([".", "0", "1", "2", "3", "4", "5", "6", "7", "8", "9"])
    for i, line in enumerate(m):
        for j, x in enumerate(line):
            if x not in irrel_charlist:
                symdict[(i, j)] = True

    return symdict


def getgears(m):
    gdict = defaultdict(lambda: False)
    for i, line in enumerate(m):
        for j, x in enumerate(line):
            if x == "*":
                gdict[(i, j)] = True
    return gdict


def calc_power(gear_coord, havenumdict):
    i = gear_coord[0]
    j = gear_coord[1]
    tl = (i - 1, j - 1)
    t = (i - 1, j)
    tr = (i - 1, j + 1)
    l = (i, j - 1)
    r = (i, j + 1)
    bl = (i + 1, j - 1)
    b = (i + 1, j)
    br = (i + 1, j + 1)
    unique_nums = []
    if havenumdict[l] is not None:
        unique_nums.append(int(havenumdict[l]))
    if havenumdict[r] is not None:
        unique_nums.append(int(havenumdict[r]))
    if havenumdict[t] is not None:
        unique_nums.append(int(havenumdict[t]))
    else:
        if havenumdict[tl] is not None:
            unique_nums.append(int(havenumdict[tl]))
        if havenumdict[tr] is not None:
            unique_nums.append(int(havenumdict[tr]))
    if havenumdict[b] is not None:
        unique_nums.append(int(havenumdict[b]))
    else:
        if havenumdict[bl] is not None:
            unique_nums.append(int(havenumdict[bl]))
        if havenumdict[br] is not None:
            unique_nums.append(int(havenumdict[br]))

    if len(unique_nums) == 2:
        return unique_nums[0] * unique_nums[1]
    else:
        return 0


def nhood_list(num_coord, num_length):
    i = num_coord[0]
    j = num_coord[1]
    nlist = [(i, j - 1), (i, j + num_length)]
    nlist += [(i - 1, j + v) for v in range(-1, num_length + 1)]
    nlist += [(i + 1, j + v) for v in range(-1, num_length + 1)]
    return nlist


def is_part_number(num_coord, num_length, symdict):
    nlist = nhood_list(num_coord, num_length)
    for tup in nlist:
        if symdict[tup] is True:
            return True
    return False


def day03(filename):
    m = []
    with open(filename, "r") as file:
        for line in file:
            m.append(line.rstrip())
    numdict = getnum(m)
    symdict = getsymbols(m)
    # print(symdict)
    count = 0
    for k, v in numdict.items():
        if is_part_number(k, len(v), symdict):
            count += int(v)

    return count


def day03b(filename):
    m = []
    with open(filename, "r") as file:
        for line in file:
            m.append(line.rstrip())
    numdict = getnum(m)
    gdict = getgears(m)
    havenumdict = havenum(numdict)
    # print(symdict)
    count = 0
    for k, _ in gdict.items():
        count += calc_power(k, havenumdict)
    return count


print(day03("day03/test_input.txt"))
print(day03("day03/input.txt"))
print(day03b("day03/test_input.txt"))
print(day03b("day03/input.txt"))
