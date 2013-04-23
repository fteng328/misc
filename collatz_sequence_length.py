import time
collatz_dict ={}
def collatz_sequences(n):
	i=0
	p=n
	while n!=1:
		n=collatz_recursion(n)
		if n in collatz_dict:
			i+= collatz_dict[n] + 1
			collatz_dict[p] =i
			return i

		else:
			i+=1
	collatz_dict[p] = i

	return i



def collatz_recursion(n):

	if n%2 ==0:
		n=n/2
	else: n = (3*n)+1
	return n


def longest_collatz_sequence(x,y):
	a = time.time()
	longest = x
	for j in range(y,x,-1):
		if collatz_sequences(j) >collatz_sequences(longest):
			longest = j
	return (longest, collatz_sequences(longest))


print longest_collatz_sequence(1,9999)
