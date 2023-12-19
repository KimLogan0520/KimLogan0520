package ch3;

public class OperatorEx8 {
    public static void main(String[] args) {
        int a = 1_000_000;
        int b = 2_000_000;
        // System.out.println("a = " + a + ", b = " + b);

        long c = (long)a * b;
        System.out.println(c);
    }
}
