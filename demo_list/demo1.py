# list =[1,2,3,4,5,6,7,8,9,10,11]

# def sum_value(value):
#  result =0
#  for item in value:
#     result += item
#  return result
    
# print (sum_value(list))
import time
for i in range(101):
 print('%3d\r'%i,end='',flush=True)
 
 time.sleep(0.05)
print('\ndone')