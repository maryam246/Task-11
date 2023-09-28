# Example of Counters.
#1.
# with keyword arguments
from collections import Counter
print(Counter(['A','C','B','D','D','A','B','C','C','D','B','D']))

#2.
# with keyword arguments
from collections import  Counter
print(Counter(D = 4,C=3,B=3,A=2))

#3.
# with dictionary
from  collections import Counter
print(Counter({'C':4,'D':3,'B':3,'A':2}))

#4.
import collections
numbers = [1,2,3,34,33,33,2,2,2,1,1,1,1]
count = collections.Counter(numbers)
print(count)
#5.
import collections
words = ['I','am','a','student','of','Virtual','univercity.']
count = collections.Counter(words)
print(count)

#Examples of OrderedDict.
#1.
from collections import OrderedDict
ages = OrderedDict()
ages ['KIran'] = 54
ages ['Ali'] =30
ages ['Noman'] =23
print(ages)

#2.
from collections import OrderedDict
print('This is an Ordered dict.')
od = OrderedDict()
od['a'] = 1
od['b'] = 2
od['c'] = 3
od['d'] = 4

for key,value in od.items():
    print(key,value)

#3.
from collections import OrderedDict
odr = OrderedDict()
odr['Amina'] = 1
odr['Ajmal'] = 2
odr['Arif'] = 3

# deleting element
odr.pop('Amina')
#re- enter the same element
odr['Amina'] = 1
for key,value in odr.items(): # output remember the sequence of intering due to OrderedDict.
    print(key,value)

#4.
import collections
dic = {1:'Oppo',2:'Sumsung',3:'Infinix'}
#Deleted element
dic.pop(1)

o = collections.OrderedDict(dic)
print(o)
# update the element
o.update({1:'Apple'})
print(o)

#5.
from collections import OrderedDict
s = {'Mobile':2023,'Laptop':2019,'Tab':2015}
result = OrderedDict(s)
print(result)

#Example of Defaultdict.
#1.
from collections import defaultdict
s = defaultdict(lambda :22)

result = s['age1']
print(result)

#2.
#default value of int,float,str
i_nt =defaultdict(int)
f_loat =defaultdict(float)
s_tring = defaultdict(str)

show = i_nt['key- 1'],f_loat['key- 1'],s_tring['key- 1']
print(show)
print(i_nt,f_loat,s_tring)

#3.
from collections import defaultdict
L = [3,44,55,3,3,44]
d = defaultdict(int)
for i in L:
    d[i] +=1
print(d)

#4.
from collections import defaultdict
d = defaultdict(list)
for i in range(6):
    d[i].append(i)
print('Dictionary with values as list is: ')
print(d)

#5.
from collections import defaultdict
n = [5.7,6,8]
d = defaultdict(int)
for i in n:
    d[i]+=1
print(d)

#Examples of Chain map.
#1.
from collections import ChainMap
a = {1:'Ali',2:'Nimra'}
b = {1:'book',2:'bag'}
c = {1:'fan',2:'AC'}

result = ChainMap(a,b,c)
print(result)

#2.
from collections import ChainMap
i = {'a':20,'b':30}
j = {'c':70,'d':40}
k = {'e':10,'g':90}

c = ChainMap(i,j,k)
print(c)
# Accessing Values using key name
print(c['d'])
print(c['b'])
print(c['g'])

# Accessing values using values()
# method
print(c.values())
# Accessing keys using keys()
# method
print(c.keys())

#Example of NamedTuple.
#1.
from collections import namedtuple
Date = namedtuple('Date',['Month','Date','Year'])
yesterday = Date(9,27,2023)
today =Date(9,28,2023)
tomorrow = Date(9,29,2023)
print(yesterday)
print(today)
print(tomorrow)

#2.
from collections import namedtuple
student = namedtuple('Student',['name','age','grade'])
s = student('kiran',20,'A')
print(s)

#3.
from collections import namedtuple
Food = namedtuple('Food',('Bryani','Qurma','pulao'))
f =Food(450,500,600)
print(f)
# Access using name
print(f.pulao)
# Access using index
print(f[0])

#Example of Deque.
#1.
from  collections import deque
d = deque('HELLO!')
print(d)
d.appendleft(4)
d.append('world.')
print(d)

#2.
from collections import deque
a = deque('123456')
print(a)
a.pop()
print(a)
a.popleft()
print(a)

#3.
from collections import deque
que = deque([1,2,3,4,4,5])
que.pop()
print(que)
que.append(6)
print(que)

#4.
from collections import deque
de = deque('AH')
de.append(' Khan')
print(de)
de.popleft()
print(de)
de.pop()
print(de)

#Examples of heap.
import  heapq
data = [1,2,3]
heapq.heappush(data,5)
print(data)
heapq.heappush(data,7)
print(data)

#2.
import heapq
heapq.heappop(data)
print(data)

#3.
import heapq
l = [2,34,57,5,8,9]
heapq.heapify(l)
print(l)

#4.
import heapq
n =[1,24,5,6,8,9]
heapq.heappushpop(n,10)
print(n)

#5.
import heapq
v = [19,49,59,66,5]
heapq.heapreplace(v,100)
print(v)

