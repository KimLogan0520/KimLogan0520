package ch3;

public class OperatorEx1 {
    public static void main(String[] args) {
        /**
         * i++; ++i; 이 두 문장이 모두 독립적으로 사용되었기 때문에, 두 출력 결과가 동일하다.
         */
        int i = 5;
        i++;
        System.out.println(i);

        i = 5;
        ++i;
        System.out.println(i);
    }
}
