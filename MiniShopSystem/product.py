from pydantic import BaseModel , Field, ValidationError 

class Product (BaseModel):
    name: str = Field(min_length=1 )
    price : float = Field(gt= 0)
    stock : int = Field(gt= -1)
    
def product_creator ():
    x=Product(     
    name = input("what is the name for this product?").lower(),
    price = input("what is the price for this product?"),
    stock = input("how is the stock for this product?")
    )
    return x

def product_printer():
   for product in products:
      print(f'name of the product is {product.name} , $ of the product is {product.price} , stock amount of the product is {product.stock} ')

products= []
while True :
    try: 
        product = product_creator()
        #print(product)
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
product_printer()
while True :
    try  :
         selected_item = input("Select an item you want to buy")
         selected_item_ammount = int(input("Select item amount you want to buy"))
         item_found = False
         for product in products : 
                if product.name == selected_item.lower() :
                  item_found = True
                elif item_found == True and product.stock == 0 : 
                    print("we dont have that product in stock right now ")
                elif item_found == True and product.stock  >= selected_item_ammount :
                    print("we have the required amount for you")
                elif item_found == True and product.stock  <= selected_item_ammount:
                    print("we dont have the amount  you wish for")
         if item_found == False:  
                print("we dont have that item")
         else : print("we do have that item")
         break                 
    
    
    except ValueError:print("your imput should be a integer")