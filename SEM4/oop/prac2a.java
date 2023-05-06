import java.util.Scanner;
public class prac2a {
    public static void main(String args[]) {
        char ch;
        int ASCII;
        Scanner sc = new Scanner(System.in);
        System.out.println("enter character ");
        ch= sc.next().charAt(0);
        ASCII = (int) ch;
        System.out.println("asci for char is " + ch + " :" + ASCII);
        System.out.println("increment is "+ ++ch);
        
    }
    
}
