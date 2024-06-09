def nested_sum(t):
    result=0
    for sublist in t:
        result+=sum(sublist)
    return result
#end

def cumsum(a):
    result=[]                        #for item in a:
    s=0                                  #if len(item) == 0:
    for i in a:                             #result.append(item)
        s+=i                             #else
        result.append(s)                    #result.append(item+result.len[-1])
    return result
#endcumsum

def middle(t):
     return t[1:-1]
#endmiddle

def main():
    t=[[1,2],[3],[4,5,6]]
    x=nested_sum(t)
    print(x)
    a=[1,2,3]
    y=cumsum(a)
    print(y)
    t=[1,2,3,4]
    y=middle(t)
    print(y)
#endmain
if __name__  =="__main__":
    main()



