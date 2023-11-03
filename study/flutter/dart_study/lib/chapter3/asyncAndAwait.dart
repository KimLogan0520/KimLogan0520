// void main() async {
//   await addNumbers(1, 1);
//   await addNumbers(2, 2);
// }

void main() async {
  final result1 = await addNumbers(1, 1);
  print('===========> 결과값1 : $result1');

  final result2 = await addNumbers(2, 2);
  print('===========> 결과값2 : $result2');
}

/// async 키워드는 매개변수 정의와 바디 사이에 작성!
Future<int> addNumbers(int number1, int number2) async {
  print('$number1 + $number2 계산 시작!');

  /// await 는 대기하고 싶은 비동기 함수 앞에 입력한다.
  await Future.delayed(Duration(seconds: 3), (){
    print('$number1 + $number2 = ${number1 + number2}');
  });

  print('$number1 + $number2 계산 끝!');

  return number1 + number2;
}