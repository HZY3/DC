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
   
