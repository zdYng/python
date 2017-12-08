import numpy as np
from numpy.linalg import *
def main():
    list=[[1,3,5],[2,4,6]]
    print(type(list))
    np_list=np.array(list)  #only one
    print(type(np_list))
    np_list=np.array(list,dtype=np.float)
    # print("shape"+np_list.shape)
    # print("ndim"+np_list.ndim)
    # print("dtype"+np_list.dtype)
    # print("itemsize"+np_list.itemsize)
    print(np.random.rand(2,4))
    print(np.ones([3,5]))
    print("Rand:")
    print(np.random.rand(2,4))
    print(np.random.rand())
    print("RandInt:")
    print(np.random.randint(1,10,3))
    print(np.random.randn(2,4))
    print("Choice:")
    print(np.random.choice([10,20,30]))
    print("Distribute:")
    print(np.random.beta(1,10,100))


    #3 Array.Opes
    # print(np.arange(1,11).reshape([2,-1]))
    # list=np.arange((1,11).reshape([2,-1]))
    # print(np.exp(list))
    # print(np.exp2(list))
    # print(np.sqrt(list))
    list2 = np.array([[[1,2,3,4],
                       [4,5,6,7]],
                      [[7,8,9,10],
                       [10,11,12,13]],
                      [[14,15,16,17],
                       [18,19,20,21]]
                      ])
    print(list2.sum(axis=2))
    print(list2.max(axis=1))
    print(list2.min(axis=0))

    lst1 =np.array([1,2,3,4])
    lst2=np.array([2,3,4,5])
    print(lst1+lst2)
    print(lst1-lst2)
    print(lst1*lst2)
    print(np.concatenate((lst1,lst2),axis=0))  # pai
    print(np.vstack((lst1,lst2)))  #lie
    print(np.hstack((lst1,lst2)))
    print(np.split(lst1,4))
    print(np.copy(lst1))

    #4 liner

    print(np.eye(3))
    lst=np.array([[1.,2,],
    [3.,4.]])
    print(inv(lst))
    print(lst.transpose())
    print(det(lst))
    print(eig(lst))
    y=np.array([[5.],[7.]])
    print(solve(lst,y))
    #5 Others
    print("FFT:")
    print(np.fft.fft(np.array([1,1,1,1,1,1,1,1])))





if __name__ =="__main__":
    main()