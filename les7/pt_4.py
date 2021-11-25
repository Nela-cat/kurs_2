numbers = [6,8,9,7,43,455,67,7,4,5,8 ,1,2,3,4,5]
new = [ 'true_2' if items%2==0 else   'true_3' if  items%3==0 else 'false' for items in numbers]
#for i in numbers:
    #if i%2==0:
        #new.append('true_2')
   # elif i%3==0:
       # new.append('true_3')
        
   # else :
     #   new.append('folse')
print(new)
