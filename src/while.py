x = 1
sum = 0
while x <= 5:
    sum = sum + x
    x = x + 1
sum

word = 'indivisible'
i = 0
while i < 5:
    i = i + 1
word[:i]

result = ''
i = 0
while i < 5:
    result = result + f'<{i}'
    i = i + 1
    result = result + '>'
result

nums = [1, 2, 3]
[n * 2 for n in nums]

result = []
i = 0
while i < len(nums):
    result.append(nums[i] * 2)
    i = i + 1
result
