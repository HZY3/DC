import xmlrpc.client

server_url = 'http://localhost:8000'
proxy = xmlrpc.client.ServerProxy(server_url)

# Call the add method
result = proxy.add(2, 3)
print("2 + 3 =", result)

# Call the subtract method
result = proxy.subtract(10, 5)
print("10 - 5 =", result)

# Call the multiply method
result = proxy.multiply(4, 6)
print("4 * 6 =", result)

# Call the divide method
try:
    result = proxy.divide(10, 0)
except xmlrpc.client.Fault as error:
    print("Error:", error.faultString)
else:
    print("10 / 0 =", result)

# Call the divide method with valid arguments
result = proxy.divide(10, 2)
print("10 / 2 =", result)
