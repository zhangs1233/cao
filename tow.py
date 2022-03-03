import torch
#t1=torch.ones(3,4)
#print(t1,t1.size())
# print(t1.shape[0],t1.size()[1])
#print(t1.dtype)
#print(t1.long().dtype)    #数据类型的转换
#t2=torch.tensor([[[[[100]]]]])
#print(t2,t2.size(),t2.item(),t2[0][0][0][0][0].numpy())  #item只能是一个值
#t3=torch.rand(3,4,2)
#print(t3,t3.view(-1,2))#一维数组
#print(t3.dim())  #获取阶数
#print(t3,t3.max(dim=-1))  #dim=-1 求这一行的最大值
#value,index=t3.max(dim=-1)
#print(value,index)
#t1=torch.tensor([1,2,3,4,5,6,7,8,9])
#print(t1.float().mean())
#print(t1.float().std())
#t1=t1.float()
#print(torch.sqrt((t1-5).pow(2).sum() / (t1.size(0)-1)))
#t1.sub_(5)    #就地修改原来的值
#print(t1)
t3=torch.rand(3,4,2)  #索引[0,1,2]
print(t3.shape)
#[2,3,4]   下标索引来
t3=t3.permute(2,0,1)
print(t3.shape)