import string

def counter():
	reserve = []
	f = open('wordss.txt', 'r')
	w = f.readlines()

	for line in w:
		res = line.lower().strip(string.punctuation + string.whitespace).split()
		reserve = reserve + res

	count = {}
	for word in reserve:
		count[word] = count.get(word, 0) + 1

	total = len(reserve)
	diff_word = len(count.keys())
	vocab = float(diff_word) / total
	concat = sorted([(v, k) for k, v in count.items()], reverse=True)
	
	for count, word in concat:
		print(word + " : " + str(concat))

	print("Words " + str(total) + "\n" + "Different words: " + str(diff_word) + "\n" + "Vocab ratio: " + str(vocab))

counter()

