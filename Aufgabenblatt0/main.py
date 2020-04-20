# -*- coding: utf-8 -*-


def task2():
    print("############## task2")

    zeros = [0 for _ in range(5)]
    print("zeros", zeros)

    ones = [1 for _ in range(6)]
    print("ones", ones)

    combined = zeros + ones
    print("combined", combined)

    one_to_ten = [x for x in range(1, 11)]
    print("one_to_ten", one_to_ten)

    one_to_ten_combined = one_to_ten + combined
    print("one_to_ten_combined", one_to_ten_combined)

    one_to_ten_set = set(one_to_ten_combined)
    print("one_to_ten_set", one_to_ten_set)

    one_to_ten_set.remove(2)
    print("without 2", one_to_ten_set)

    one_to_ten_set.add("2")
    one_to_ten_set.add(True)
    print("moron list", one_to_ten_set)


def task3():
    print("############## task3")

    numbers = [x for x in range(1, 10)]
    print("numbers", numbers)

    # inx = int(input("Gib einen Index: "))
    inx = 2

    numbers = numbers[:inx][::-1] + numbers[inx:]
    print(numbers)


def scrabble(word: str):
    print("############## scrabble")

    values = {
        "a": 1, "b": 3, "c": 4, "d": 1, "e": 1, "f": 4,
        "g": 2, "h": 2, "i": 1, "j": 6, "k": 4, "l": 2,
        "m": 3, "n": 1, "o": 2, "p": 4, "q": 10, "r": 1,
        "s": 1, "t": 1, "u": 1, "v": 6, "w": 3, "x": 8,
        "y": 10, "z": 3, "ä": 6, "ö": 8, "ü": 6
    }

    score = 0

    for char in word.lower():
        score += values.get(char, 0)

    print(score)


def min_max_stuff():
    numbers = [x for x in range(20)]
    numbers.append(22)

    print("numbers", numbers)
    print("min", min(numbers))
    print("max", max(numbers))

    sum = 0
    for val in numbers:
        sum += val

    print("median", sum / len(numbers))
    print("unterschiedlich", len(set(numbers)))
    print("is_integer", 5.0.is_integer())


if __name__ == "__main__":
    task2()
    task3()
    scrabble("informatikum")
    min_max_stuff()
