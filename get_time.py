# 在一个列表中存储100万整数,在第二个位置
# 插入一个数,计算插入所用时间,1000万个呢?
# 100  time: 0.0008537769317626953
# 1000 time: 0.008672714233398438

import time

l = [x for x in range(1000000)]

st = time.time()
l.insert(0,'007')
print("time:",time.time() - st)
