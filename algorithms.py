# Concatenations Sum
def concatenationsSum(a):
    # output = 0
    # for i in a:
    #     for j in a:
    #         output += int(str(i) + str(j))
    # return output
    return sum(int(str(x) + str(y)) for x in a for y in a)

# Fibonacci Numbers
def fibonacciNumbers(a):
    output = [0, 1, 1]
    for i in range(3, a):
        output.append(output[i-1] + output[i-2])
    return output

# Mutate The Array
def mutateTheArray(n, a):
    # b = []
    # b.append(a[0] + a[1])

    # for i in range(1, len(a)-1):
    #     b.append(a[i-1] + a[i] + a[i+1])
    
    # b.append(a[-2] + a[-1])
    # return b
    return [a[0]+a[1]]+[sum(a[x-1:x+2])for x in range(1,len(a))]if n>1 else a

# Count Tiny Pairs
def countTinyPairs(a, b, k):
    output = 0
    # for i, j in zip(a, b):
    #     x = str(i) + str(j)
    #     if int(x) < k:
    #         output += 1
    # return output

    return sum([1 if int(str(x)+str(y))<k else 0 for x,y in zip(a,b)])


# Mean Groups
def meanGroups(a):
    groups = {}
    for i, lst in enumerate(a):
        mean = sum(lst) / len(lst)
        if mean not in groups:
            groups[mean] = []
        groups[mean].append(i)
    return list(groups.values())
    # d,e=[],[]
    # for i,j in enumerate(a):
    #     if sum(j)/len(j)not in e:
    #         e+=[sum(j)/len(j)]
    #         d+=[[i]]
    #     else:
    #         d[e.index(sum(j)/len(j))]+=[i]
    # return d

# Alternating Sort
def alternatingSort(a):
    n = len(a)
    for i in range(n//2):
        if a[i] >= a[n-i-1]:
            return False
    return True
    return [False if (a[i] >= a[len(a)-i-1] for i in range(len(a)//2)) else True] 
    c,l=0,a[0]
    while c!=(len(a)-1)//2:
        c=-c if c<0 else -c-1
        if a[c]<=l:
            return False
        l=a[c]
    return True

# Merge Strings
def mergeStrings(s1, s2):
    result = ''
    while s1 and s2:
        if s1[0] < s2[0]:
            result += s1[0]
            s1 = s1[1:]
        else:
            result += s2[0]
            s2 = s2[1:]
    return result + s1 + s2

    s,o1,o2='',s1,s2
    while len(s1)*len(s2)!=0:
        if o1.count(s1[0])>o2.count(s2[0]) or (o1.count(s1[0])==o2.count(s2[0]) and s1[0]>s2[0]):
            print(o1.count(s1[0]))
            s+=s2[0]
            s2=s2[1:]
        else:
            s+=s1[0]
            s1=s1[1:]
    return s+s1+s2


def hashMap(queryType, query):
    # hash = {}
    # sum = 0
    # key_addition = 0
    # value_addition = 0

    # for i, j in zip(queryType, query):
    #     if i == 'insert':
    #         hash[j[0]-c1] = j[1]-c2



    d,s,c1,c2={},0,0,0
    for i,j in zip(queryType,query):
        if i == 'insert':
            d[j[0]-c1]=j[1]-c2
            print(d)
        elif i == 'addToValue':
            c2+=j[0]
        elif i == 'addToKey':
            c1+=j[0]
        # elif i== 'get':
            # print(d[j[0]-c1])
            # s+=d[j[0]-c1]+c2
    return s

def solution(password, key):
    table = {i:ord(key[j]) for i, j in zip(range(97, 123), range(len(key)))}
    return password.translate(table)

def billboard(t, width, precision):
    return "{:^{width}.{precision}f}".format(t, width=width, precision=precision)
    
# def solution(inputArray):
#     output = 0
#     for i in range(len(inputArray)-1):
#         x = inputArray[i] * inputArray[i + 1]
#         if x > output:
#             output = x
#     print(output)
#     return output

def solution(ids):
    digitsum = sum([int(j) for j in str(ids)])

    # for i in ids:
    #     y = str(i)
    #     for j in y:
    #         digitsum = digitsum + int(j)
    return digitsum

print(solution(1234))
# print(concatenationsSum([1, 2]))
# print(fibonacciNumbers(20))
# print(mutateTheArray(10, [1, 4, 3]))
# print(countTinyPairs([1, 2, 3], [4, 5, 6], 50))
# print(meanGroups([[1, 2, 3], [1, 2, 3], [3, 4]]))
# print(alternatingSort([1, 2, 2, 5, 4, 7, 6, 9, 8]))
# print(mergeStrings('hello', 'awais'))
# print(hashMap(['insert', 'addToKey', 'insert', 'get', 'addtoValue', 'insert', 'get'], [[2, 5], [4], [4, 2], [1], [-7], [4, -2], [-5]]))
# print(billboard(3.1415, 10, 2))