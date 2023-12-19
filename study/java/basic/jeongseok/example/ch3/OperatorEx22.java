package ch3;

public class OperatorEx22 {
    public static void main(String[] args) {
        float f = 0.1f;
        double d = 0.1; // 사실 double타입의 상수인 0.1도 저장되는 과정에서 오차가 발생하지만, float타입의 리터럴인 0.1f보다는 적은 오차로 저장된다.
        double d2 = (double)f;

        /**
         * 10.0==10.0f는 true인데, 0.1==0.1f는 false인 이유?
         * ==> 정수형과 달리 실수형은 근사값으로 저장되므로 오차가 발생할 수 있기 때문이다.
         */
        System.out.printf("10.0 == 10.0f %b%n", 10.0==10.0f);
        System.out.printf("0.1 == 0.1f %b%n", 0.1==0.1f);

        System.out.println();
        System.out.printf("f = %19.17f%n", f);
        System.out.printf("d = %19.17f%n", d);
        System.out.printf("d2 = %19.17f%n", d2);

        System.out.printf("d == f \t %b%n", d==f);
        System.out.printf("d == d2 \t %b%n", d==d2);
        System.out.printf("d2 == f \t %b%n", d2==f);
        System.out.printf("(float)d == f \t %b%n", (float)d==f);
    }
}
