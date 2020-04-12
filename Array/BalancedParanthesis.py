def checkBalanced(str):
    s=[]
    res= True
    top=-1
    for e in str:
        if top==-1:
            s.append(e)
            top+=1
            
        else:
            if e == "{" or e=="[" or e=="(":
                s.append(e)
                top+=1
               
            else:
                if (e==")" and s[top]=="("):
                    
                    s.remove(s[top])
                    top-=1      
                elif (e=="]" and s[top]=="["):
                   
                    s.remove(s[top])
                    top-=1   
                elif (e=="}" and s[top]=="{"):
                  
                    s.remove(s[top])
                    top-=1  
                else:
                    res= False
    if top>=0:
        return False
    elif res is True or top==-1:
        return True
    else:
        return False
                           


def main():
    testCases=[]
    n = int(input())
    for i in range(n):
        t  = input()
        testCases.append(t)
    
    for j in testCases:
        print(j)
        print("checking......")
        print(checkBalanced(j))     

if __name__ == '__main__':
    main()