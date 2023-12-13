package ch2;

public class OverflowEx {
    public static void main(String[] args) {
        /**
         * short와 char는 2byte(16bit)이므로 표현할 수 있는 값의 개수가 동일하다.
         * 하지만...
         * short는 이중 절반을 음수를 표현하는데 사용하고,
         * char는 전체를 양수와 0을 표현하는데 사용.
         */
        short sMin = -32768;
        short sMax = 32767;
        char cMin = 0;
        char cMax = 65535;

        System.out.println("sMin   = " + sMin);
        System.out.println("sMin-1 = " + (short)(sMin-1)); // 최소값에 -1하면 결국 최대값
        System.out.println();
        System.out.println("sMax   = " + sMax);
        System.out.println("sMax+1 = " + (short)(sMax+1)); // 최대값에 +1하면 결국 최소값
        System.out.println();
        System.out.println("cMin   = " + (int)cMin);
        System.out.println("cMin-1 = " + (int)--cMin);
        System.out.println("cMax   = " + (int)cMax);
        System.out.println("cMax+1 = " + (int)++cMax);
    }
}
