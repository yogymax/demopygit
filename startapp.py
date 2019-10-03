
from clc_python_five.service.customer import Customer
from clc_python_five.service.customerserviceimpl import CustomerImpl

impl = CustomerImpl()
import sys
if __name__ == '__main__':
    c1 = Customer(cid=1111,cnm='AAA',cag=20,cadr='Pune',cbal=2938.34)
    c2 = Customer(cid=1231, cnm='BBB', cag=20, cadr='Pune', cbal=2938.34)
    c3 = Customer(cid=1111, cnm='CCC', cag=20, cadr='Pune', cbal=2938.34)

    result1 =impl.addCustomer(c1)
    result2 =impl.addCustomer(c2)
    print(result1)
    print(result2)


    result = impl.deleteCustomer(2344)

    print('result delete -- ',result)

    print('--------------before update------------------')
    customers = impl.getAllCustomers()
    print(customers)


    result2 = impl.updateCustomer(c3)
    print(result2)
    print('---------------------------------')
    result = impl.getCustomer(1231)
    print(result)

    print('--------------after update------------------')
    customers = impl.getAllCustomers()
    print(customers)


    sys.exit(0)
    customers = impl.getAllCustomers()
    print(customers)

