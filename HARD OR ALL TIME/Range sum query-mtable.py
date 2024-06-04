class node:
     def __init__(self,l,r):
          self.start=l
          self.end=r
          self.total=0
          self.left=None
          self.right=None
class NumArray(object):
     def __init__(self, nums):
          
          def dfs(l,r):
               if l==r:
                    n=node(l,r)
                    n.total=nums[l]
                    return n
               mid=(l+r)//2
               n=node(l,r)
               n.left=dfs(l,mid)
               n.right=dfs(mid+1,r)
               n.total=n.left.total+n.right.total
               return n  
          self.root=dfs(0,len(nums)-1)
     def update(self, index, val):
          """
          :type index: int
          :type val: int
          :rtype: None
          """
          def updateval(root):
               ...
               if root.start==root.end:
                    root.total=val
                    return
               mid=(root.start+root.end)//2
               if index<=mid:
                    updateval(root.left)
               else:
                    updateval(root.right)
               root.total=root.left.total+root.right.total
               return
          updateval(self.root)
     def sumRange(self, left, right):
          """
          :type left: int
          :type right: int
          :rtype: int
          """
          def rangeSum(root, i, j):
            if root.start == i and root.end == j:
                return root.total

            mid = (root.start + root.end) // 2
            if j <= mid:
                return rangeSum(root.left, i, j)
            elif i >= mid + 1:
                return rangeSum(root.right, i, j)
            else:
                return rangeSum(root.left, i, mid) + rangeSum(
                    root.right, mid + 1, j
                )

          return rangeSum(self.root, left, right)






n=NumArray([1, 3, 5])
n.update(2, 2)
