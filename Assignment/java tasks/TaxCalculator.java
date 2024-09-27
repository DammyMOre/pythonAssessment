import java.util.Scanner;
public class TaxCalculator{

public static void main(String... args){

Scanner scanner = new Scanner(System.in);

for(int count = 1; count<=3; count++)

System.out.print("Enter your name");
name = scanner.nextLine();

System.out.print("Enter earnings");
int earnings = scanner.nextInt();


if(earning <= 30000){
taxRate = (15/100) * earning;
System.out.println(taxrate);
}

else {
if(earning > 30000);
taxRate = (20/100) * earning;
System.out.println(taxrate);

}







}
}