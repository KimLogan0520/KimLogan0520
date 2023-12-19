package ch3;

public class OperatorEx28 {
    public static void main(String[] args) {
        int x = 0xAB, y = 0xF;

        System.out.printf("x = %#X \t\t %s%n", x, toBinaryString(x));
        System.out.printf("y = %#X \t\t %s%n", y, toBinaryString(y));

        System.out.println();

        System.out.printf("%#X | %#X = %#X \t%s%n", x, y, x|y, toBinaryString(x|y));
        System.out.printf("%#X & %#X = %#X \t%s%n", x, y, x&y, toBinaryString(x&y));

        System.out.println();

        System.out.printf("%#X ^ %#X = %#X \t%s%n", x, y, x^y, toBinaryString(x^y));
        System.out.printf("%#X ^ %#X ^ %#X = %#X \t%s%n", x, y, y, x^y^y, toBinaryString(x^y^y));
    }

    /**
     * 10진 정수를 2진수로 변환하는 메서드
     * @param int x
     * @return 2진수로 변환된 문자열
     */
    static String toBinaryString(int x) {
        String zero = "00000000000000000000000000000000";
        String temp = zero + Integer.toBinaryString(x);

        return temp.substring(temp.length() -32);
    }
}
