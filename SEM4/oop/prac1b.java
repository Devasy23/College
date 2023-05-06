import java.util.Scanner;
public class prac1b {
    public static void main(String args[]){
        byte b=2;
        short s=12;
        int i = 120;
        float f = 8.34f;
        double d = 3.1456;
        long l= 12345; 
        char c = 'h';
        boolean mbool = true;
        Scanner mobj = new Scanner(System.in);
        String username = mobj.nextLine();
        System.out.println("byte" + b);
        System.out.println("short" + s);
        System.out.println("int" + i);
        System.out.println("float"+ f);
        System.out.println("long" + l);
        System.out.println("char" + c);
        System.out.println("bool"+ mbool);
        System.out.println("username is "+ username);
        
    }

    
}
