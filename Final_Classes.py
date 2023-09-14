

class Inventory:
    def __init__(self,ID,name,stock,price):
        self.__ID=ID
        self.__name=name
        self.__stock=int(stock)
        self.__price=float(price)
    
    def get_id(self):
        return self.__ID
    
    def get_name(self):
        return self.__name
    
    def get_stock(self):
        return self.__stock
    
    def get_price(self):
        return self.__price
    
    def restock(self, new_stock):
        if new_stock>0:
            self.__stock+=new_stock
            return True
        else:
            return False
    
    def purchase(self, purch_qty):
        if self.__stock>=purch_qty:
            self.__stock-=purch_qty
            return True
        else:
            return False
        
    def __str__(self):
        string=self.__ID+3*"\t"+self.__name.rjust(20)+2*"\t"+"$"+str(self.__price)+3*"\t"+str(self.__stock)
        return string

class TransactionItem():
    def __init__(self):
        self.__id=222
        self.__name="Cake"
        self.__quantity=5
        self.__price=10
        
    def set_id(self,new_id):
        self.__id=new_id
    
    def get_id(self):
        return self.__id

    def set_name(self, new_name):
        self.__name=new_name
        
    def get_name(self):
        return self.__name
    
    def set_quantity(self, new_qty):
        self.__quantity=new_qty
        
    def get_quantity(self):
        return self.__quantity
    
    def set_price(self, new_price):
        self.__price=new_price
        
    def get_price(self):
        return self.__price
    
    def calc_cost(self):
        self.total_price=self.__price*self.__quantity
        return self.total_price
    
    def __str__(self):
        string=str(self.__id)+2*"\t"+self.__name.rjust(20)+4*"\t"+str(self.__quantity)+3*"\t"+"$"+str(format(self.__price,'.2f'))+4*"\t"+"$"+str(format(self.total_price,'.2f'))
        return string
        
                
