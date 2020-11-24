import numpy as np

def thereExists( A ) :
  v = 0 
  for a in A : 
    if a > 4 : v = 1
  return v
  
def negationThereExists( A ) :
  # Your code goes here 
  
# This code allows you to test the functions you have written
print(thereExists([3,4,5,6,7,8,9]), "the proposition is true for this set")
print(negationThereExists([0,1,2,3]), "the negation is true for this set")
print(thereExists([0,1,2,3]), "the proposition is false for this set")
print(negationThereExists([5,6,7,8,9,10]), "the negation is false for this set")
