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
shopping=True
while shopping :
    try  :
         selected_item = input("Select an item you want to buy")
         selected_item_ammount = int(input("Select item amount you want to buy"))
         item_found = False
         for product in products : 
                if product.name == selected_item.lower() :
                  item_found = True
                  if product.stock == 0 : 
                    print("we dont have that product in stock right now ")
                  elif product.stock  >= selected_item_ammount :
                    print("we have the required amount for you")
                    product.stock = product.stock - selected_item_ammount
                    print("thanks for the purchase")
                    print(f'now the new stock for the product is { product.stock }')
                  else :
                    print("we dont have the amount  you wish for")
                  break  
         if item_found == False:  
                print("we dont have that item")
    except ValueError:
        print("your input should be a integer")
    multiple_purchase= input ("you want to continue buying ? just y or n")
    if multiple_purchase.lower() == "y": 
        print("Sure!")
    elif multiple_purchase.lower() == "n":
        shopping=False
        break
    else:
        print("you should only type y or n")
        while True:
         multiple_purchase = input("you want to continue buying ? just y or n ")
         if multiple_purchase.lower() == "y":
              print("Sure!")
              break
         elif multiple_purchase.lower() == "n":
              shopping = False
              break
         else:
            print("ONLY y OR n")

