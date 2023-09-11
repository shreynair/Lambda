from functools import reduce


def is_present(lst,x):
  for i in lst:
    if(x == lst[i]):
      return True
  
  return False

def count_occ(lst,target):
  return reduce(lambda x,y: x + (1 if y == target else 0), lst, 0)

def uniq(lst):
  uniq_nums = []
  return list(map(lambda x,y: x if x not in uniq_nums else 0, lst, uniq_nums))

# This is find_max
def find_max(matrix):
  return reduce(lambda x,y: y if y > x else x, matrix)

def count_ones(matrix):
  return reduce(lambda x, y: x + reduce(lambda a, b: a + 1 if b == 1 else a + 0, y, 0), matrix, 0)

def addgenerator(x):
  return lambda y: x + y 

def apply_to_self():
  return lambda e,f: e + f(e)

def ap(fns,args):
  return 0

def map2(matrix,f):
  return list(map(lambda x: list(map(f, x)), matrix))


