#row
A = input("A: ")
list_A = []
for i in A:
    list_A.append(i)
#col
B = input("B: ")
list_B = []
for i in B:
    list_B.append(i)
print("   ",end="")
for i in list_B:
    print(i,end = "  ")
print()
matrix = [[0]*len(B)]* len(A) 


dictionary = dict(zip(A, matrix))
for col,row in dictionary.items():
    print(col,row)
      
        

            
            
            
            
            
