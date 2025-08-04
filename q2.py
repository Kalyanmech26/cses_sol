def getWays(mp, i, nums):
    if i < 0:
        return {0}
    if i in mp:
        return mp[i]
    
    mp[i] = set()
    prev_sums = getWays(mp, i-1, nums)

    for s in prev_sums:
        mp[i].add(s)
        mp[i].add(s + nums[i])

    return mp[i]


def main():
    n = int(input())
    nums = list(map(int, input().split()))
    mp = {}
    getWays(mp, n-1, nums)
    print(len(mp[n-1])-1)
    print(*sorted(x for x in mp[n-1] if x != 0))

if __name__ == "__main__":
    main()
