import java.rmi.Naming;

public class AddClient
{
 public static void main(String args[])
 {
   try
   {
        AddInterface ai=(AddInterface)Naming.lookup("//localhost/Add");
        System.out.println("the sum of 2 numbers is: "+ai.sum(22,21));
           }
   
   catch(Exception e)
   {
      System.out.println("Client Exception"+e);
    }
  }
 }
   

































/*
emote Method Invocation (RMI) is an API that allows an object to invoke a method on an 
object that exists in another address space, which could be on the same machine or on 
a remote machine. Through RMI, an object running in a JVM present on a computer (Client-side) 
can invoke methods on an object present in another JVM (Server-side). RMI creates a public 
remote server object that enables client and server-side communications through simple method calls on the server object.

Stub Object: The stub object on the client machine builds an information block and sends this information to the server.
Skeleton Object: The skeleton object passes the request from the stub object to the remote object.

These are the steps to be followed sequentially to implement Interface as defined below as follows:
  1.Defining a remote interface
  2.Implementing the remote interface
  3.Creating Stub and Skeleton objects from the implementation class using rmic (RMI compiler)
  4.Start the rmiregistry
  5.Create and execute the server application program
  6.Create and execute the client application program.

Diagram
                            RMI Registry
                            
             2.search using object name           1.register name and OR
             3.remote OR
             -----------                         -----------
             -----------                         -----------
           |  Client    |                       |  Server   |
           |  Procedure |                       | Procedure |
             -----------                         -----------
             local call                           local call
             -----------                         -----------
           |  Client    |                       |  Server   |
           |  Stub      |                       |   Stub    |
             -----------                         -----------
             -----------                         -----------
               remote 
                call
             ----------- 
             -----------                         -----------
   local   |  Rpc       |                       |  Object   | remote kernel
   kernel  |  Transport |                       |  adaptor  |
             -----------                         -----------
             -----------                         -----------
             
                                                 ----------- 
                                                 -----------
                                  result        |  Rpc      |
                         Network Arguments      | transport |
                                                 -----------
                                                 ----------- 
             
             
             
             
*/
