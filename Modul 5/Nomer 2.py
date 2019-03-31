def insertionSort(A):
    n = len(A)
    for i in range(1, n):
        nilai = A[i]
        pos = i
        while pos > 0 and nilai < A[pos - 1]:
            A[pos] = A[pos - 1]
            pos = pos - 1
        A[pos] = nilai

A = [1,2,3,4,5]
B = [6,7,8,9,10]
C = []
C.extend(A)
C.extend(B)

insertionSort(C)
print(C)
