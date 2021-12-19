#for tests
'''
a='nirvana'
print(a,'\'yo')

my_list = ['p','r','o','g','r','a','m','i','z']
print(my_list[-1:1:-1])
# Demonstration of list insert() method
odd = [1, 9]
odd.insert(1,3)

print(odd)

odd[2:2] = [5, 7]
print(odd)
print(odd.pop(1))

print(odd)

print('1a$'.isalnum())

for 'c' in 'hacker':
    print(c,end='')

flag=0
while flag==0:
    s=input()
    if len(s)<10:
        continue
    else:
        flag=1
'''

word=input()
v=0
c=0
for letters in word:
    if letters in 'aeiou':
        v=v+1
    else:
        c=c+1
print(v)
print(c)