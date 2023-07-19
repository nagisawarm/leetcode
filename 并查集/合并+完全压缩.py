nums = [1, 2, 3, 4]

def union(x, y):
    xx = find(x)
    yy = find(y)
    if xx == yy:
        return
    # if size[xx] > size[yy]:     #按大小合并
    if rank[xx] > rank[yy]:     #按秩合并
        xx, yy = yy, xx
    parent[xx] = yy
    if rank[xx] == rank[yy]:
        rank[yy] += 1
    size[yy] += size[xx]

def find(x):
    if x != parent[x]:
        parent[x] = find(parent[x])
    return parent[x]

m = len(nums)
parent = {i: i for i in range(m)}
rank = {i : 1 for i in range(m)}
size = {i : 1 for i in range(m)}
