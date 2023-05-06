import java.util.*;
public class prac3a {
    public static void main(String[] args) {
        display dis = new display();
        dis.ans();
    }
}
class display{
    void ans(){
        int chee = 0;
        System.out.println(chee);
        for(chee = 0; chee<50; chee++){

            if(chee%3==0 && chee%5 ==0){
                System.out.println("fixxxxxx : " + chee);
            }
        }
    }
}
