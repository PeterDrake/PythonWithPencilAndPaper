nums = [1, 2, 3, 4, 5, 6]
s1 = 0
s2 = 0
for n in nums:
    s1 = s1 + n
    if n >= 3:
        break
    s2 = s2 + n ** 2
s1

s2

s3 = 0
for n in nums:
    if n % 2 == 0:
        continue
    s3 = s3 + n
s3
