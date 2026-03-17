from pydantic import BaseModel , Field, ValidationError

class Product (BaseModel):
    name: str = Field(min_length=1 )
    price : float = Field(gt= 0)
    stock : int = Field(gt= -1)
    
def product_creator ():
    x=Product(     
    name = input("what is the name for this product?"),
    price = input("what is the price for this product?"),
    stock = input("how is the stock for this product?")
    )
    return x
    
Products= []
a=True
while a == True :
    try: 
        product1 = product_creator()
        print(product1)
        another_list=input("Do you want to create another product? Type y / n")
        if another_list.lower == "y": 
            a==True
        elif another_list.lower == "n":
            break
        else: print("you typed something else please type again")
    except ValidationError as e :
        print(e)
        print("ValidationError fix your error")