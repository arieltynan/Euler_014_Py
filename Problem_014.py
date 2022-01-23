#Longest Collatz sequence
seqlen = [] #list of lengths of sequences
for n in range(1,1000000):
    seq = [] #sequence of numbers
    seq.append(n)
    while n > 1:
        if n % 2 == 0:
            n = n/2
            seq.append(n)
        elif n % 2 != 0:
            n = 3*n + 1
            seq.append(n)
    seqlen.append(len(seq))
   
print(max(seqlen))
print(seqlen.index(max(seqlen)))