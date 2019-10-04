
from abc import ABC,abstractmethod

#CRUD == create/read[all/filtered]/update/delete

print('inside service impl')

#Abstraction -- Contract
class Service(ABC): #what -- focus

    @abstractmethod #without imple...mandatory imple-- for childs
    def addCustomer(self):
        pass

    @abstractmethod
    def updateCustomer(self):
        pass

    @abstractmethod
    def deleteCustomer(self):
        pass

    @abstractmethod
    def getAllCustomers(self):
        pass

    @abstractmethod
    def getCustomer(self):
        pass

