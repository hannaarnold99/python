# - - - - - - Merge Sort Algorithm Using Python- - - - - - #
class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """

        helper = nums1[:m]

        i = j = k = 0
        while ( i < m and j < n):
            if (helper[i] <= nums2[j]):
                nums1[k] = helper[i]
                i += 1
            else:
                nums1[k] = nums2[j]
                j += 1
            k += 1
        while ( i < m):
            nums1[k] = helper[i]
            i+=1
            k+=1
        while (j < n):
            nums1[k] = nums2[j]
            j += 1
            k += 1
