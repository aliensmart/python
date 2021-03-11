import random

supplies =  ['pen', 'ruler', 'stapler', 'flamthrowers', 'binder']

'''
    Instead of using the range(len(someList)) technique with a for loop to obtain the 
    integer index of the items in the list, you can call the enumerate() function instead. 
    On each iteration of the loop, enumerate() will return two values: the index of the 
    item in the list, and the item in the list itself
'''
for index, item in enumerate(supplies):
    print('index '+str(index)+' in the supplies is '+ item)

choice = random.choice(supplies)
print(choice)


'''
    The del statement is good to use when you know the index of the value 
    you want to remove from the list. The remove() method is useful when 
    you know the value you want to remove from the list.
'''

spam = ['cat', 'bat', 'rat', 'cat', 'hat', 'cat']

spam.remove('cat')

spam = ['a', 'z', 'A', 'Z']
spam.sort(key=str.lower)