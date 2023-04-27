
import java.net.*;
import java.io.*;

public class IPCClient
{
public static void main(String args[])
{


        try
        {
                Socket s= new Socket("192.168.1.10",8080);
                DataOutputStream dos= new DataOutputStream(s.getOutputStream());
                DataInputStream dis= new DataInputStream(s.getInputStream());
                InputStreamReader isr=new InputStreamReader(System.in);
                System.out.println("\n Client Process has started");

                System.out.println("\n Please enter values of both numbers to pass them to Server Process");
                BufferedReader br= new BufferedReader(isr);
                int a1= Integer.parseInt(br.readLine());
                System.out.println("\n Number 1  ===>" + a1);
               
                dos.writeInt(+a1);

                int b1= Integer.parseInt(br.readLine());
                System.out.println("\n Number 2  ===>" + b1);
                dos.writeInt(+b1);
                int result=dis.readInt();
                System.out.println("\n Client Process has received result from server");
                System.out.println("\n The addition of "+ a1 +" and "+ b1 + " is" + result);
                s.close();        
        }
        catch(Exception e)
        {
                        System.out.println("Exception is " +e);
        }
}
}

Interprocess Communication is a process of exchanging the data between two or more independent process in a distributed environment is called as Interprocess communication. Interprocess communication on the internet provides both Datagram and stream communication.

Examples Of Interprocess Communication:

N number of applications can communicate with the X server through network protocols.
Servers like Apache spawn child processes to handle requests.
Pipes are a form of IPC: grep foo file | sort





It has two functions:

Synchronization:
Exchange of data is done synchronously which means it has a single clock pulse.
Message Passing:
When processes wish to exchange information. Message passing takes several forms such as: pipes, FIFO, Shared Memory, and Message Queues.
Characteristics Of Inter-process Communication:
There are mainly five characteristics of inter-process communication in a distributed environment/system.

Synchronous System Calls:
In the synchronous system calls both sender and receiver use blocking system calls to transmit the data which means the sender will wait until the acknowledgment is received from the receiver and receiver waits until the message arrives.
Asynchronous System Calls:
In the asynchronous system calls, both sender and receiver use non-blocking system calls to transmit the data which means the sender doesn’t wait from the receiver acknowledgment.
Message Destination:
A local port is a message destination within a computer, specified as an integer. Aport has exactly one receiver but many senders. Processes may use multiple ports from which to receive messages. Any process that knows the number of a port can send the message to it.
Reliability:
It is defined as validity and integrity.
Integrity:
Messages must arrive without corruption and duplication to the destination.
Validity:
Point to point message services are defined as reliable, If the messages are guaranteed to be delivered without being lost is called validity.
Ordering:
It is the process of delivering messages to the receiver in a particular order. Some applications require messages to be delivered in the sender order i.e the order in which they were transmitted by the sender.
