"""
pseudo code
collect a name as parameter
save it as name and reverse it
"""
"""
def reversestring(name):
	if reversestring(name)== reversestring(name)[::-1]:

		return reversestring

print (reversestring(namen))
"""

def reverse_string(word):
	reverse_word = ''
	for number in range(len(word)-1, -1 -1):
		reverse_word += word[number]
	return reverse_word

print(reverse_string("mummy wa"))



def pallindrome(number):
	return str(number) == reverse_string(str(number))
print(pallindrome("dad"))