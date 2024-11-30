from itertools import product

def togglechallenge():
    segment_data = [input().strip() for _ in range(3)]
    digits = []
    for i in range(10):
        digit = [segment_data[row][i*3:(i+1)*3] for row in range(3)]
        digits.append(digit)

    input_number_segments = [input().strip() for _ in range(3)]
    num_segments = len(input_number_segments[0]) // 3
    number = []
    for i in range(num_segments):
        segment = [input_number_segments[row][i*3:(i+1)*3] for row in range(3)]
        number.append(segment)

    def is_away(base, target):
        diff_count = 0
        for row1, row2 in zip(base, target):
            for char1, char2 in zip(row1, row2):
                if char1 != char2:
                    diff_count += 1
                    if diff_count > 1:
                        return False
        return diff_count == 1

    possibledigits = []
    for segment in number:
        validdigits = []
        for digit, refsegment in enumerate(digits):
            if segment == refsegment or is_away(segment, refsegment):
                validdigits.append(digit)
        if not validdigits:
            print("Invalid")
            return
        possibledigits.append(validdigits)

    allnumbers = []
    for digitcombination in product(*possibledigits):
        allnumbers.append(int("".join(map(str, digitcombination))))

    print(sum(allnumbers))

togglechallenge()