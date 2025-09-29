import operator
fp=open("Nikhil.txt","r")
dic={}
for line in fp:
    for word in line.split():
       
        if word in dic:
            dic[word]+=1
        else:
            
            dic[word]=1
print(dic)
sorted_list=dict(sorted(dic.items(),key=operator.itemgetter(1),reverse=True)[:10])
print(str(sorted_list))