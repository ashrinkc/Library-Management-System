def files():
    global bookname,authorname,quantity,cost #using the keyword global makes the variable usable outside the scope of the function
    # empty lists are declared
    bookname=[]
    authorname=[]
    quantity=[]
    cost=[]
    with open("Books.txt","r") as f:    
        lines=f.readlines()
        lines=[line.replace('\n',"") for line in lines]
        for w in lines:
            index=0
            for a in w.split(','):
                if(index==0):
                    bookname.append(a) #appending to list bookname
    
                elif(index==1):
                    authorname.append(a) #appending to list authorname
                    
                elif(index==2):
                    quantity.append(a) #appending to list quantity
                    
                elif(index==3):
                    cost.append(a.strip("$")) #appending to list cost
                    
                index+=1 #incrementing the value by 1 so that we can access all index
