package ch3;

public class OperatorEx2 {
    public static void main(String[] args) {
        int i = 5, j = 0;

        j = i++;
        /**
         * 위 문장, 후위의 경우 값이 참조된 이후에 값이 증가하기 때문에, 기존 5라는 값이 참조되어 j에 대입되고 난 뒤, 값이 1 증가함
         */
        System.out.println("j = i++; 실행 후, i = " + i + ", j = " + j);

        i = 5;
        j = 0;

        j = ++i;
        /**
         * 위 문장, 전위의 경우 값이 참조되기 전에 값이 증가하기 때문에, 기존 5라는 값에 증가가 먼저 일어나고 참조되기 떄문에 i와 j는 모두 6이 된다.
         */
        System.out.println("j = ++i; 실행 후, i = " + i + ", j = " + j);
    }
}
