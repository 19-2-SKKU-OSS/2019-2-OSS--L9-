M = 20
N = 40
result = []
for i in range(1,20001):
    if M <= i**2 <= N:
        result.append(i**2)
    elif i**2 > N:
        break
if result == []:
    print(-1)
else:
    print(result)
