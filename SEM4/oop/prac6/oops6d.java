
import java.util.*;
class GSSArray{
 private int arr[];
 int size;
 private int li=-1;
 GSSArray(int s){
 this.size=s;
 this.arr=new int[this.size];
 }
 public void insert(int val){
 if(li==-1){ //Empty
 arr[0]=val;
 li=0;
 System.out.println("Element inserted.");
 }
 else{//Not Empty
 if(li==size-1){
 increaseSize();
 }
 if(val<=arr[0]){
 for(int k=li;k>=0;k--){
 arr[k+1]=arr[k];
 }
 arr[0]=val;
 }
 else if(val>arr[li]){
 arr[li+1]=val;
 }
 else{
 for(int i=li;i>=0;i--){
 if(val>arr[i]){
 for(int j=li;j>i;j--){
 arr[j+1]=arr[j];
 }
arr[i+1]=val;
 break;
 }
 }
 }
 li++;
 System.out.println("Element inserted.");
 }
 }
 public void display(){
 if(li==-1){
 System.out.println("Empty Array.");
 }
 else {
 for (int i = 0; i < arr.length; i++) {
 System.out.print(arr[i] + " ");
 }
 }
 System.out.println("");
 }
 private void increaseSize() {
 int a[] = new int[this.size]; //doubling size
 for (int i = 0; i < arr.length; i++) {
 a[i] = arr[i];
 }
 this.arr= new int[this.size*2];
 for (int i = 0; i < a.length; i++) {
 arr[i] = a[i];
 }
 }
 public boolean delete(int val){
 boolean ch=false;
 for(int i=0;i<arr.length;i++){
 if(arr[i]==val){
 for(int j=i;j<li;j++){
 arr[j]=arr[j+1];
 }
 arr[li]=0;
 li--;
ch=true;
 return ch;
 }
 }
 return ch;
 }
 }
public class oops6d {
 public static void main(String[] args, Scanner scanner, Scanner scanner2) {
 boolean ch=true;
 System.out.print("Enter intial size:");
 int n=scanner.nextInt();
 GSSArray gs=new GSSArray(n);
 while(ch){
 System.out.println("1->Insert.");
 System.out.println("2->Delete.");
 System.out.println("3->Display.");
 System.out.println("4->Exit.");
 System.out.print("Enter your choice:");
 int yc=scanner2.nextInt();
 switch(yc){
 case 1:
 System.out.print("Enter the value:");
 int val=new Scanner(System.in).nextInt();
 gs.insert(val);
 break;
 case 2:
 System.out.print("Enter the value:");
 int val1=new Scanner(System.in).nextInt();
 if(gs.delete(val1)){
 System.out.println("Element Deleted!!");
 }
else{
 System.out.println("Element not found!!");
 }
 break;
 case 3:
 System.out.println("Array is:");
 gs.display();
 break;
 case 4:
 System.exit(0);
 }
 }
 }
}