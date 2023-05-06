package p1;

import java.util.*;

class Number {
    int FirstNum, SecondNum;
    double result;

    Number(int x, int y) {
        this.FirstNum = x;
        this.SecondNum = y;
    }

    void add() {
        result = this.FirstNum + this.SecondNum;
    }

    void sub() {
        result = this.FirstNum - this.SecondNum;
    }

    void mul() {
        result = this.FirstNum * (this.SecondNum);
    }

    void div() {
        int flag = 0;
        try {
            if (this.SecondNum == 0) {
                flag = 1;
                throw new Exception("Divison by 0 is not allowed");
            }
        } catch (Exception e) {
        }
        if (flag == 1) {
            System.exit(0);
        } else {
            result = this.FirstNum / this.SecondNum;
        }
    }
}

public class best{
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        boolean a1 = true;
        System.out.println("Enter First Number:");
        int a = sc.nextInt();
        System.out.println("Enter Second Number:");
        int b = sc.nextInt();
        Number n = new Number(a, b);
        while (a1) {
            System.out.println("\tMENU");
            System.out.println("1--> ADDITION.");
            System.out.println("2--> SUBTRACTION.");
            System.out.println("3--> MULTIPLICATION.");
            System.out.println("4--> DIVISION.");
            System.out.println("5--> EXIT.");
            System.out.print("Enter your choice:");
            int ch = sc.nextInt();
            switch (ch) {
                case 1:
                    n.add();
                    break;
                case 2:
                    n.sub();
                    break;
                case 3:
                    n.mul();
                    break;
                case 4:
                    n.div();
                    break;
                case 5:
                    System.exit(0);
            }
            System.out.println("Result is:" + n.result);
        }
    }
}