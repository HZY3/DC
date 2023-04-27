
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
