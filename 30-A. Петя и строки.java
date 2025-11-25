import java.util.Scanner;

public class MyClass {
  public static void main(String args[]) {
    Scanner scanner = new Scanner(System.in);

    String a = scanner.nextLine().toLowerCase();
    String b = scanner.nextLine().toLowerCase();

    int result = a.compareTo(b);

    if (result < 0) {
        System.out.println(-1);
    }
    else if (result > 0) {
        System.out.println(1);
    }
    else {
        System.out.println(0);
    }
  }
}
