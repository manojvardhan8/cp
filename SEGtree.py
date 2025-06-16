class SEGtree:
    def __init__(self,l):
        self.l=l 
        self.n=len(l)
        self.seg=[0 for i in range(4*self.n)]
        self.build(0,self.n-1,0)
    def build(self,left,right,index):
        if left==right:
            self.seg[index]=self.l[left]
            return 
        m=(left+right)>>1 
        self.build(left,m,2*index+1)
        self.build(m+1,right,2*index+2)
        self.seg[index]=self.seg[2*index+1]+self.seg[2*index+2]
    def query(self,left,right,i,j,index):
        if i>=left and j<=right:
            return seg[index]
        if j<left or i>right:
            return 0 
        m=(i+j)>>1 
        return self.query(left,right,i,m,2*index+1)+self.query(left,right,m+1,j,2*index+2)
    def point_update(self,ind,val,i,j,index):
        if i==j:
            self.seg[index]=val 
            self.l[ind]=val 
            return 
        m=(i+j)>>1 
        if ind<=m:
            self.point_update(ind,val,i,m,2*index+1)
        else:
            self.point_update(ind,val,m+1,j,2*index+2)
        self.seg[index]=self.seg[2*index+1]+self.seg[2*index+2]
