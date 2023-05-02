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
























'''
Remote Procedure Call (RPC) is a powerful technique for constructing distributed, client-server based applications. 
It is based on extending the conventional local procedure calling so that the called procedure need not exist in the 
same address space as the calling procedure. The two processes may be on the same system, or they may be on different 
systems with a network connecting them. 

The following steps take place during a RPC : 
1.A client invokes a client stub procedure, passing parameters in the usual way. The client stub resides within the client’s own address space. 

2.The client stub marshalls(pack) the parameters into a message. Marshalling includes converting the representation of the parameters into a 
  standard format, and copying each parameter into the message. 
  
3.The client stub passes the message to the transport layer, which sends it to the remote server machine. 

4.On the server, the transport layer passes the message to a server stub, which demarshalls(unpack) the 
  parameters and calls the desired server routine using the regular procedure call mechanism. 
  
5.When the server procedure completes, it returns to the server stub (e.g., via a normal procedure call return), 
  which marshalls the return values into a message. The server stub then hands the message to the transport layer. 
  
6.The transport layer sends the result message back to the client transport layer, which hands the message back to the client stub. 

7.The client stub demarshalls the return parameters and execution returns to the caller.
(diagram)
Conclusion: RPC is a protocol tat provides the high level of communication paradigm used in distributed systems. Thus we have successfully implemented Remote Procedure Call (RPC).
Remote Procedure Call CRPC)
'''
