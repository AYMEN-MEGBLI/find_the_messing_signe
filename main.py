from itertools import product
from math import sqrt
def link(l1,l2):
    t=[]
    for i in range(len(l1)):
        a=l1[i]+str(l2[i])+(")" if l1[i]=="sqrt(" else "")
        t.append(a) 
    return t
def sqrt_link(l1):
    t=[]
    for j in l1 :
        t.append(link(j[0],j[1]))
    return t
       
def all_poss_sqrt(list1):
    arr=[]
    for i in range(len(list1)+1):
        a=[""]*len(list1)
        a[:i]=["sqrt("]*i
        arr.extend(product(a,repeat=len(list1)))
    sqrt_prob=[*set(arr)]
    return sqrt_link(zip(sqrt_prob,[list1]*len(sqrt_prob)))

def find(*arr,target,maxR=0):
    if maxR>1:return "not found"
    operation=("+","-","*","/","%")#"**" : >9**9**9 : imp : 
    for ops in product(operation,repeat=len(arr)-1) :
        exp=str(arr[0])
        for i,signe in enumerate(ops,start=1):
            exp+=signe+str(arr[i]) 
        try :
            
            if eval(exp)==target :
                return f"{exp} = {target} "
        except ZeroDivisionError :
            continue
        except OverflowError:
            continue
    t=all_poss_sqrt(arr)
    
    for i in t :
        if x:=find(*i,target=target,maxR=maxR+1):
            return x
for i in range(2,10):
    print(i,"=> ",find(*[i]*3,target=6))


