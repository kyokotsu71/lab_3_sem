sps = [1, 2, -10, 7, 1000, 823, -111]
max_index = sps.index(max(sps))
min_index = sps.index(min(sps))
sps[max_index], sps[min_index] = sps[min_index], sps[max_index]
# sps[sps.index(max(sps))], sps[sps.index(min(sps))] = sps[sps.index(min(sps))], sps[sps.index(max(sps))]
print(sps)
