import requests
import json

# responce = requests.get("https://www.nbrb.by/api/exrates/rates/dynamics/145?startdate=2021-01-28&enddate=2021-02-03")
# data = json.loads(responce.text)
# print(data)


import random
from datetime import datetime


# def experiment():
#     ls = []
#     for i in range(4000000):
#         ls.append(random.randint(1, 10 ** 10))
#
#     start = datetime.now
#     for _ in range(100):
#         random.randint(1, 10 ** 10) in ls
#     print("100 раз поискал в списке за" + str((datetime.now() - start)))
#
#     hash = set(ls)
#     start = datetime.now
#     for _ in range(100):
#         random.randint(1, 10 ** 10) in hash
#     print("100 раз поискал в множестве за" + str((datetime.now() - start)))


# print(experiment())


import sympy


# def simple(x):
#     acc = []
#     for i in sympy.primerange(2, 10000):
#         if len(acc) < x:
#             acc.append(i)
#         else:
#             return acc
#
#
# # print(simple(100))
#
# def zimple(x):
#     accs = []
#     for i in sympy.primerange(2, 10000):
#         if len(accs) < x:
#             accs.append(i)
#         yield accs


# generator = zimple(10000000)
# print(next(generator))
# print(next(generator))
# print(next(generator))


def client():
    return requests.post(
        "http://127.0.0.1:8000/person",
        {"id": 1,
         "name": "Oleg",
         "age": 30}
    ).text


# print(client())


# def digit(some):
#     list_digit = len(str(some))
#     result = 0
#     for i in range(list_digit):
#         result += int(str(some)[i])
#     return result


# print(digit(5555))


def su(sd):
    s = 0
    for i in str(sd):
        s += int(i)
    return s


# print(su(123))


def largest_digit(digit):
    result = ""
    for i in range(len(str(digit))):
        result += str(9)
    return result


# print(largest_digit(1))


import pandas
from pandas import concat
from pandas import DataFrame

# df1 = DataFrame({"name": ["Vasya", "Petya", "Ivan"], "age": ["18", "22", "42"], "job": ["Aaaa", "BBB", "CCC"]})
# df2 = DataFrame({"name": ["Oleg", "Ilia"], "age": ["30", "19"], "job": ["Master", "Slomaster"]})
#
# df3 = concat([df2, df1])
#
# df = pandas.read_csv('C:\\Users\\xxx\\Desktop\\Pythom projects/data.csv')


# for job,df5 in df.groupby("job"):
# print(job, df5["age"].sum() / df5.shape[0] )


# df6 = df[df['age'].isin([20, 25])]
# print(df6)


# def reverce():
#     c = []
#     f = ""
#     for i in b:
#         c.append(i)
#         f = c[::-1]
#         for m in f:
#             f[0] += m
#     return str(f[0])
# 
#
# b = "abcdefg"
# n = b[::-1]


# print(reverce())


# def ala():
#     b = []
#     a = {"a": 153, "b": 200}
#     for i in dict.keys(a):
#         b += str(i)
#     return b
#
#
# # print(ala())
#
#
# def string():
#     fff = ["a", "b", "c"]
#     nnn = "".join(fff)
#     return nnn


# print(string())


# def wait_for_processing(fn):
#     def wrapper(*args, **kwargs):
#         print("Ожидайте, идет подсчет")
#         result = fn(*args, **kwargs)
#         print("Подсчет закончен")
#         return result
#
#     return wrapper
#
#
# @wait_for_processing
# def square(a):
#     for i in range(a):
#         print(i ** 2)


# print(square(1000))

# print(list(filter(lambda x: x % 2 == 0, [20,35,40])))

import re


# print(re.match("^\d+$", "9999") is not None)


# def waiter(fn):
#    start = datetime.now()
#    print("Wait, it is calculating")
#    def function(*args, **kwargs):
#        result = fn(*args, **kwargs)
#        print("All did calculated", datetime.now() - start)
#    return function

# @waiter
# def qube(x):
#    for i in range(x):
#        print(i*i*i)

# print(qube(100))

# def capitalizer(fn):
#     def wrapper(*args, **kwargs):
#         line = ""
#         for arg in args:
#             line += arg.capitalize()
#         result = fn(*args, **kwargs)
#         print(result)
#         return line
#
#     return wrapper
#
#
# @capitalizer
# def swap_words(words):
#     tmp = words.split(' ')
#     return tmp[1] + ' ' + tmp[0]
#
#
# print(swap_words("lolek bolek"))
#
#
# def apply_two_times(fn):
#     def wrapper(*args, **kwargs):
#         result = fn(fn(*args, **kwargs))
#         return result
#
#     return wrapper
#
#
# @apply_two_times
# def mult_on_2(ls):
#     result = []
#     for x in ls:
#         result.append(x * 2)
#     return result
#
#
# print(mult_on_2([2, 4, 5, 6, 7]))
#
# import math
#
#
# def positive_number_check(fn):
#     def wrapper(*args, **kwargs):
#         for arg in args:
#             if arg > 0:
#                 return fn(*args, **kwargs)
#             else:
#                 return "Cannot to use numbes, smaller than zero"
#
#     return wrapper
#
#
# @positive_number_check
# def my_sqrt(x):
#     return math.sqrt(x)
#
#
# print(my_sqrt(-25))
#
# print(list(filter(lambda x: x % 2 == 0, [100, 200, 301])))
# print(list(map(lambda x: x + 100, [100, 200, 301])))



#import re

#print(re.match("^a\d+v$", "a11111v") is not None)

import pandas

#dft = DataFrame({"name": ["Oleg", "Alex", "Vitya"],"lastname": ["Alekseev", "Kekov", "Krakov"], "zp":[20,40,60]})

#print(dft[dft["zp"] > 20])
#print(dft.columns)


# dfdf = pandas.read_csv("C:/Users/xxx/Downloads/titanic.csv")
#
# total_on_board = dfdf["Name"].shape[0]
# print("Total on board", total_on_board)
#
# columns = dfdf.columns
# print("Total columns", columns)
#
# men_only = dfdf[(dfdf["Sex"] == "male")].shape[0]
# print("Total men on the board", men_only)
#
# women_only = dfdf[(dfdf["Sex"] == "female")].shape[0]
# print("Total women on the board", women_only)
#
# total_alive = dfdf[dfdf["Survived"] == 1].shape[0]
# alive_percent = (total_alive / total_on_board) * 100
# print("Alive percent is ", alive_percent)
#
# total_alive_men = dfdf[(dfdf["Survived"] == 1) & (dfdf["Sex"] == 'male')].shape[0]
# men_alive_percent = (total_alive_men / total_alive) * 100
# print("Men alive percent is ", men_alive_percent)
#
# lower_class_alive = dfdf[(dfdf["Survived"] == 1) & (dfdf["Pclass"] == 3)].shape[0]
# middle_class_alive = dfdf[(dfdf["Survived"] == 1) & (dfdf["Pclass"] == 2)].shape[0]
# higher_class_alive = dfdf[(dfdf["Survived"] == 1) & (dfdf["Pclass"] == 1)].shape[0]
# lower_class_alive_percent = lower_class_alive / total_alive * 100
# middle_class_alive_percent = middle_class_alive / total_alive * 100
# higher_class_alive_percent = higher_class_alive / total_alive * 100
# print("Lower class alive percent is ", lower_class_alive_percent, " Middle class alive percent is ", middle_class_alive_percent,
#       " Higher class alive percent is ", higher_class_alive_percent)

# info = pandas.read_csv("C:/Users/xxx/Downloads/info.csv")
# marks = pandas.read_csv("C:/Users/xxx/Downloads/marks.csv")
#
# total_info_persons = info["id"].shape[0]
# total_marks_persons = marks["id2"].shape[0]
# difference = total_info_persons - total_marks_persons
#
# print(difference)
#
# inner_tables = info.merge(marks, left_on = "id", right_on = "id2")
# total_matches = info.merge(marks, left_on = "id", right_on = "id2").shape[0]
# total_pupils_without_marks = total_info_persons - total_matches
# print("Pupils with out marks", total_pupils_without_marks)
#
# group_a = inner_tables[inner_tables["race"] == "group A"]
# math_total_group_a = group_a["math"].sum()
# group_a_total = inner_tables[inner_tables["race"] == "group A"].shape
# middle_score_group_a = (math_total_group_a / group_a_total)
# print("The middle score math group A is ", str(middle_score_group_a))
#
#
# outer_table = info.merge(marks, left_on = "id", right_on = "id2", how = "outer").shape[0]
# print(outer_table)
#
# leftjoin_table = info.merge(marks, left_on = "id", right_on = "id2", how = "left").shape[0]
# print(leftjoin_table)
#
# rightjoin_table = info.merge(marks, left_on="id", right_on="id2", how = "right").shape[0]
# print(rightjoin_table)


# def delete_repeat(a):
#     b = set(a)
#     c = list(b)
#     return c
#
# print(delete_repeat([2,3,4,4,5,6,7,7,7,7,7,8,8,9,0]))
#
#
# def repeat(a,b):
#     c = []
#     for i in a:
#         if i in b:
#             c.append(i)
#     return  set(c)
#
#
# print(repeat([2,3,4,5,4,5,6], [2,2,4,3,4,6,6,6]))


#
# def robo_greetings():
#     number = int(input("Number of students in the classroom"))
#     magick = str(number)
#     if magick[-1] == "5" or magick[-1] == "6" or magick[-1] == "7" or magick[-1] == "8" or magick[-1] == "9" or magick[-1] == "0":
#         return number, "Программистов"
#
#     elif magick[-1] == "1" and len(magick) == 1:
#         return number, "Программист"
#
#     elif magick[-1] == "2" or magick[-1] == "3" or magick[-1] == 4 and len(magick) == 1:
#         return number, "Программиста"
#
#     elif magick[-2] == "1" and magick[-1] == "1" or magick[-1] == "2" or magick[-1] == "3" or magick [-1] == "4":
#         return number, "Программистов"
#
#     elif magick[-1] == "1":
#         return number, "Программистов"
#
#     else:
#         return number, "Программиста"
#
# print(robo_greetings())

############################################          HASHES

# def randomfunction():
#     ls = []
#     for _ in range(4000000):
#         ls.append(random.randint(1, 10000000000))
#
#     start = datetime.now()
#     for _ in range(100):
#         random.randint(1, 10000000000) in ls
#     print("Firs operation takes ", datetime.now() - start)
#
#     start = datetime.now()
#     hash = set(ls)
#     for _ in range(100):
#         random.randint(1, 10000000000) in hash
#     print("Second operation takes", datetime.now() - start)
#
#
#     hash2 = {}
#     for i in ls:
#         hash2[i] = True
#
#     start = datetime.now()
#     for _ in range(100):
#         random.randint(1, 10000000000) in hash2
#     print("Third operation takes", datetime.now() - start)
#
# randomfunction()




# a = [1,2,3]
# b = {3,4,5}
# c = {"a" : 5, "b" : 6, "c": 7}
#
# def mutability(y, z, c):
#     y[0] = 10
#     z.add(5)
#     c["a"] = 200
#
# print(mutability(a,b,c))

# a = [4, 7, 1, 3, 6, 9, 2]
# f = int(len(a))
#
# def bubble_sort(som_list):
#     count = 0
#     for i in range(f -1):
#         for i in range(f -1):
#             if a[i] > a[i + 1]:
#                 count += 1
#                 a[i], a[i + 1] = a[i + 1], a[i]
#     return a, count
#
# print(bubble_sort(a))
# print(a)



# def reverce_word():
#     word = "abraham lincoln"
#     list_word = list(word)
#     free = []
#     for i in range(len(word)):
#         free.append(list_word[-1])
#         list_word.pop(-1)
#
#     return "".join(free), word[::-1]
#
# print(reverce_word())
#
# list_comprehantion = [i**3 for i in range(1, 10)]
# print(list_comprehantion)


# def slices():
#
#     aa = int(input("Insert number of biologic students"))
#     bb = int(input("Insert number of informatic students"))
#     first = []
#     second = []
#     if aa == bb:
#         return aa
#     elif aa != bb:
#         for i in range(1, bb + 1):
#             f = aa * i
#             first.append(f)
#         for n in range(1, aa + 1):
#             s = bb * n
#             second.append(s)
#             for same in first:
#                 if same in second:
#                     return same
#
#
# print(slices())


# def decorator(fn):
#     def wrapper(*args, **kwargs):
#         start = datetime.now()
#         result = fn(*args, **kwargs)
#         return "Program was completed for", str((datetime.now() - start).seconds), "seconds"
#     return wrapper
#
# @decorator
# def another_decorated_function():
#     a = random.randint(1, 10000)
#     x = []
#     f = []
#     for i in range(a):
#         x.append(i)
#         for n in x:
#             if n % 2 == 0:
#                 f.append(n)
#     return f
#
# print(another_decorated_function())

#lisst_compreh = [ for i in [2,3,4,5] for j in [7,8,9] if i*j > 30]
#print(lisst_compreh)


# def example():
#     a = int(input("Введите число от которого начинать отсчёт"))
#     b = int(input("До которого числа"))
#     c = int(input("Начало отрезка умножения"))
#     d = int(input("Конец отрезка умножения"))
#     select = []
#     select2 = []
#     k = 0
#     for i in range(((b -a)+1)*((d-c)+1) + b):
#         if c + k <= d and a <= b:
#             print(str(a), " *",  str(c+k), " =", str(a*(c + k)))
#             select.append(a*(c+k))
#             k += 1
#         else:
#             k = 0
#             a += 1
#     return select
#
# #print(example())
#
#
# def examples():
#     a = int(input("Введите число от которого начинать отсчёт"))
#     b = int(input("До которого числа"))
#     c = int(input("Начало отрезка умножения"))
#     d = int(input("Конец отрезка умножения"))
#     s = 0
#     select2 = []
#     k = ""
#     for i in range((b - a) + 1):
#         if a + s <= b:
#             k += str(a+s)
#             k += "\t"
#             print(k)
#             s += 1
#     return k


print(examples())