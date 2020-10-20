# Calculadora-Python-SOAP
A simple calculator for testing the web service with Python, in the SOAP protocol

### Import the library:
from zeep import Client

### Access the web service:
cliente = Client(wsdl='http://www.dneonline.com/calculator.asmx?WSDL')

### Calculates and shows the results of the four operations. Do you can to choose the values, changing the parenthesis values:

print(cliente.service.Add(10,5))

print(cliente.service.Subtract(10,5))

print(cliente.service.Multiply(10,5))

print(cliente.service.Divide(10,5))

