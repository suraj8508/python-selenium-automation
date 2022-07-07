#numbers = [34, 45, 54, 65 , 56, 77, 87, 89, 98 , 97]


def find_max(numbers):
    maxi = numbers[0]
    for number in numbers:
        if number > maxi:
            maxi = number

    return maxi


def lbs_to_kgs(weight):
    return weight * 0.45

def kgs_to_lbs(weight):
    return weight / 0.45

