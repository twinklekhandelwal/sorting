user_list=[2,5,4,3,0,7]
i=0
while(i<len(user_list)):
    j=i+1
    min_index=i
    while(j<len(user_list)-1):
        if(user_list[min_index]>user_list[j]):
            min_index=j
        j=j+1
        tep=user_list[i]
        user_list[i]=user_list[min_index]
        user_list[min_index]=tep
    i=i+1
print user_list
