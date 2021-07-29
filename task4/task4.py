import sys
arr = open(sys.argv[1], 'r').read()
arr = [int(i) for i in arr.rsplit('\n') if i != '']
mean = round(sum(arr)/len(arr))
print(sum([abs(mean-i) for i in arr]))


