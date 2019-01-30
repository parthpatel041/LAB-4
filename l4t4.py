import string

def wordlist():
	reserve = []
	word = open('wordss.txt', 'r')
	for l in word:
		w = l.strip()
		reserve += [w]
	return reserve

list = wordlist()


def counter(list):
	reserve = []
	f = open('wordss.txt', 'r')
	w = f.readlines()
	
	for line in w:
		res = line.lower().strip(string.punctuation + string.whitespace).split()
		reserve += res

	count = {}
	for word in reserve:
		count[word] = count.get(word, 0) + 1

	no_list = list(set(count.keys()) - set(list))

	return no_list
	
print(counter(list))


