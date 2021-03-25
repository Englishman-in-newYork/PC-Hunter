import requests
import json

# responce = requests.get("https://www.nbrb.by/api/exrates/rates/dynamics/145?startdate=2021-01-28&enddate=2021-02-03")
# data = json.loads(responce.text)
# print(data)


import random
from datetime import datetime


def experiment():
    ls = []
    for i in range(4000000):
        ls.append(random.randint(1, 10 ** 10))

    start = datetime.now
    for _ in range(100):
        random.randint(1, 10 ** 10) in ls
    print("100 раз поискал в списке за" + str((datetime.now() - start)))

    hash = set(ls)
    start = datetime.now
    for _ in range(100):
        random.randint(1, 10 ** 10) in hash
    print("100 раз поискал в множестве за" + str((datetime.now() - start)))


# print(experiment())


import sympy


def simple(x):
    acc = []
    for i in sympy.primerange(2,10000):
        if len(acc) < x:
            acc.append(i)
        else:
            return acc

#print(simple(100))

def zimple(x):
    accs = []
    for i in sympy.primerange(2,10000):
        if len(accs) < x:
            accs.append(i)
        yield accs

#generator = zimple(10000000)
#print(next(generator))
#print(next(generator))
#print(next(generator))



def client():
    return requests.post(
        "http://127.0.0.1:8000/person",
        {"id" : 1,
         "name": "Oleg",
         "age": 30}
    ).text

#print(client())


def digit(some):
    list_digit = len(str(some))
    result = 0
    for i in range(list_digit):
        result += int(str(some)[i])
    return result


#print(digit(5555))



def su(sd):
    s = 0
    for i in str(sd):
        s += int(i)
    return s

#print(su(123))


def largest_digit(digit):
    result = ""
    for i in range(len(str(digit))):
        result += str(9)
    return result

#print(largest_digit(1))


import pandas
from pandas import concat
from pandas import  DataFrame

df1 = DataFrame({"name": ["Vasya", "Petya", "Ivan"], "age": ["18", "22", "42"], "job": ["Aaaa", "BBB", "CCC"]})
df2 = DataFrame({"name": ["Oleg", "Ilia"], "age": ["30", "19"], "job": ["Master", "Slomaster"]})

    
df3 = concat([df2,df1])


df = pandas.read_csv('C:\\Users\\xxx\\Desktop\\Pythom projects/data.csv')

#for job,df5 in df.groupby("job"):
    #print(job, df5["age"].sum() / df5.shape[0] )


#df6 = df[df['age'].isin([20, 25])]
#print(df6)


def reverce():
    c = []
    f = ""
    for i in b:
        c.append(i)
        f = c[::-1]
        for m in f:
            f[0] += m
    return str(f[0])
b = "abcdefg"
n = b[::-1]
#print(reverce())


def ala():
    b = []
    a = {"a": 153, "b" : 200}
    for i in dict.keys(a):
        b += str(i)
    return b

#print(ala())


def string():
    fff = ["a", "b", "c"]
    nnn = "".join(fff)
    return nnn

#print(string())






def wait_for_processing(fn):
    def wrapper(*args, **kwargs):
        print("Ожидайте, идет подсчет")
        result = fn(*args, **kwargs)
        print("Подсчет закончен")
        return result
    return wrapper

@wait_for_processing
def square(a):
    for i in range(a):
        print(i**2)

#print(square(1000))

#print(list(filter(lambda x: x % 2 == 0, [20,35,40])))

import re
#print(re.match("^\d+$", "9999") is not None)


def waiter(fn):
    start = datetime.now()
    print("Wait, it is calculating")
    def function(*args, **kwargs):
        result = fn(*args, **kwargs)
        print("All did calculated", datetime.now() - start)
    return function

@waiter
def qube(x):
    for i in range(x):
        print(i*i*i)

print(qube(100))






