package ch2;

public class PrintfEx2 {
    public static void main(String[] args) {
        String url = "www.codechobo.com";

        float f1 = .10f; // 0.10
        float f2 = 1e1f; // 10.0
        float f3 = 3.14e3f;
        double d = 1.23456789;

        /**
         * %f : 기본적으로 소수점 아래 6자리까지만 출력함
         * %e : 지수형태로 출력할 때
         * %g : 값을 간략하게 표현할 때
         */
        System.out.printf("f1 = %f, %e, %g%n", f1, f1, f1);
        System.out.printf("f2 = %f, %e, %g%n", f2, f2, f2);
        System.out.printf("f3 = %f, %e, %g%n", f3, f3, f3);

        System.out.printf("d = %f%n", d);
        /**
         * %전체자리.소수점아래자리f, 전체 14자리 중에서 소수점 10자리, d =   1.2345678900
         * ( 소수점(.)도 한자리를 차지하고, 소수점 아래의 빈자리는 0으로 채우고, 정수의 빈자리는 공백으로 채워서 전체 자리수를 맞춤.
         */
        System.out.printf("d = %14.10f%n", d);

        System.out.printf("[12345678901234567890]%n");
        System.out.printf("[%s]%n", url); // 문자열의 길이만큼 출력공간을 확보
        System.out.printf("[%20s]%n", url); // 최소 20글자 출력공간 확보 ( 우측 정렬 )
        System.out.printf("[%-20s]%n", url); // 최소 20글자 출력공간 확보 ( 좌측 정렬 )
        System.out.printf("[%.8s]%n", url); // 왼쪽에서 8글자만 출력
    }
}
