
from clc_python_five.service.customerservice import Service
from clc_python_five.service.customer import Customer

listOfCustomers = []
class CustomerImpl(Service): #how

    def addCustomer(self,cust):
        if type(cust)==Customer:
            if type(self.getCustomer(cust.customerId))==Customer:
                return 'Duplicate Customer..!'
            else:
                listOfCustomers.append(cust) #append
                return 'Customer Added Successfully..!'
        else:
            return 'Invalid Customer Type..'

    def updateCustomer(self,cust):
        dbcust = self.getCustomer(cust.customerId)
        if type(dbcust)==Customer: #present inside list
            ind = listOfCustomers.index(dbcust) # find existin element cha index
            listOfCustomers[ind]=cust
            return 'customer record updated Successfully....'
        return "Cannot update as customer not exist..!"

    def deleteCustomer(self,cid):
        dbcust = self.getCustomer(cid) #cust[present] -- str [absent]
        if type(dbcust)==Customer:
            listOfCustomers.remove(dbcust)
            return 'Customer deleted Successfully..'

        return "Cannot deleted as customer not exist..!"

    def getAllCustomers(self):
        return listOfCustomers

    def getCustomer(self,cid):
        for cust in listOfCustomers:
            if cust.customerId==cid:
                return cust

        return 'Customer Not Exist..with given identifier..'

