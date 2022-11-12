class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
#         new_array = []
#         while len(arr) > 1:
       
#             new_array.append(max(arr[1:]))
#             arr = arr[1:]
#         new_array.append(-1)
#         return new_array
            
#         set the max to -1
#         compare current to max
        currentMax = -1
        for i in range(len(arr)-1, -1 , -1):
            newMax = max(currentMax,arr[i])
            arr[i] = currentMax
            currentMax =newMax
        
        return arr
