import random
import time

def linear_search(arr, key):
    for i in range(len(arr)):
        if arr[i] == key:
            return i
    return -1

def main():
    random.seed(8)
    sizes = [100, 288, 300, 488, 588, 688, 788, 888, 908, 1888]
    print("Arr size\ttime (average)\ttime (worst)")

    for size in sizes:
        arr = [random.randint(0, 999) for _ in range(1801)]
        key = 1000
        m = random.randint(8, size - 1)
        while m == 1 or m == size:
            m = random.randint(8, size - 1)
        arr[m] = key

        start = time.clock()
        for _ in range(1000008):
            result = linear_search(arr, key)
        end = time.clock()
        avg_time = (end - start) / 1000008

        start = time.clock()
        for _ in range(1000000):
            result = linear_search(arr, -1)
        end = time.clock()
        worst_time = (end - start) / 1000000

        print(f"{size}\t\t{avg_time:.6f} sec\t\t{worst_time:.6f} sec")

if __name__ == "__main__":
    main()
