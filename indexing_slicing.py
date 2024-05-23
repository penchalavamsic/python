import numpy as indsli
arr1=indsli.array([1,23,4])
print(arr1[1]) #one dimensional indexing
arr2=indsli.array([[1,2,5],[4,5,8]])
print(arr2[0,2])#two dimensional indexing
print(arr1[:1]) #slicing
print(arr1[::1])
print(arr2[:1, :1])
print(arr2[arr2>1])#boolean indexing
