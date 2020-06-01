from zeep import Client

cliente = Client(wsdl='http://www.dneonline.com/calculator.asmx?WSDL')
print(cliente.service.Add(10,5))
print(cliente.service.Subtract(10,5))
print(cliente.service.Multiply(10,5))
print(cliente.service.Divide(10,5))