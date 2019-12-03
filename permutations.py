#Find all permutations of s within b
  
# Function returns true 
# if contents of arr1[] and arr2[] 
# are same, otherwise false. 
def compare(arr1, arr2, MAX): 
    for i in range(MAX): 
        if arr1[i] != arr2[i]: 
            return False
    return True
       
def searchWithin(s, b):
	MAX=256

	M = len(s)
	N = len(b) 
  
    # countP[]:  Store count of 
    # all characters of stern 
    # countTW[]: Store count of 
    # current window of text
    countP = [0]*MAX
    countTW = [0]*MAX
  
    for i in range(M): 
        (countP[ord(s[i])]) += 1
        (countTW[ord(b[i])]) += 1

    # Traverse through remaining 
    # characters of stern 
    for i in range(M,N): 
        # Compare counts of current 
        # window of text with 
        # counts of stern[] 
        if compare(countP, countTW, MAX): 
            print("Found at Index", (i-M)) 
  
        # Add current character to current window 
        (countTW[ord(b[i])]) += 1
  
        # Remove the first character of previous window 
        (countTW[ord(b[i-M])]) -= 1
      
    # Check for the last window in text     
    if compare(countP, countTW, MAX): 
        print("Found at Index", N-M)
        
def subPerm(s):
    sLeft = [s[0]+s[1],s[1]+s[0]]
    return sLeft

def placein(letter, string):
    newS = [0,string for string in string]

def perm(s):
    sList = list(s)
    newPerm = 
    for i in range(s-1):
        perm


small = 'abbc'
big = 'cbabadcbbabbcbabaabccbabc'
print([0,string])
searchWithin(small,big)