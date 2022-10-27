class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        i = 0; j = 0; val = list();
        while(i < m and j < n):
            if (nums1[i] < nums2[j]):
                val.append(nums1[i]); i += 1;
            else:
                val.append(nums2[j]); j += 1;
        while (i < m):
            val.append(nums1[i]); i+=1;
        while(j < n): 
            val.append(nums2[j]); j+=1;
        for i in range(m+n):
            nums1[i] = val[i]
            