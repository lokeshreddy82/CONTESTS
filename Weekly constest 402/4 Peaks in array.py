class Node:
    def __init__(self,l,r):
        self.l=l
        self.r=r
        self.left=None
        self.right=None
        self.total=0
class segment:
    def __init__(self,n,nums):
        self.n=n-1
        self.arr=nums
    def change_index(self,index,val):
        self.arr[index]=val
    def build(self,low,high):
        if low==high:
            n=Node(low,high)
            if low>0 and high<self.n:
                if self.arr[low-1]<self.arr[low] and self.arr[low]>self.arr[low+1]:
                    n.total=1
            return n
        mid=(low+high)>>1
        n=Node(low,high)
        n.left=self.build(low,mid)
        n.right=self.build(mid+1,high)
        n.total=n.left.total+n.right.total
        return n
    def update(self,root,left,right):
        if root.l>right or root.r<left:
            return
        if root.l==root.r:
            if root.l>0 and root.r<self.n and self.arr[root.l-1]<self.arr[root.r] and self.arr[root.l]>self.arr[root.l+1]:
                root.total=1
            else:
                root.total=0
            return
        mid=(root.l+root.r)>>1
        if left <= mid:
            self.update(root.left, left, right)
        if right > mid:
            self.update(root.right, left, right)

        root.total = 0
        if root.left:
            root.total += root.left.total
        if root.right:
            root.total += root.right.total
    def peaks(self,root,left,right):
        if root.l==root.r:
            return root.total
        if root.l>=left and right>=root.r:
            return root.total
        mid=(root.l+root.r)>>1
        if right<=mid:
            return self.peaks(root.left,left,right)
        elif left>=mid+1:
            return self.peaks(root.right,left,right)
        else:
            return self.peaks(root.left,left,right)+self.peaks(
                root.right,left,right)
class Solution:
    def countOfPeaks(self, nums: list[int], queries: list[list[int]]) -> list[int]:
        n=len(nums)
        s=segment(n,nums)
        self.root=s.build(0,len(nums)-1)
        res=[]
        for query in queries:
            if query[0]==1:
                if query[2]-query[1]<2:
                    res.append(0)
                else:
                    res.append(s.peaks(self.root,query[1]+1,query[2]-1))
            else:
                ind,val=query[1],query[2]
                s.change_index(ind,val)
                l,r=ind,ind
                if l!=0:
                    l -=1
                if r!=n-2:
                    r +=1
                s.update(self.root,l,r)
        return res
