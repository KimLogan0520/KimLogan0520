import 'dart:async';

void main(){
  final controller = StreamController();
  final stream = controller.stream;

  /// Stream listen() 함수를 실행하면, 값이 주입될 때마다 콜백함수를 실행할 수 있다.
  final streamListener1 = stream.listen((value) {
    print(value);
  });

  controller.sink.add(1);
  controller.sink.add(2);
  controller.sink.add(3);
  controller.sink.add(4);
}