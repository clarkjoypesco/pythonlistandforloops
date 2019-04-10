# We defined:

stooges = ['Moe','Larry','Curly']

# but in some Stooges films, Curly was
# replaced by Shemp.

# Write one line of code that changes
# the value of stooges to be:

# ['Moe','Larry','Shemp']

# but does not create a new List
# object.

stooges[2] = 'Shemp'
print stooges

#testmode

p = ['H', 'e', 'l', 'l', 'o']
q = p
print p
print q
q[0] = 'Y'
print p
print q

#secret agent man
# What is the value of agent[2] after the following code runs?
spy = [0,0,7]
agent = spy
spy[2] = agent[2] + 1

#spy should print 8

print agent[2]



# Define a procedure, replace_spy,
# that takes as its input a list of
# three numbers, and modifies the
# value of the third element in the
# input list to be one more than its
# previous value.


def replace_spy(list):
    list[2] = list[2] + 1
    
spy = [0,0,7]

# In the test below, the first line calls your 
# procedure which will change spy, and the 
# second checks you have changed it.
# Uncomment the top two lines below.
replace_spy(spy)
print spy
#>>> [0,0,8]


#testmode
def inc(n):
    n+=1
    return n

a = 3
print inc(a)
print a

#Testing Length

p = [1,2]
p.append(3)
p = p + [4,5]
print len(p)

#should print 5

#Testing append
p =[1,2]
q = [3,4]
p.append(q)

#p = [1,2,[3,4]]
print len(p)
#should print 3
print p


#Finish the while expression so that this function prints all of the elements of p.

def print_all_elements(p):
    i = 0
    while i < len(p):
        print p[i]
        i = i + 1

list = [1,2,3,4,5]
print_all_elements(list)


print 'Below code is using for loop in python!'
def print_allfor_elements(p):
    for e in p:
        print e

list = [1,2,3,4,5]
print_allfor_elements(list)


# Read through these examples and try to figure out what's going on.
# Press "Test Run" to see what they do.

print "EXAMPLE 1: We can use for loops to go through a list of strings"
example_list_1 = ['a', 'b', 'c', 'd']
for thing in example_list_1:
    print thing
    

print "EXAMPLE 2: We can use for loops on nested lists too!"
example_list_2 = [['China', 'Beijing'],
                  ['USA'  , 'Washington D.C.'],
                  ['India', 'Delhi']]
for country_with_capital in example_list_2:
    country = country_with_capital[0]
    capital = country_with_capital[1]
    print capital + ' is the capital of ' + country



# Define a procedure, sum_list,
# that takes as its input a
# list of numbers, and returns
# the sum of all the elements in
# the input list.

def sum_list(list):
    sum = 0
    for e in list:
        sum += e
    return sum









print sum_list([1, 7, 4])
#>>> 12

print sum_list([9, 4, 10])
#>>> 23

print sum_list([44, 14, 76])
#>>> 134




# Define a procedure, measure_udacity,
# that takes as its input a list of strings,
# and returns a number that is a count
# of the number of elements in the input
# list that start with the uppercase 
# letter 'U'.

def measure_udacity(list):
    found = 0
    for e in list:
        if e[0] == 'U':
            found += 1
    return found



print measure_udacity(['Dave','Sebastian','Katy'])
#>>> 0

print measure_udacity(['Umika','Umberto'])
#>>> 2




# Define a procedure, find_element,
# that takes as its inputs a list
# and a value of any type, and
# returns the index of the first
# element in the input list that
# matches the value.

# If there is no matching element,
# return -1.

def find_element(list, element):
    index = 0
    for e in list:
        if e == element:
            return index
        index +=1
    return -1




print find_element([1,2,3],3)
#>>> 2

print find_element(['alpha','beta'],'gamma')
#>>> -1








