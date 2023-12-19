package ch3;

public class OperatorEx6 {
    public static void main(String[] args) {
        byte a = 10;
        byte b = 20;
        byte c = (byte)(a + b); // java: incompatible types: possible lossy conversion from int to byte
        System.out.println(c);
    }
}
