# Summing numbers
from typing import List, Tuple, Any, Union


def my_sum(*sums: int) -> int:
    """Return the summation of all numbers in the arguments"""
    total = 0
    for number in sums:
        total += number
    return total


def my_sum_02(sums: List[int], start: int = 0) -> int:
    """Add an optional starting sum"""
    total = start
    for number in sums:
        total += number
    return total


def my_sum_03(sums: List[int]) -> float:
    """Return the average of the numbers"""
    total = my_sum(*sums)
    return total / (len(sums))


def my_sum_04(words: List[str]) -> Tuple[int, float]:
    """Return the length of the shortest word, the length of the longest word, and the average word length"""
    words.sort(key=len)
    word_length: List[int] = [len(w) for w in words]
    return (word_length[0], word_length[-1], my_sum_03(word_length))


def my_sum_05(objs: List[Any]) -> Union[int, float]:
    """Return the sum of anything which can be turned integer"""
    total: Union[int, float] = 0
    for obj in objs:
        try:
            total += obj
            next
        except TypeError:  # TypeError occurs when str + int
            try:
                total += int(float(obj))
                continue
            except ValueError:  # ValueError occurs when int(str) return no integer
                continue
    return total


if __name__ == "__main__":
    print(my_sum(1, 2, 3, 4, 5))
    print(my_sum_02([1, 2, 3, 4, 5], 20))
    print(my_sum_03([1, 2, 3, 4, 5]))
    print(my_sum_04(["bc", "a", "abcdef", "abc", "e"]))
    print(my_sum_05([1, 2, 3, 4, 5, 6.5, 7.8, "23", "43.2", "abc"]))
