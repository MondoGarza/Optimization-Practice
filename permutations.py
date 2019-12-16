#Function to check if string a is a permutation
#of string b
#Runtime = O(a + b + 256) => O(a + b)
#space = O(hash1 + hash2) => O(1)
def is_perm(a, b):
	hash1 = [0] * 256
	hash2 = [0] * 256

	for char1 in a:
		hash1[ord(char1)] += 1
		
	for char2 in b:
		hash2[ord(char2)] += 1

	if hash1 == hash2:
		return ("yes")
	else:
		return ("No")

perm1 = 'abcabcabcabcabcabc'
perm2 = 'aaaaaabbbbbbcccccc'
is_perm(perm1,perm2)