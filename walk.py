import time, sys
import tracemalloc
lst=list(range(10000000))

def sum1(lst):
    print(sum(lst))

def sum2(lst):
    total=0
    for i in lst:
        total+=i
    print(total)

def sum3(lst):
    total=0
    i=0
    while i< len(lst):
        total+=lst[i]
        i+=1
    print(total)


def sum4(lst, begin, end):
     if (begin < end):
         return 0
     if (begin == end):
       return a[end]
     q = begin + (end - begin) // 2
     print( sum4(lst, begin, q) + sum4(lst, q + 1, end))

def sum5(lst):
    if len(lst)== 0:
        return 0
    elif len(lst)==1:
        return lst[0]
    else:
        return lst[0]+sum5(lst[1:])

def sum6(a, begin, end):
     if (begin < end):
         return 0
     if (begin == end):
         return a[end]
     q = (end - begin) // 4
     print(sum6(a, begin, begin + q) + sum6(a, begin + q + 1, begin + 2 * q) +sum6(a, begin + 2 * q + 1, begin + 3 * q) + sum6(a, begin + 3 * q + 1, end))

#đo thời gian
start_time = time.perf_counter()

# Đo bộ nhớ
tracemalloc.start()

#sum1(lst)
#sum2(lst)
sum3(lst)
#sum4(lst,1,10000000)
#sum5(lst)
#sum6(lst,1,10000000)
current, peak = tracemalloc.get_traced_memory()
tracemalloc.stop()

end_time = time.perf_counter()

print(f"Thời gian chạy: {end_time - start_time} giây")
print(f"Bộ nhớ hiện tại đang sử dụng: {current / 10**6} MB; Đỉnh điểm bộ nhớ sử dụng: {peak / 10**6} MB")
print(f"Bộ nhớ tiêu tốn {sys.getsizeof(lst)} bytes")
