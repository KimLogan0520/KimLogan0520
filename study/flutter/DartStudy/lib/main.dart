void main() {
  // 주석
  /**
   * 여러줄 주석
   */
  /// 문서 주석
  /// DartDoc이나 안드로이드 스튜디오 같은 IDE에서 문서(Documentation)으로 인식함

  /**
   * dynamic val
   *  - var는 변수의 값을 이용해서 변수의 타입을 유추, 한번 유추하면 그 이후로는 그 타입으로 고정
   *  - but, dynamic을 이용하면 변수의 타입이 고정되지 않아 다른 타입의 값을 저장할 수 있음
   */
  dynamic name2 = 'Chan';
  print(name2);

  name2 = 1;
  print(name2);

  /**
   * const / final
   *  - final은 런타임 상수
   *  - const는 빌드타임 상수
   */
  final String name3 = 'KimChan';
  // name3 = 'XXX';

  const String name4 = 'KimChan2';
  // name4 = 'XXX';

  final DateTime now = DateTime.now();
  print(now);

  // const로 저장된 변수는 빌드타임에 값을 알 수 있어야 하는데 DateTime.now()함수는 런타임에 반환되는 값을 알 수 있기 때문
  // 코드를 실행하지 않은 상태에서 값이 확정되면 const를, 실행될때 확정되면 final을 사용!!
  // const DateTime now2 = DateTime.now();
  // print(now);

  /**
   * 변수의 타입
   */

}