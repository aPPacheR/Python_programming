def two_sum(lst, target):
    for i in range(len(lst)):
        for j in range(len(lst)):
            if i != j and lst[i] != lst[j] and lst[i] + lst[j] == target:
                return i, j
    return None

def two_sum_hashed(lst, target):
    seen = {}
    min_pair = None
    for i in range(len(lst)):
        comp = target - lst[i]
        if comp in seen and lst[i] != comp:
            if min_pair is None or (seen[comp], i) < min_pair:
                min_pair = (seen[comp], i)
        if lst[i] not in seen:
            seen[lst[i]] = i
    return min_pair

def two_sum_hashed_all(lst, target):
    seen = {}
    pairs = []
    for i in range(len(lst)):
        comp = target - lst[i]
        if comp in seen and lst[i] != comp:
            pairs.append((seen[comp], i))
        elif lst[i] not in seen:
            seen[lst[i]] = i
    return pairs


lst = [2, 2, 0, 4]
target = 4
print(two_sum_hashed_all(lst, target))