import fileinput

lst = None

# parse input
i = 0
for line in fileinput.input():
    if lst == None:
        lst = []
        i = i + 1
    else:
        numstrs = line.rstrip().split(' ')
        ts = map(int, numstrs)
        tsi = ts + [i]
        lst.append(tsi)
        i = i + 1
        
def join(a,b):
    c = []
    while len(a) != 0 and len(b) != 0:
        x = a[0]
        y = b[0]
        if x[0] * y[1] <= y[0] * x[1]:
            c.append(x)
            a.remove(x)
        else:
            c.append(y)
            b.remove(y)
    if len(a) == 0:
        c += b
    else:
        c += a
    return c
        

def mergesort(x):
    if len(x) == 0 or len(x) == 1:
        return x
    else:
        mid = len(x)/2
        a = mergesort(x[:mid])
        b = mergesort(x[mid:])
        return join(a,b)    

for res in mergesort(lst):
    print res[2]


# A shoemaker has N orders from customers that he must execute. The shoemaker can work on only one job each day. For each job i, it takes Ti days for the shoemaker to finish the job, where Ti is an integer and (1 ≤ Ti ≤ 1000). For each day of delay before starting to work for the job i, shoemaker must pay a fine of Si (1 ≤ Si ≤ 10000) rupees. Your task is to help the shoemaker find the sequence in which to complete the jobs so that his total fine is minimized. If multiple solutions are possible, print the one that is lexicographically least (i.e., earliest in dictionary order).

# Solution hint

# Sort the jobs in terms of the ratios Si / Ti. To compare a/b and c/d, cross-multiply to avoid floating point comparisons. Use a stable sort to get the lexicographically smallest value.

# Input format

# The first line of input contains an integer N (1 ≤ N ≤ 100000). Each of the next N lines contains two space separated integers: the time Ti and fine Si for job i, 1 ≤ i ≤ N.

# Output format

# You program should print the sequence of jobs with minimal fine. Each job should be represented by its position in the input and each job should appear on a new line, by itself. If multiple solutions are possible, print the one that is lexicographically least (i.e., earliest in dictionary order).