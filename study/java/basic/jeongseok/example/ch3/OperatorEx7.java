package ch3;

public class OperatorEx7 {
    public static void main(String[] args) {
        byte a = 10;
        byte b = 30;
        byte c = (byte)(a*b); // 결과는 300이 아닌 44가 출력됨, byte형의 범위가 -128~127이므로 300의 값을 대입한다고 하더라도 보존할수가 없다.
        System.out.println(c);
    }
}
