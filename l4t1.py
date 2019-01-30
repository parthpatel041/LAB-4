import string
def strip():
        reserve = []
        f = open('wordss.txt','r')

        for line in f:
             res = line.lower().strip(string.punctuation + string.whitespace) 
             reserve += res
        return reserve

print(strip())

