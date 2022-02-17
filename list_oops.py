def append(list1, list2):
    return list1 + list2
def concat(lists):
    result = []
    for l in lists:
        for i in l:
            result.append(i)
    return result
def filter(function, list):
    l = []
    for i in list:
        if function(i):
            l.append(i)
    return l
def length(list):
    return len(list)
def map(function, list):
    l = []
    for i in list:
        l.append(function(i))
    return l
def foldl(function, list, initial):
    result = initial
    for i in list:
        result = function(result, i)
    return result
def foldr(function, list, initial):
    result = initial
    for i in list[::-1]:
        result = function(i, result)
    return result
def reverse(list):
    return list[::-1]
