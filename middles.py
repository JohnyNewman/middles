def get_middle(s):
	s = str(s)
	a = len(s)
	p = int(((a - 1) / 2))
	char1 = int((p + 0.5))
	char2 = int((p + 1.5))
	char3 = int((p))
	result1 = s[char1]
	result2 = s[char2]
	result3 = s[char3]
	for i in range(0, len(s)):
		if a % 2 == 0:
			return (result1 + result2)
		else:
			return (result3)
s = input("WRITE SOMETHING: ")
print(get_middle(s))