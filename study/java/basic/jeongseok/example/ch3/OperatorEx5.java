package ch3;

public class OperatorEx5 {
    public static void main(String[] args) {
        int a = 10;
        int b = 4;

        System.out.printf("%d + %d = %d%n", a, b, a + b);
        System.out.printf("%d - %d = %d%n", a, b, a - b);
        System.out.printf("%d * %d = %d%n", a, b, a * b);
        System.out.printf("%d / %d = %d%n", a, b, a / b); // 이 경우 소수점 이하는 버려진다. int / int = int ( 참고로 반올림 발생하지 않음 )
        System.out.printf("%d / %f = %f%n", a, (float)b, a / (float)b);
    }
}
