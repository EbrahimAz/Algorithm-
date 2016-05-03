
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
        d[c] = d.get(c, 0) + 1     # return value from a key  if no key then return the default: .get(key, default)
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

print('# 1.6. compressed string')

def compress(st):
	compressed = ""
	count = 1
	prev = st[0]
	for ind,c in enumerate(st[1:],1):
		if c != prev:
			compressed += prev + str(count)
			prev = c
			count = 1
		else:
			count += 1
	if st[-1] != compressed[-1]:
		compressed += prev + str(count)
	if len(compressed) < len(st):
		return compressed
	else:
		return st
		
print compress("aaadddrrgbbbbbhdhyfavcccccccccccccd")
		
print('####################################################################################')

print('# 1.7. Rotate a Matrix')
# require O(N2) memory
def rotate_matrix(mat):
	n = len(mat[0])
	rotated = [[None for x in range(n)] for x in range(n)]
	for i in range(n):
		for j in range(n):
			rotated[j][n-i-1] = mat[i][j]
	return rotated
			
print rotate_matrix([[12,7,3],[4 ,5,6],[7 ,8,9]])		
#  it can be done in place		
		
print('####################################################################################')

print('# 1.8. zero Matrix')		
def nullify(mat):
	null_row = []
	null_col = []
	for i in range(len(mat)):
		for j in range(len(mat[0])):
			if mat[i][j] == 0:
				null_row.append(i)
				null_col.append(j)
	for i in null_row:
		for j in range(len(mat[0])):
			mat[i][j] = 0
	for i in range(len(mat)):
		for j in null_col:
			mat[i][j] = 0
	return mat

print nullify([[12,7,3],[4 ,5,6],[7 ,8,0]])		
			
print('####################################################################################')

print('# 1.9. is substring')			
		
def isrotation(str1,str2):
	if str1=="" or str2=="":
		return False
	return IsSubstring(str2+str2, str1)
	
def IsSubstring(str1,str2):  # str2 is a substring of str1?
	len1 = len(str1)
	len2 = len(str2)
	for i in range(len1-len2+1):
		print str2,str1[i:i+len2]
		if str2 == str1[i:i+len2]:
			return True
	return False
	
print isrotation("cats","tsca")		
		
		
print('####################################################################################')

print('# career cup')
'''
Find if the characters of the sample string is in the same order in the text string.. Give a simple algo.. 
Eg.. TextString: abcNjhgAhGjhfhAljhRkhgRbhjbevfhO 
Sample string :NAGARRO

'''
#first method
def check(text, sample):
    pos = 0 
    for i in range(len(text)):
        if text[i] == sample[pos]: 
            pos += 1
        if pos == len(sample): 
            return True
    return False
	
#second	
def longers(P,S):
    maps = {}
    str1 = ''
    str2 =''
    for i in S:
        maps[str(i)] = str(ord(i))
    for ij in P:
        str1 = str1 + str(maps.get(ij))
    print str1
    for x in P:
        str2 = str2+str(str(ord(x)))
    print str2
    if str1 == str2:
        return True
    else:
        return False

print longers('NAGARRG', 'abcNjhgAhGjhfhAljhRkhgRbhjbevfhO')
print " ################# max difference ######################## "
"""
second mock : Pooya
You have an array for which the ith element is the price of a given stock on the day i.
 If you only permitted to buy one share if the stock and sell one share of the stock, 
 design an algorithm to find the  best times to buy and sell.
 5, 10, 8, 2, 6
 1, 2, 3, 4, 5
6.3 elements of programming
similarly this algorithm works for the min  battery that a robot requires to follow a path up and down 
up: uses battery
down: charges the battery
min battery required , therefore, is the max difference between alist[i], alist[j] where i<j
"""
def max_diff(alist):
	ind_min = ind_low = ind_high = 0
	min = alist[0]
	max_diff = 0
	for i in range(1,len(alist)-1):
		if alist[i] < min:
			min = alist[i]
			ind_min = i
		if (alist[i]- min) > max_diff:
			max_diff = alist[i]- min
			ind_low = ind_min
			ind_high = i
	return ind_low, ind_high, max_diff
		
print max_diff([5,10,2,7,0,8,4])
# time complexity O(N), space complexity O(1)

def unscramble(scramble):
    if len(scramble) <= 1:
        return scramble
    permuts = [scramble[i]+x for i in range(len(scramble)) for x in unscramble(scramble[:i]+scramble[i+1:])]
    return permuts
 
print unscramble("nowk")

print " ################# uneaten leaves ######################## "
"""
K caterpillars are eating their way through N leaves. Each caterpillar falls from leaf to leaf in a unique sequence.
All caterpillars start at a twig in position 0 and fall onto the leaves at positions between 1 and N. Each caterpillar
i has an associated jump-number A. A caterpillar with jump number j eats leaves at positions that are multiples of j. 
It will proceed in the order 1j, 2j, 3j,   till it reaches the end of the leaves, then it stops and builds its cocoon.
N = number of leaves
K = number of caterpillars
A = Array of integer jump numbers (one per line).
Output Format:
An integer denoting the number of uneaten leaves.
N,K,A = 10,3,[2,4,5]
output = 4  
3,4,7,9 are uneaten
"""
def uneaten(n,k,A):
	count = 0
	for i in range(1,n+1):
		eaten = False
		for j in A:
			if i % j == 0:
				eaten = True
				break
		if not eaten:
			count += 1
	return count
print uneaten(10,3,[2,4,5])

# this is O(NK)
print " ################# maximum length palindrome ######################## "
# maximum length palindrome

def ml_helper(st, istart, iend):
	maxl = len(st[istart:iend])+1
	while istart>0 and iend<len(st)-1:
		if st[istart-1] == st[iend+1]:
			maxl += 2
			istart -= 1
			iend += 1
		else:
			break
	return maxl
			

def longest_palindrome(st):
	if len(st)<2:
		return len(st)
	mlp = 0
	for i in range(len(st)-1):
		curr = ml_helper(st,i,i)   # for the case that palindrome length is odd
		mlp = max(curr, mlp)
		if st[i] == st[i+1]:    # for the case where palindrome lenght is even
			curr = ml_helper(st,i,i+1)
			mlp = max(curr, mlp)
	return mlp

print longest_palindrome("aisnfgycbdkbasdfggfdsacushbsjbb jsdlkdj")
print longest_palindrome("a")
print longest_palindrome(" ")
print longest_palindrome("aa")

print " ################## is palindrome ############################ "
def is_palind(str):
	return str == str[::-1]
print is_palind("asdsa")