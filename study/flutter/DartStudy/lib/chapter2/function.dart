/// 1.7 함수와 람다 ( page 60 ~ )
// positional parameter(포지셔널 파라미터, 위치 매개변수)
int addTwoNumbers(int a, int b) {
  return a + b;
}
// 기본값을 갖는 경우
int addTwoNumbers3(int a, [int b = 2]) {
  return a + b;
}

// named parameter(네임드 파라미터, 명명된 매개변수)
int addTwoNumbers2({
  // required : 매개변수가 null값이 불가능한 타입이면 기본값을 지정해주거나 필수로 입력해야 한다는 의미
  required int a,
  required int b
}) {
  return a + b;
}
// 기본값을 갖는 경우
int addTwoNumbers4({
  required int a,
  int b = 4
}) {
  return a + b;
}

// 포지셔널 파라미터와 네임드 파라미터가 동시에 존재하는 함수 ( 이런 경우는 포지셔널 파라미터가 반드시 먼저 위치해야 한다 )
int addTwoNumbers5(
  int a, {
  required int b,
  int c = 4
  }
) {
  return a + b + c;
}

/**
 * << 익명 함수 >>
 *   (매개변수) {
 *     함수 바디
 *   }
 *
 * << 람다 함수 >> : 익명함수에서 {}를 빼고 => 기호를 추가한 것이 람다 함수, 매개변수는 아얘 없거나 하나 이상이어도 됨
 *   (매개변수) => 단 하나의 스테이트먼트
 */

// typedef와 함수
// typedef 키워드는 함수의 시그니처를 정의하는 값으로 보면된다.
// 여기서 시그니처는 함수의 반환값 타입, 매개변수 개수와 타입 등을 말함.
// 즉, 함수의 선언부를 정의하는 키워드이며, 함수가 무슨 동작을 하는지에 대한 정의는 없다.
typedef Operation = void Function(int x, int y);

void add( int x, int y ) {
  print('결괏값 : ${x + y}');
}
void subtract( int x, int y ) {
  print('결괏값 : ${x - y}');
}

void calculate(int x, int y, Operation oper) {
  oper(x, y);
}

void main() {
  print(addTwoNumbers(3, 5));
  print(addTwoNumbers2(a: 2, b: 4));
  print(addTwoNumbers3(77));
  print(addTwoNumbers4(a: 3));
  print(addTwoNumbers5(1, b: 3, c: 7));

  List<int> numbers = [1, 2, 3, 4, 5];

  // 익명함수
  final allMembers = numbers.reduce((value, element) {
    return value + element;
  });
  print(allMembers);

  // 람다함수
  final allMembers2 = numbers.reduce((value, element) => value + element);
  print(allMembers2);

  // typedef는 일반적인 변수의 type처럼 사용이 가능
  Operation oper = add;
  oper(1, 2);
  oper = subtract;
  oper(1, 2);

  calculate(1, 2, add);
}