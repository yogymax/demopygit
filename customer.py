'''
newly added

'''
print('added by another developer....2333')

class Customer:

    def __init__(self,cid,cnm,cag,cadr,cbal): #constructor- to ini fields
        self.customerId=cid
        self.customerName=cnm
        self.customerAge=cag
        self.customerAddress=cadr
        self.customerBalance=cbal

    def __str__(self): # to represent individual object of customer type
        return f'''\n
                CustomerId : {self.customerId},
                CustomerName : {self.customerName},
                CustomerAge : {self.customerAge},
                CustomerBalance : {self.customerBalance},
                CustomerAddress : {self.customerAddress},
            '''

    def __repr__(self):# to present complex type of customer
        return str(self)

if __name__ == '__main__':
    c1 = Customer(cid=1123,cnm='AAAA',cag=20,cadr='Pune',cbal=29393.4)
    c2 = Customer(cid=11133,cnm='AAAA',cag=20,cadr='Pune',cbal=29393.4)
    c3 = Customer(cid=11421,cnm='AAAA',cag=20,cadr='Pune',cbal=29393.4)
    customers = [c1,c2,c3]
    print(customers)



def newfun():
    print('add new fun')
