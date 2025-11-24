import java.util.Scanner;

public class MyClass {
  public static void main(String args[]) {
    Scanner scanner = new Scanner(System.in);
    String line = scanner.nextLine();
    int a = Integer.parseInt(line);
    
    if (a != 2 && a % 2 ==0) {
      System.out.println("YES");
    }
    else{
      System.out.println("NO");
    }
  }
}
