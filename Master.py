from random import randint

def partition (A, a, b):
    p = randint(a,b)
    # or mid point
    # p = (a + b) / 2

    piv = A[p]

    # swap the pivot with the end of the array
    A[p] = A[b]
    A[b] = piv

    i = a     # left index (right movement ->)
    j = b - 1 # right index (left movement <-)

    while i <= j:
        # move right if smaller/eq than/to piv
        while A[i] <= piv and i <= j:
            i += 1
        # move left if greater/eq than/to piv
        while A[j] >= piv and j >= i:
            j -= 1

        # indices stopped moving:
        if i < j:
            # swap
            t = A[i]
            A[i] = A[j]
            A[j] = t
    # place pivot back in the right place
    # all values < pivot are to its left and 
    # all values > pivot are to its right
    A[b] = A[i]
    A[i] = piv

    return i

def IpQuickSort (A, a, b):

    while a < b:
        p = partition(A, a, b) # p is pivot's location

        #sort the smaller partition
        if p - a < b - p:
            IpQuickSort(A,a,p-1)
            a = p + 1 # partition less than p is sorted
        else:
            IpQuickSort(A,p+1,b)
            b = p - 1 # partition greater than p is sorted


def main():
    #teste com o vetor preenchido
    A =  [12,3,5,4,7,3,1,3]
    print A
    IpQuickSort(A,0,len(A)-1)
    print A

if __name__ == "__main__": main()
