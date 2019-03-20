class sort:
    def __init__(self,arr):
        self.arr=arr

    def mergeSort(self,arr):
        if arr is None:
            arr=self.arr
        if len(arr)>1:
            
            mid = len(arr)//2
            L=arr[:mid]
            R=arr[mid:]

            self.mergeSort(L)
            self.mergeSort(R)
            i=j=k=0
            while i<len(L) and j<len(R):
                if L[i]<R[j]:
                    arr[k]=L[i]
                    i=i+1
                else:
                    arr[k]=R[j]
                    j=j+1
                k=k+1

            while i<len(L):
                arr[k]=L[i]
                k=k+1
                i=i+1
            while j<len(R):
                arr[k]=R[j]
                k=k+1
                j=j+1


    def printArr(self,arr):
        if arr is None:
            arr=self.arr
        for i in arr:
            print(i)

class main:
    arr= list(map(int,input("Enter numbers seperated by space to sort: ").split()))
    m = sort(arr)
    m.mergeSort(arr)
    m.printArr(arr)