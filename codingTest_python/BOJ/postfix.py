
exp =list(map(str, input().rstrip()))    

ans = []        
st = []      
priority = {'*':3,'/':3,'+':2,'-':2,'(':1}     

for i in range(len(exp)):    
    if exp[i].isalpha(): 
        ans.append(exp[i])
    elif exp[i] == '(':  
            st.append(exp[i])
    elif exp[i] == ')':  
        while st[-1] != '(':
            ans.append(st.pop())
        st.pop() 
    else:   
        while st and priority[exp[i]] <= priority[st[-1]]:
            ans.append(st.pop())
        st.append(exp[i]) 

while len(st) != 0:  
    ans.append(st.pop())

print(''.join(ans))