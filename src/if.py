x = 1
if 1 < 2:
    x = 2
x

if 4 in {1, 2, 3}:
    a = 1
else:
    a = 2
a

def accessory(temp, rain):
    if temp >= 70:
        if rain:
            return 'umbrella'
        else:
            return 'beverage'
    elif temp >= 40:
        return 'jacket'
    else:
        return 'coat'
accessory(59, True)

accessory(70, False)

accessory(33, False)

accessory(72, True)
