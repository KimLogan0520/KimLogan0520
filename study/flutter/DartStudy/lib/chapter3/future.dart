void main(){
  /// 비동기 프로그래밍은 서버 요청과 같이 오래 걸리는 작업을 기다린 후 값을 받아와야 하기 때문에, 미래값을 표현하는 Future 클래스가 필요함
  // Future<String> name; // 미래에 받을 String값
  // Future<int> number; // 미래에 받을 int값
  // Future<bool> isOpened; // 미래에 받을 bool값

  addNumbers(1, 1);
}

void addNumbers(int number1, int number2) {
  print('$number1 + $number2 계산 시작!');

  /// Future.delayed()를 사용하면 일정 시간 후에 콜백함수를 실행할 수 있음!
  Future.delayed(Duration(seconds: 3), (){
    print('$number1 + $number2 = ${number1 + number2}');
  });

  print('$number1 + $number2 코드 실행 끝!');
}