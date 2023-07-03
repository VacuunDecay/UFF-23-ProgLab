# Python code file

N, D = list(map(int, input().split()))
P = list(map(int, input().split()))



resp = "N"
for i in range(N-1):
    d = P[i+1] - P[i]
    if d > D:
        resp = "N"
        break
    resp = "S"
if(resp == "S" and P[N-1] - 42195 > D):
    resp = "N"

print(resp)