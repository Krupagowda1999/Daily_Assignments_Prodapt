import pymongo

client=pymongo.MongoClient("mongodb://localhost:27017/")
mydata=client['studentdetDb']
collection_name=mydata['students']

class StudentDetails:
    pass

while True:
    print("1. create a student detail: ")
    print("2. view student with their marks: ")
    print("3. search a student with class : ")
    print("4. search a student with rollno: ")
    print("5. update a student data and marks based on rollno and class: ")
    print("6. find the average marks of english subject based on class: ")
    print("7. delete a student based on rolno and class: ")
    print("8. print total marks: ")
    print("9. exit: ")
    ch=int(input("enter a choice: "))

    if(ch==1):
        name=input("enter name: ")
        rlno=int(input("enter roll no: "))
        clas=input("enter the class: ")
        em=int(input("enter the english marks: "))
        mm=int(input("enter the maths marks: "))
        som=int(input("enter the social marks: "))
        sim=int(input("enter the science marks: "))
        m=em+mm+som+sim
        a=m/4
        print(m)
        print(a)
        dic={"total":m,"name":name,"rlno":rlno,"class":clas,"em":em,"mm":mm,"som":som,"si":sim}
        collection_name.insert_one(dic)
        print(dic)

    if(ch==2):
        result=collection_name.find()
        for i in result:
            print(i)

    if(ch==3):
        c=input("enter the class to be searched: ")
        result=collection_name.find({"class":c})
        # result=collection_name.find({"$and":[{"class":clas},{"rollno":rlno},{"delflag":0}]})
        # result=collection_name.find({"$or":[{"class":clas},{"rollno":rlno},{"delflag":0}]})
        for i in result:
            print(i)

    if(ch==4):
        rl=int(input("enter the roll no to search: "))
        result2=collection_name.find({"rollno":rl})
        for i in result2:
            print(i)

    if(ch==5):
        rl=int(input("enter the rollno : "))
        name=input("enter the student name to be update: ")
        result3=collection_name.update_one({"roll no":rl},{"$set":{"name":name}})
        print(result3)

    if(ch==6):
        clas=input("enter the class:")
        result=collection_name.aggregate([{"$group":{"_id":"$clas","average":{"$average":"a"}}}])
        for i in result:        
            print(i)  


    if(ch==7):
        clas=input("enter the class to be delete: ")
        d=collection_name.delete_one({"class":clas})
        print(d)

    if(ch==8):
        c=input("enter the class: ")
        result1=collection_name.aggregate([{"$group":{"_id":"$c","total":{"$sum":"m"}}}])
        for i in result1:        
            print(i)  
            

    if(ch==9):
        break



