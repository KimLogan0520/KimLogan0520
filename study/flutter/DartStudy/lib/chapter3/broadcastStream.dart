import 'dart:async';

void main(){
  final controller = StreamController();

  /// 여러번 리슨할 수 있는 Broadcast Stream 객체 생성
  final stream = controller.stream.asBroadcastStream();

  /// 첫 listen() 함수
  final streamListener1 = stream.listen((event) {
    print('listening1 ==> $event');
  });

  /// 두번째 listen() 함수
  final streamListener2 = stream.listen((event) {
    print('listening2 ==> $event');
  });

  controller.sink.add(1);
  controller.sink.add(2);
  controller.sink.add(3);

  playStream();
}

/// Stream을 반환하는 함수는 async*로 선언!
Stream<String> calculate(int number) async* {
  for ( int i = 0; i < 5; i++ ) {
    /// StreamController의 add()처럼 yield 키워드를 이용해서 값 반환!!!
    yield 'i = $i';
    await Future.delayed(Duration(seconds: 1));
  }
}

void playStream(){
  /// StreamController와 마찬가지로 listen() 함수로 콜백 함수 입력
  calculate(1).listen((value) {
    print(value);
  });
}