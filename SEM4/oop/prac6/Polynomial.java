import java.util.*;
class Term{
 int coeff,expo;
 Term() {
 this.coeff = 0;
 this.expo = -99;
 }
}
public class Polynomial {
 Term t[]=new Term[100];
 int len=0;
 Polynomial(){
 for(int i=0;i<100;i++){
 this.t[i]=new Term();
 }
 }
 public boolean excheck(int ex){
 for(int i=0;i<len;i++) {
 if (ex == this.t[len].expo)
 return true;
 }
 return false;
 }
 public void setTerm(int cf,int ex) {
 if (excheck(ex)) {
 System.out.println("Exponent already exists!!");
 }
 else if(len>100){
 System.out.println("Array limit is exceeded!!");
 }
 else if(ex<0){
 System.out.println("Exponent is Negative!!");
 }
 else {
 this.t[len].coeff = cf;
 this.t[len].expo = ex;
 len++;
 }
 }
 public void sort(){
 for(int i=0;i<this.len;i++){
 for(int j=i+1;j<this.len;j++){
 if(t[i].expo>t[j].expo){
 Term temp=new Term();
 temp=t[i];
 t[i]=t[j];
 t[j]=temp;
 }
 }
 }
 }
 public void display(){
 for(int i=0;i<len;i++){
 System.out.println(this.t[i].coeff+"X^"+this.t[i].expo);
 }
 System.out.print(" ");
 }
 public static void main(String[] args) {
 Scanner sc=new Scanner(System.in);
 System.out.print("Enter number of terms:");
 int n=sc.nextInt();
 Polynomial p=new Polynomial();
 for(int i=0;i<n;i++){
 System.out.printf("Enter coefficient of %d:",i+1);
 int c= sc.nextInt();
 System.out.printf("Enter exponent of %d:",i+1);
 int e= sc.nextInt();
 p.setTerm(c,e);
 }
 System.out.println("Before Sorting:");
 p.display();
 System.out.println("");
 System.out.println("After Sorting:");
 p.sort();
 p.display();
 }
}