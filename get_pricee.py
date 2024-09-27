def get_price(self,quantity):
    try:
        if quantity <=0:
            raise  ValueError("Quantity must be greater than 0")
        discount=0
        if quantity<10:
           pass
        elif 10<=quantity<99:
           discount =10 #10%
        else:
           discount=20 #20#
    #total price
        price=(100-discount)/100*self.price
        return price*quantity

    except ValueError as e:
     print(f"Error occured: {e}")
    return None



  
 

