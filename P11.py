def search(list,n):
    for i in range(len(list)):
         if list[i] == n:
              return True
              return False
        
list=[1,2,'sachin',4,'python',6]
n='python'
if search(list,n):
            print("found")
else:
            print("false")