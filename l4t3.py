import string
def frequent():
        reserve = []
        f = open('wordss.txt','r')

        for line in f:
             res = line.lower().strip(string.punctuation + string.whitespace) 
             reserve += res
       # return reserve

        max = 10
        for i in reserve:
          if reserve.count(i) > max:
             max = reserve.count(i)
             print (i)
        print(max)

print(frequent())
