class:
    def generate_bill_amount(self,item_quantity,items):
        Bill.counter+=1
        self.__bill_amount=0
        self.__bill_id='B'=str(Bill.counter)
        tmp_dict=item_quantity
        a=[]
        for item in tmp_dict:
            a[item.lower()]!=tmp_dict[item]
        for prod,quan in items:
            if item.get_item_id().lower==prod:
                self.__bill_amount+=quan*item.get_price_per
                break
    def get_bill_id(self):
        return self.__bill_id
    def get_bill_amount(self):
        return self.__bill_amount

class customer:
    def __init__(self,customer_name):
        self.__customer_name=customer_name
        self.__payment_status=None
    def pays_bill(self,bill):
        self.__payment_status='paid'
        print(self.__customer_name)
        print(bill.get_bill_id())
        print(bill.get_bill_amount())
    def get_customer_name(self):
        return self.__customer_name
    def get_payment_status(self):
        return self.get_payment_status
class Item:
    def __init__(self,item_id,description,price_per_quantity):
        self.__item_id=item_id
        self.__description=description


    def get_item_id(self):
        return self.__item_id
    def get_description(self):
        return self.__description
    def get_price_per_quantity(self):
        return self.get_price_per_quantity

    item_quantity=('IR987':3,'IR346':2,'IR659':4,'IR123':2)
    c=customer('Sudarshan')
    L1=Item('IR987',"Sunfeast_Marie",100.0)
    L2=Item('IR658',"Kellogs Oats",151.0)
    L3=Item('IR346',"Maggie Noodles",35.75)
    L4=Item('IR234',"Kissan Jam",100.0)
    L5=Item('IR123',"Nescafe",55.5)
    L6=Item('IR111',"Milk",100.0)

    items=[L1,L2,L3,L4,L5,L6]
    b=bill()
    b.generate_bill_amount