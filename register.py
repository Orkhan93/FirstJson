import json
newDict=[]
class User:
    def __init__(self,_name,_surname,_username):
        self.name=_name
        self.surname=_surname
        self.username=_username
        self.addToDataDict()

    def addToDataDict(self):
        myDict=customDict()
        myDict.__add__('name',self.name)
        myDict.__add__('surname',self.surname)
        myDict.__add__('username',self.username)
        newDict.append(myDict)

def newUserRegister():
    name=input("Adiniz : ")
    surname=input("soyadiniz : ")
    username=input("Istifadeci adiniz : ")
    User(name,surname,username)

class customDict(dict):
    def __init__(self):
        self=dict()
    def __add__(self,key,value):
        self[key]=value

for i in range(2):
    newUserRegister()
    print("Qeydiyyat Tamamlandi...")

with open("data.json","w") as connect:
    json.dump(newDict,connect)
