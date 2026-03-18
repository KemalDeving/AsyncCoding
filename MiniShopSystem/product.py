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
    
products= []

while True :
    try: 
        product = product_creator()
        print(product)
        while True:
            another_list=input("Do you want to create another product? Type y / n")
            if another_list.lower() == "y": 
             products.append(product)
             break
            elif another_list.lower() == "n":
             products.append(product)
             break
            else: print("you typed something else please type again")
        if another_list.lower() == "n":break
            
    except ValidationError as e :
        print(e)
        print("ValidationError fix your error")

print(products)