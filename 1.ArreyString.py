
# if a string has all unique characters

print('1.1. Implement an algorithm to determine of a string has all unique characters  What if you cannot use additional data structures ?')

"""
A good review
http://codereview.stackexchange.com/questions/96630/determine-if-string-has-all-unique-characters
 
# to analyse the time omplexity:
# https://www.ics.uci.edu/~pattis/ICS-33/lectures/complexitypython.txt
# https://wiki.python.org/moin/TimeComplexity
"""

####################################################################################
print('####################################################################################')

print('# 1. using the set data type: len() and set() both have time time complexity of O(1)')
def isuniq1(s):
    return len(set(s)) == len(s)

print isuniq1('hello') 
print isuniq1('bus') 
""" 
discussion: time constant, space O(N) at most : number of characters are limited therefore constant
This one liner has the very precise meaning of "iterate over the chars or my_string, storing them in a hash-table;
when done, fetch the total number of items stored in the hash-table, fetch the total number of items in my_string,
and compare them for equality," which is a perfectly valid algorithm.
  	 	
As for it's time complexity, insertion into a hash table is, for all practical purposes, amortized constant time,
and the hash table itself takes up space proportional to the number of items stored. So you can confidently say
in an interview that set(my_string) is O(n) time and space, perhaps throwing in "amortized." If you were to find
the pedantic interviewer, you could argue that, in Python's implementation, there are no collisions in a 32 or 64
item hash table where the keys are single characters in a-z, so the insertion time is indeed constant.

Getting the length of both a string and a set are constant time in Python, so your one-liner takes amortized
linear time and space on the length of the input string. If the interviewer wanted you to do differently, he
would hardly say that this is not an algorithm, but ask you e.g. to return the position of the first duplicate
found in the string, which would force you to do by yourself a little more of what Python was doing for you in
the previous answer
"""

####################################################################################
print('#2 for loop has O(len(s))')
def isuniq2(s):
    sets=set()  											 # creates an empty set
    for c in s:
        if c in sets:
            return False
        sets.add(c)
    return True

print isuniq2('hello') 
print isuniq2('bus') 

####################################################################################
print('#3 by sorting : Time: O(nlog(n)) ')

def isuniq3(s):
    prev_char = None
    ss = sorted(s)
    for c in ss:
        if c == prev_char :
            return False
        prev_char = c
    return True

print isuniq3('hello') 
print isuniq3('bus') 

####################################################################################
print('# OPTION 4: Array/list way')
# Time: O(n)   Space: O(1) but influenced by the list of length 96
def isuniq4(s):
    if len(s)>96:
        return False
    clist = [False] * 96
    for c in s:
        # take list position by taking ascii position - 32 (amount of control characters)
        idx = ord(c)-32
        if clist[idx]:
            return False
        clist[idx] = True
    return True

print isuniq4('hello') 
print isuniq4('bus') 
####################################################################################
print('#5: bitwise attempt')
# only consider lowercase character a-z, which fits in 4 bytes.
# Time: O(n)   Space: O(1) => 4 bytes.
def isuniq5(s):
    # each bit represents the presence of a character or not (e.g. bit position 0 represents 'a')
    check = 0
    for c in s:
        idx = ord(c)-ord('a')
        if (check & (1 << idx)) > 0:
            return False
        check |= (1 << idx)              # check = check | (1 << idx)
    return True

print isuniq5('abcdc')
print isuniq5('bus') 
####################################################################################
print('####################################################################################')

print(' a bit about bit attempts ')

# bit manipulation
# bin(41)                     # Convert to binary
# int('101001',2)             # Convert to int from binary

a = 60            # 60 = 0011 1100 
b = 13            # 13 = 0000 1101 
c = 0

c = a & b;        # 12 = 0000 1100
print "Line 1 - Value of c is ", c

c = a | b;        # 61 = 0011 1101 
print "Line 2 - Value of c is ", c

c = a ^ b;        # 49 = 0011 0001
print "Line 3 - Value of c is ", c

c = ~a;           # -61 = 1100 0011
print "Line 4 - Value of c is ", c

c = a << 2;       # 240 = 1111 0000
print "Line 5 - Value of c is ", c

c = a >> 2;       # 15 = 0000 1111
print "Line 6 - Value of c is ", c

####################################################################################
print('####################################################################################')
print('1.2.Checking if two strings are permutations of each other ')

def ispermut1(s1,s2):
    if len(s1) <> len(s2):
        return False
    ss1 = sorted(s1)
    ss2 = sorted(s2)
    for i in range(len(ss1)):
        if ss1[i] <> ss2[i]:
            return False
    return True

print ispermut1('budgdsss', 'ddssgubs')            # true
print ispermut1('budddssdsse', 'dsdsdsssubs')     # false

####################################################################################

def ispermut2(s1,s2):
    d={}
    for c in s1:
        d[c] = d.get(c, 0) + 1     # return value from a key  if no key then return the default: get(key, default)
    for c in s2:
        d[c] = d.get(c, 0) - 1
    for v in d.itervalues():        # all the values
        if v != 0:
            return False
    return True

print ispermut2('budgdsss', 'ddssgubs')            # true
print ispermut2('budddssdsse', 'dsdsdsssubs')     # false
####################################################################################
""" second method can be implemented by bit as well"""

# for ascii string only
def ispermut3(s1,s2):
    ccount = [0] * 256
    for c in s1:
        ccount[ord(c)] += 1
    for c in s2:
        ccount[ord(c)] -= 1
        if ccount[ord(c)] < 0:
            return False
    return True

print ispermut3('budgdsss', 'ddssgubs')            # true
print ispermut3('budddssdsse', 'dsdsdsssubs')     # false

####################################################################################
# another emplimentation
import collections
def same_permutation(a, b):
    d = collections.defaultdict(int)
    for x in a:
        d[x] += 1
    for x in b:
        d[x] -= 1
    return not any(d.itervalues())
####################################################################################
print('####################################################################################')
print('1.3.Replacing all the spaces with  "%20" ' )

def replaced(s,m):
    
    count_sp = 0
    for i in range(m):
        if s[i] == ' ':
            count_sp += 1
    count_st = m + 2 * count_sp
    list1=[None] * count_st
    for i in range(m-1,-1,-1):
        if s[i] == ' ':
            list1[count_st - 1] = '0'
            list1[count_st - 2] = '2'
            list1[count_st - 3] = '%'
            count_st = count_st - 3
        else:
            list1[count_st - 1] = s[i]
            count_st  = count_st -  1
    return ''.join(list1)                   # convert list to str: seperator.join(list_name)

print replaced('ab d   ',4)


####################################################################################
print('####################################################################################')
# easy method: consider only the first m character and 
print 'ab d   '.replace(" ","%20")


# convert list and str as string is immutable

####################################################################################
print('####################################################################################')

print('# 1.4. Palindrome Permutation')
# method1
# put the string in a data dictionary with value showing the number of repeatition of each character (key) in the string


# to be a Palindrome permutation, all values should be even, at most one value could be odd

# method 2
# sort the string
# count each character
# count the number of characters with odd counts

def ispalpermut2(s):
    ss = sorted(s)
    odd_counts = 0
    count = 0
    prev_char = None
    for c in ss:
        if prev_char == c :
            count += 1
        else:
            if (count % 2!=0) :
                odd_counts += 1
            count = 1
            prev_char = c
    if odd_counts > 1:
        return False
    return True

print ispalpermut2('asdrdas')   # True
print ispalpermut2('asdrbdas')   # False

# assume only lowercase , space is a character as well

print('####################################################################################')

print('# 1.5. one edit away')

# first I write a program to check remove and insert: 

def one_edit(str1, str2):
	if len(str1) == len(str2):
		return check_replace(str1, str2)
	elif len(str1) + 1 == len(str2):
		return check_remove(str1, str2)
	elif len(str1) == len(str2) + 1 :
		return check_remove(str2, str1)
	else:
		return False
		
def check_remove(str1, str2): 
	idx1 = 0
	idx2 = 0
	one_change = False
	while idx1 < len(str1) :
		if str1[idx1] == str2[idx2]:
			idx1 += 1
			idx2 += 1
		elif str1[idx1] != str2[idx2] and not one_change :
			idx2 += 1
			one_change = True
		else:
			return False
	return True

def check_replace(str1, str2):
	one_change = False
	for i in range(len(str1)):
		if str1[i] != str2[i] and not one_change :
			one_change = True
		elif str1[i] != str2[i] and one_change :
			return False
	return True
	
print one_edit("cost","coaat")		
		
print('####################################################################################')

print('# 1.6. compressed string ')

		
		
		
		
		
		
		
		
		
		
		
		
		
