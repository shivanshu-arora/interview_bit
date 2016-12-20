class Solution:
    # @param A : list of integers
    # @return an integer
    def firstMissingPositive(self, A):
        n = len(A)
        i = 0
        j = n-1
        
        while i <= j:
            while i <= j and A[i] <= 0:
                i = i + 1
            while j >= i and A[j] > 0:
                j = j - 1
    
            if i < n and j >= 0 and i<=j and A[i] > 0 and A[j] <= 0:
                A[i], A[j] = A[j], A[i]
                
        i = 0
        while i<n:
            if A[i] >0:
                break
            i = i+1

        for k in range(i,n):
            if abs(A[k])+i-1 <n:
                if A[abs(A[k])+i-1] >=0:
                    A[abs(A[k])+i-1] = -A[abs(A[k])+i-1]
        
        
        count = 1
        for k in range(i,n):
            if A[k] >0:
                break
            else:
                count +=1
        return count
            
