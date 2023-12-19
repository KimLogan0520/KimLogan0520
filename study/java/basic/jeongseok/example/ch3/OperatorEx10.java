package ch3;

public class OperatorEx10 {
    public static void main(String[] args) {
        int a = 1000000;

        int result1 = a * a / a; // 오버플로우 발생!
        int result2 = a / a * a;

        System.out.println(result1);
        System.out.println(result2);
    }
}
