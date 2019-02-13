def numbers2letters(numbers):
    return ''.join([chr(number + ord('A')) for number in numbers])

def combinations():
    numbers = [0, 0, 0, 0]
    while numbers != [25, 25, 25, 25]:
        for i in xrange(len(numbers)):
            if numbers[i] > 25:
                numbers[i] = 0
                numbers[i+1] += 1
        letters = numbers2letters(numbers)
        if (
                letters.find('AB') < 0
            and letters.find('BA') < 0
            and letters.find('ZL') < 0
            and letters.find('LZ') < 0
            and len(set(numbers)) > 2
        ):
            yield letters
        numbers[0] += 1

combos = combinations()
count = 0
while True:
    try:
        combos.next()
        # print(combos.next())
    except StopIteration as e:
        break
    count += 1
    
print count
