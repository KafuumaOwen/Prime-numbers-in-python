#Code the takes a list of numbers and outputs only prime numbers from the original list

#Original list with allkinds of numbers
numbers =[7,9,11,1,43,82,7,1,62]

flag = False

for i in numbers:
  if i ==1:
    numbers.remove(i)
  elif i>1:
    #look for factors
    for x in range(2,i):
      if(i%x)==0:
        flag = True
#Remove non-prime numbers greater than 1
  if flag==True:
    numbers.remove(i)
  
          
print(list(numbers))

