tel = {'jack': 4098, 'sape': 4139}
print(tel)
tel['guido']=4127
print(tel)

knights = {'gallahad': 'the pure', 'robin': 'the brave'}
for k,v in knights.items():
    print(k,v)

questions=['name','quest','favourite color']
answers=['lancelot','holy grain','blue']

for q,a in zip(questions,answers):
    print('what is your {0}? it is {1}.'.format(q,a))



for i in reversed(range(1,10)):
        print(i)

fruits=["apple","banana","tendua"]

for i in sorted(fruits):
    print(i)