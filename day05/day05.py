import itertools
from collections import defaultdict


def offsetmap(tups):
    def _f(x):
        offset = 0
        for tup in tups:
            dst, src, leng = tup
            if x in range(src, src + leng):
                offset = dst - src
        return x + offset

    return _f


def findinverse(target, tups):
    for dst, src, leng in tups:
        if target in range(dst, dst + leng):
            delta = target - dst
            return src + delta
    return target


def findallinverse(target, tups):
    ans = [target]
    for dst, src, leng in tups:
        if target in range(dst, dst + leng):
            delta = target - dst
            ans += [src + delta]
    return ans


def sorted_keys(mappings):
    list_keys_full = [k for k, _ in mappings.items()]
    list_keys = []
    kw = "seed"
    while len(list_keys_full) > 0:
        for s in list_keys_full:
            if s.startswith(kw):
                list_keys.append(s)
                list_keys_full.remove(s)
                tmp = s.split("-to-")
                kw = tmp[1]
    # print(list_keys)
    return list_keys


def day05(filename):
    mappings_data = defaultdict(list)

    with open(filename, "r") as file:
        for line in file:
            s = line.rstrip()
            if len(s) == 0:
                continue
            s = s.split(" ")
            if s[0] == "seeds:":
                seeds = [int(x) for x in s[1:]]
            elif s[-1] == "map:":
                active_field = s[0]
            else:
                mappings_data[active_field].append([int(x) for x in s])

    mappings = {k: offsetmap(v) for k, v in mappings_data.items()}
    list_keys = sorted_keys(mappings)

    def _seedmap(x):
        result = x
        for k in list_keys:
            result = mappings[k](result)
        return result

    loc_list = [_seedmap(x) for x in seeds]

    return min(loc_list)


def day05b(filename):
    mappings_data = defaultdict(list)

    with open(filename, "r") as file:
        for line in file:
            s = line.rstrip()
            if len(s) == 0:
                continue
            s = s.split(" ")
            if s[0] == "seeds:":
                seeds = [int(x) for x in s[1:]]
            elif s[-1] == "map:":
                active_field = s[0]
            else:
                mappings_data[active_field].append([int(x) for x in s])

    mappings = {k: offsetmap(v) for k, v in mappings_data.items()}
    list_keys = sorted_keys(mappings)

    corners = [src for _, src, _ in mappings_data[list_keys[-1]]]
    rev_keys = list_keys[::-1]
    for i, k in enumerate(rev_keys):
        if i >= 1:
            newcorners = list(
                itertools.chain.from_iterable(
                    findallinverse(x, mappings_data[k]) for x in corners
                )
            )
            # newcorners += [min(corners), max(corners)]
            corners = list(newcorners) + [src for _, src, _ in mappings_data[k]]

    def _seedmap(x):
        result = x
        for k in list_keys:
            result = mappings[k](result)
        return result

    def _min_from_range(st, rg):
        ed = st + rg - 1
        return min(_seedmap(x) for x in [st, *corners, ed] if st <= x <= ed)

    # loc_list = [_seedmap(x) for x in seeds]
    seed_st = seeds[0:-1:2]
    seed_rg = seeds[1::2]
    minlist = []
    for st, rg in zip(seed_st, seed_rg):
        min_i = _min_from_range(st, rg)
        # print(min_i)
        minlist += [min_i]
    return min(minlist)


print(day05("day05/test_input.txt"))
print(day05("day05/input.txt"))
print(day05b("day05/test_input.txt"))
print(day05b("day05/input.txt"))
