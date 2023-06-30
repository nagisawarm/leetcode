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
    