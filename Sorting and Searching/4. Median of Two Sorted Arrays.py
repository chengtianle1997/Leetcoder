
# O(logn) solution
class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        k = (len(nums1) + len(nums2)) // 2 
        if (len(nums1) + len(nums2)) % 2 == 1:
            return self.kth(nums1, nums2, k)
        else:
            return (self.kth(nums1, nums2, k - 1) + self.kth(nums1, nums2, k)) / 2
        
    def kth(self, a, b, k):
        if not a:
            return b[k]
        if not b:
            return a[k]
        
        ia, ib = len(a) // 2, len(b) // 2
        ma, mb = a[ia], b[ib]
        
        if ia + ib < k:
            # less than k elements, search right
            if ma > mb:
                # drop the left part of b
                return self.kth(a, b[ib + 1:], k - ib - 1)
            else:
                # drop the left part of a
                return self.kth(a[ia + 1:], b, k - ia - 1)
        else:
            # more than k elements selected, search left
            if ma > mb:
                # drop the right part of a, 
                # k is not changed because we only cares about the index from the left
                return self.kth(a[:ia], b, k)
            else:
                # drop the right part of b
                return self.kth(a, b[:ib], k)
            
        
            