import sys
def calc(n,m):
    ms = [i for i in range(1,n+1)]
    a = 0
    b = m
    path=[]
    while True:
        if n%m==0: break
        l = ms[a:b]
        if l[-1] == ms[0]:
            path.append(l[0])
            break        
        else:
            path.append(l[0])
            ms += ms[0:n]
            a = b - 1
            b = a + m
    answer = ''
    for i in path:
        answer+=str(i)
    return answer


if __name__ == "__main__":
    n = sys.argv[1]
    m = sys.argv[2]
print(calc(int(n),int(m)))
