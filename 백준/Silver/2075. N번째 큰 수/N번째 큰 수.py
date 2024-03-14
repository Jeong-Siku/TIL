n = int(input())
nums = []
for _ in range(n):
    nums+= list(map(int, input().split()))
    nums = sorted(nums, reverse=True)[:n]
print(nums[-1])