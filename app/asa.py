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

print(simple(100))

def zimple(x):
    accs = []
    for i in sympy.primerange(2,10000):
        if len(accs) < x:
            accs.append(i)
        yield accs

generator = zimple(10000000)
print(next(generator))
print(next(generator))
print(next(generator))
