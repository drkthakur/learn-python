from collections import deque
queue=deque(["Gurmeet","Ram","Rahim"])

queue.append("Dera")
queue.append("Sachcha")

print ("-->",queue)

print("Queue pop ", queue.pop())
print("Queue pop left", queue.popleft())

################################################
name=["Dheeru","Kumar","Singh","Faridabad","New Delhi"]

name.append("Mumbai")
name[len(name):]=["Kolkata"]
print(name)

squares=list(map(lambda x:x**2,range(10)))
print(squares)

squares1 =[x**2 for x in range(10)]
print(squares1)

print([(x,y) for x in [1,2,3] for y in [3,4,1] if  x !=y])

print([(x,x**2) for x in range(10)])

from math import pi
print([round(pi,i) for i in range(5)])