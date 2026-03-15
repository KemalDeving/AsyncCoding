from pydantic import BaseModel , ValidationError , Field
import asyncio

class Musteri(BaseModel):
    username:str = Field(min_length=1 )
    password:str = Field(min_length=6)
    age:int = Field(gt=0)

async def login_basarisi (x):
     print("checking your login")
     await asyncio.sleep(x)
     print("Succesfull")

#i = True
#while i == True:
    # d
     
     
     
try :
    Musteri1 =  Musteri (
        username= input("Whats your username?") , 
        password = input("Whats your password?"),
        age = input("Whats your age?") )
    asyncio.run(login_basarisi(2))
    print (Musteri1)  
    i = False
except ValidationError as e :   
      print (f'Validation went wrong')
      print(e)