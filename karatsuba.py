def power(p,n):
    
    for i in range(n):
        p += '0'
    return p

def bitadd(s,m):
    size1=len(s)
    size2 = len(m)
    if size1<size2:
        for i in range(abs(len(s)-len(m))):
            s ='0'+s
    else:
        for i in range(abs(len(s)-len(m))):
                m ='0'+m
    s = s[::-1]
    m = m[::-1]
    final = '0'
    carry=0
    for i in range(len(s)):
        add = int(s[i])+int(m[i])+carry
        digit = add%10
        carry = add//10
        final += str(digit)
        
    final += str(carry)        
    
    p = final[::-1]
    return p[1:len(p)-1:]


def isSmaller(str1, str2): 
  
    n1 = len(str1)  
    n2 = len(str2) 
   
    if (n1 < n2): 
        return True
    if (n2 < n1): 
        return False
   
    for i in range(n1): 
        if (str1[i] < str2[i]): 
            return True
        elif (str1[i] > str2[i]): 
            return False
   
    return False

def findDiff(str1, str2): 
  
     if (isSmaller(str1, str2)): 
        
        temp = str1 
        str1 = str2 
        str2 = temp 
    
     str3 = "" 
   
     n1 = len(str1)  
     n2 = len(str2) 
   
     str1= str1[::-1] 
     str2 = str2[::-1] 
  
     carry = 0
    
     for i in range(n2):  
           
        sub = ((ord(str1[i])-ord('0'))-(ord(str2[i])-ord('0'))-carry) 
        
        if (sub < 0): 
          
            sub = sub + 10
            carry = 1
              
        else: 
            carry = 0
  
        str3 = str3+str(sub)
    
     for i in range(n2,n1): 
      
        sub = ((ord(str1[i])-ord('0')) - carry) 
        if (sub < 0): 
          
            sub = sub + 10
            carry = 1
          
        else: 
            carry = 0
               
        str3 = str3+str(sub ) 
   
     str3= str3[1::-1] 
   
     return str3
 
 
def karatsuba(s,m):

    size1=len(s)
    size2 = len(m)
    if size1<size2:
        for i in range(abs(len(s)-len(m))):
            s ='0'+s
    else:
        for i in range(abs(len(s)-len(m))):
                m ='0'+m
    if len(s)==1:
        p = str(int(s)*int(m))
        return p
    
    else:
        n=len(s)
        x=n//2
        if(n%2!=0):
            x=x+1
        l1 = s[0:(len(s)//2)]
        r1 = s[(len(s)//2):len(s)]
        l2 = m[0:(len(m)//2)]
        r2 = m[(len(m)//2):len(m)]
        p1 = karatsuba(l1,l2)
        #p2 = karatsuba(str(int(l1)+int(r1)),str(int(l2)+int(r2)))
        p2 = karatsuba((bitadd(l1,r1)),(bitadd(l2,r2)))
        p4 = karatsuba(r1,r2)
        #p3=str(int(p2)-int(p4)-int(p1))
        q = findDiff(p2,p4)
        p3 = findDiff(q,p1)
        #p = str(int(p1)*10**len(s)+(int(p3))*10**x+int(p4)) 
        a1 = power(p1,len(s))
        a2 = power(p3,x) 
        a3 = bitadd(a1,a2)
        p = bitadd(a3,p4)
        i=0
        for i in range(len(p)):
            if p[i]!="0":
                break
        p = p[i:len(a3)]
        return p
        return p    

print(karatsuba('255','2'))
