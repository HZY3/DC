import java.net.*;
import java.io.*;

public class IPCServer
{
public static void main(String args[])
{

        System.out.println("\n IPC");
        System.out.println("\n Server process started ");        
        System.out.println("\n Server is ready and waiting to receive data from client");

try
{

                ServerSocket ss= new ServerSocket(8080);
                Socket clientSocket=ss.accept();
                System.out.println("\n Client is connected with IP address" +clientSocket.getInetAddress()+" and port number" + clientSocket.getPort());
                DataOutputStream dos= new DataOutputStream(clientSocket.getOutputStream());
                DataInputStream dis= new DataInputStream(clientSocket.getInputStream());

                int a=dis.readInt();
                System.out.println("\n Server Received");
                System.out.println("\n Number 1  ===>"+a);
                int b=dis.readInt();
                System.out.println("\n Number 2  ===>"+b);
                int c=a+b;
                dos.writeInt(c);
                System.out.println("\n Server has executed the request and sent the result to the client\n");

                clientSocket.close();
                System.out.println("\n Server process exiting");
                ss.close();

}
catch (Exception e)
{
        System.out.println("Exception:"+e);
}
}
}

