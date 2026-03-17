from pydantic import BaseModel , Field, ValidationError

class Product (BaseModel):
    name: str = Field(min_length=1 )
    price : float = Field(gt= 0)
    stock : int = Field(gt= -1)
    

def product_creater ():
    x=Product(     
    name = input("what is the name for this product?"),
    price = input("what is the price for this product?"),
    stock = input("how is the stock for this product?")
    )
    return x
    


try: 
    product1 = product_creater()
    print(product1)
except ValidationError as e :
    print(e)
    print("ValidationError fix your error")