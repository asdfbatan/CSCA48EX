def edit_distance(s1, s2):
    if len(s1) == 0:
        return 0
    return int(s1[0] != s2[0]) + edit_distance(s1[1:], s2[1:])


def edit_distance2(s1, s2):
    if len(s1) == 0 or len(s2) == 0:
        return max(len(s1), len(s2))
    elif s1[0] == s2[0]:
        return edit_distance2(s1[1:], s2[1:])
    return 1 + min(edit_distance2(s1[1:], s2[0:]),
                   edit_distance2(s1[0:], s2[1:]),
                   edit_distance2(s1[1:], s2[1:]))


def subsequence(s1, s2):
    if s1 == '':
        return True
    elif s2 == '':
        return False
    try:
        return subsequence(s1[1:], s2[s2.index(s1[0]) + 1:])
    except:
        return False


def perms(s):
    if len(s) <= 1:
        return{s}
    permutations = perms(s[1:])
    char = s[0]
    result = set()
    for perm in permutations:
        for i in range(len(perm) + 1):
            result.add(perm[:i] + char + perm[i:])
    return result
