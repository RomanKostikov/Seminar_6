# 43. Дана последовательность чисел. Получить список уникальных элементов
# заданной последовательности.
# *Пример:*
# [1, 2, 3, 5, 1, 5, 3, 10] => [2, 10]

"""Doc."""
from random import randint
import os
os.system('cls')

nums = [randint(1, 15) for i in range(21)]
print('Задан список: ', nums, '\n')

# первое решение c filter and lambda
nums1 = list(filter(lambda x: nums.count(x) == 1, nums))
# второе решение for
nums2 = [i for i in nums if nums.count(i) == 1]
# третье решение(множества)
nums3 = list(set(nums))
print('Список уникальных элементов: ', nums1)
print('Список уникальных элементов: ', nums2, '\n')
print('Список уникальных элементов: ', nums3, '\n')
