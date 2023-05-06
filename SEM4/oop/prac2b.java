import java.util.Scanner;
public class prac2b {
    public static void main(String args[]){
        int date, month, year;
        Scanner sc = new Scanner(System.in);
        System.out.println("enter date");
        date = sc.nextInt();
        System.out.println("\n next is month");
        month = sc.nextInt();
        System.out.println("\nenter year");
        year = sc.nextInt();

        System.out.println("your bday is at " + date + "/"+month+"/"+year);
    }
}
