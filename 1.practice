

print "#################################################"
print "############## practice chapter1 ################"

def isuniq(astr):
	return len(set(astr))== len(astr)
	
print isuniq("abcdefg")
print isuniq("aabcdef")

print "#################################################"

def isuniq1(astr):
	sstr = sorted(astr)
	checker = True
	prev = None
	for char in sstr:
		if char == prev:
			checker = False
		prev = char
	return checker

print isuniq1("abcdefg")
print isuniq1("aabcdef")

####################################################################################
print('#2 for loop has O(len(s))')
def isuniq2(s):
    sets=set()
    for c in s:
        if c in sets:
            return False
        sets.add(c)
    return True

print isuniq2('hello') 
print isuniq2('bus') 


####################################################################################
print('#3 for loop has O(len(s))')
def isuniq3(s):
	uniq = set()
	checker = True
	for char in s:
		if char in uniq:
			checker = False
		else:
			uniq.add(char)
	return checker


print isuniq3('hello') 
print isuniq3('bus') 

####################################################################################

print "###################################################"
print "############## practice chapter1.2 ################"

def ispermut(str1, str2):
	if len(str1) != len(str2):
		return False
	sstr1 = sorted(str1)
	sstr2 = sorted(str2)
	for i in range(len(sstr1)):
		if sstr1[i] != sstr2[i]:
			return False
	return True
print ispermut("hel","leh")
print ispermut("hello1","lehho1")	

print "###################################################"
print "############## practice chapter1.3 ################"

def ispermut(str1, str2):
	if len(str1) != len(str2):
		return False
	sstr1 = sorted(str1)
	sstr2 = sorted(str2)
	for i in range(len(sstr1)):
		if sstr1[i] != sstr2[i]:
			return False
	return True
print ispermut("hel","leh")
print ispermut("hello1","lehho1")	



