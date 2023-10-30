m, n = map(int, input().split())
dim_list = []
for _ in range(m):
    dim_list.append(list(map(int, input().split())))
dim_list = dim_list[::-1]
for j in range(1, m):
    dim_list[j][0] = dim_list[j][0] + dim_list[j-1][0]
for k in range(1, n):
    dim_list[0][k] = dim_list[0][k] + dim_list[0][k-1]
for g in range(1, m):
    for l in range(1, n):
        dim_list[g][l] = dim_list[g][l] + max(dim_list[g-1][l], dim_list[g][l-1])
i = m - 1
j = n - 1
path = ""
while i or j:
    if not i:
        path += "R"
        j -= 1
    elif not j:
        path += "F"
        i -= 1
    elif dim_list[i-1][j] < dim_list[i][j-1]:
        path += "R"
        j -= 1
    else:
        path += "F"
        i -= 1
print(path[::-1])
