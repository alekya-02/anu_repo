n=int(input())
d=list(map(int,input().split()))
se=int(input())
for i in range(n):
    if d[i]==se:
        print("Found")
        break
else:
    print("Not Found")
