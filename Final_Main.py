
import Final_Classes


def display_menu(item_list):    
    print("ID"+6*"\t"+"Item"+3*"\t"+"Price"+3*"\t"+"Qty Available"+"\n", end='')
    for i in item_list:
        print(i)
        
def display_invoice_and_rewrite_menu(transaction_list,item_list):
    print()
    print("Order complete. See Invoice Below. ")
    print()
    print("ID"+4*"\t"+"Name"+4*"\t"+"Quantity"+3*"\t"+"Price"+3*"\t"+"Total Price",sep='')
    for i in transaction_list:
        print(i)
    new_data=open("UpdatedInventory.txt", "w")
    for i in item_list:
        new_data.write(i.get_id()+"\n")
        new_data.write(i.get_name()+"\n")
        new_data.write(str(i.get_stock())+"\n")
        new_data.write(str(i.get_price())+"\n")
        
def display_receipt(count,total):    
    print()
    print("Total items:",count)
    print("Subtotal: $"+str(format(total,'.2f')))
    
    sales_tax=total*.0850
    print("Sales Tax: $"+str(format(sales_tax,'.2f')))
    
    print("Grand Total: $"+str(format(sales_tax+total,'.2f')))
    


def main():
    item_list=[]
    stripped_item_list=[]
    inventory_data=open("Inventory.txt", "r")
    line_list=inventory_data.readlines()
    length=len(line_list)
    transaction_list=[]
    count=0
    total=0
    
    
    for i in line_list:
        stripped_item=i.rstrip("\n")
        stripped_item_list.append(stripped_item)
        

    for num in range(0,length,4):
        item_id=stripped_item_list[num]
        item_name=stripped_item_list[num+1]
        item_qty=stripped_item_list[num+2]
        item_price=stripped_item_list[num+3]
        object_ex=Final_Classes.Inventory(item_id,item_name,item_qty,item_price)
        item_list.append(object_ex)

      
    id_list=[]
    for i in item_list:
        id_list.append(int(i.get_id()))
    
    display_menu(item_list)
        
    product_id=int(input("Which product ID would you like to purchase? (Enter 0 to exit) "))
    
    
    while product_id!=0:
        while product_id not in id_list:
            print("Invalid product ID. Please try again.")
            product_id=int(input("Which product ID would you like to purchase? (Enter 0 to exit) "))
        
        purchase_return_items=int(input("How many items would you like to purchase? Enter negative numbers for returns. "))
        
        while purchase_return_items==0:
            print("That is not a valid quantity. Please try again. ")
            purchase_return_items=int(input("How many items would you like to purchase? Enter negative numbers for returns. "))
        
        if purchase_return_items>0:
            index_location=id_list.index(product_id)
            purchase=item_list[index_location].purchase(purchase_return_items)
            while purchase is False:
                print("There is not enough inventory to purchase this amount. Try again.")
                purchase_return_items=int(input("How many items would you like to purchase? Enter negative numbers for returns. "))
                purchase=item_list[index_location].purchase(purchase_return_items)
            
            count+=purchase_return_items
            total+=item_list[index_location].get_price()*purchase_return_items
            
            transaction_object=Final_Classes.TransactionItem()
            transaction_object.set_id(product_id)
            transaction_object.set_name(item_list[index_location].get_name())
            transaction_object.set_price(item_list[index_location].get_price())
            transaction_object.set_quantity(purchase_return_items)
            transaction_object.calc_cost()
            transaction_list.append(transaction_object)
        
        elif purchase_return_items<0:
            index_location=id_list.index(product_id)
            restock=item_list[index_location].restock(abs(purchase_return_items))
          
            
            transaction_object=Final_Classes.TransactionItem()
            transaction_object.set_id(product_id)
            transaction_object.set_name(item_list[index_location].get_name())
            transaction_object.set_price(item_list[index_location].get_price())
            transaction_object.set_quantity(purchase_return_items)
            transaction_object.calc_cost()
            transaction_list.append(transaction_object)
            
            count+=purchase_return_items
            total+=item_list[index_location].get_price()*purchase_return_items

        
        
        display_menu(item_list)
        
        product_id=int(input("Which product ID would you like to purchase? (Enter 0 to exit) "))
        
    if product_id==0:
            if len(transaction_list)==0:
                   print("Thank you for visiting!")
            else:
                display_invoice_and_rewrite_menu(transaction_list, item_list)
                display_receipt(count, total)
                


    
            
                
        

            
            

    
    

        
        
        
           
           
           
           

           
           
           
           
           
        


main()                
            
        