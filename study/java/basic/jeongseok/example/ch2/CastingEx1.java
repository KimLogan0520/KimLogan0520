package ch2;

public class CastingEx1 {
    public static void main(String[] args) {
        double d = 85.4;
        int score = (int)d;

        System.out.println("score = " + score);
        System.out.println("d = " + d);

        /**
         *      ㅁㅁㅁㅁㅁㅁㅁㅁ ㅁㅁㅁㅁㅁㅁㅁㅁ ㅁㅁㅁㅁㅁㅁㅁㅁ ㅁㅁㅁㅁㅁㅁㅁㅁ => 32bit(4byte)
         * (1) 절대값 2의 2진수 구하기 : 00000000 00000000 00000000 00000010(2)
         * (2) 0 -> 1, 1 -> 0     : 11111111 11111111 11111111 11111101(2)
         * (3) +1                 : 11111111 11111111 11111111 11111110(2)
         * ==> 따라서 -2를 2진수로 표현하면 11111111 11111111 11111111 11111110(2)이 된다.
         */
    }
}
