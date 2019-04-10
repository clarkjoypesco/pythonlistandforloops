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