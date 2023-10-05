enum Status {
  approved,
  pending,
  rejected,
}

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
  // String 문자열
  String name5 = 'Chan';

  // int 정수
  int isInt = 10;

  // double 실수
  double isDouble = 2.5;

  // bool 불리언(True / False)
  bool isTrue = true;

  print(isInt);
  print(isDouble);
  print(isTrue);

  /**
   * 컬렉션
   *  - 여러값을 하나의 변수에 저장할 수 있는 타입
   *  - 컬렉션 타입은 서로의 타입으로 자유롭게 형변환이 가능하다는 매우 큰 장점
   *  1) 여러 값을 순서대로 저장 => List
   *  2) 특정 키 값을 기반으로 빠르게 값을 검색 => Map
   *  3) 중복된 데이터를 제거할 때 사용 => Set
   */
  /**
   * List
   */
  List<String> blackPinkList = ['리사', '지수', '제니', '로제'];
  print(blackPinkList);
  print(blackPinkList[0]);
  print(blackPinkList.length);

  blackPinkList[3] = 'Chan';
  print(blackPinkList[3]);
  print(blackPinkList);

  // add()
  blackPinkList.add('value');
  print(blackPinkList);

  List<int> numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10];
  print(numbers);

  // where()
  final newEvenList = numbers.where(
      (num) => num % 2 == 0,
  );
  print(newEvenList); // (2, 4, 6, 8, 10) 📍where 함수는 이터러블을 반환
  print(newEvenList.toList()); // Iterable을 List로 다시 변환할때 .toList()를 사용

  // map()
  List<String> lastNames = ['kim', 'lee', 'yong', 'park'];
  final newNames = lastNames.map((e) => 'Chan $e');
  print(newNames);
  print(newNames.toList());

  // reduce()
  List<String> lastNames2 = ['kim', 'lee', 'yong', 'park'];
  final newNames2 = lastNames2.reduce((value, element) => value + ', ' + element);
  print(newNames2); // kim, lee, yong, park 📍reduce()함수는 List 멤버의 타입과 같은 타입을 반환

  // fold() : 📍reduce()함수는 함수가 실행되는 리스트 요소들의 타입이 같아야하지만, fold()함수는 어떠한 타입이든 반환할 수 있음!!
  List<String> lastNames3 = ['kim', 'lee', 'yong', 'park'];

  final allNames = lastNames3.fold<int>(0, (previousValue, element) => previousValue + element.length);
  print(allNames);

  /**
   * Map
   */
  Map<String, String> dictionary = {
    'Harry Potter': '해리 포터',
    'Ron Weasley': '론 위즐리',
    'Hermione Granger': '해르미온느 그레인저',
  };
  print(dictionary['Harry Potter']);

  print(dictionary.keys);
  print(dictionary.keys.toList());
  print(dictionary.values);
  print(dictionary.values.toList());

  /**
   * Set
   */
  Set<String> firstNames = {'Chan', 'Min', 'Choi', 'Park'};
  print(firstNames);
  print(firstNames.contains('Chan')); // 값이 있는지 확인
  print(firstNames.toList()); // 리스트로 변환하기

  List<String> dupNames = ['Chan', 'Chan', 'Choi', 'Lee'];
  print(Set.from(dupNames)); // List타입을 Set으로 변환 ( Set은 중복을 허용하지 않기 때문에 Chan이 하나 삭제 된걸 확인할 수 있음 )

  /**
   * Enum
   *  - 한 변수의 값을 몇가지 옵션으로 제한하는 기능 ( 선택지가 제한적일 때 사용 )
   *  - main함수 외부에 작성
   */
  Status status = Status.approved;
  print(status);

  /**
   * 연산자
   *  - 수치 연산자
   *  - null값 입력 관련 연산자
   *  - 값 비교 연산자
   *  - 타입 비교 연산자
   *  - 논리 연산자
   */
  // 수치 연산자
  double number = 2;
  print(number + 2);
  print(number - 2);
  print(number * 2);
  print(number / 2);
  print(number % 2);

  number++;
  number--;

  number += 2;
  number -= 2;
  number *= 2;
  number /= 2;

  print(number);

  // null 관련 연산자 ( dart언어에서는 변수 타입이 null값을 가지는지 여부를 직접 지정해줘야 한다, 타입 키워드를 그대로 사용하면 기본적으로 null값이 지정될 수 없음, 타입뒤에 '?'를 추가해줘야 null값이 저장될 수 있음
  double? number1 = null;

  double? nullableNum; // 자동으로 null값 지정
  print(nullableNum);

  nullableNum ??= 3; // ??을 사용하면 기존 값이 null일떄만 저장
  print(nullableNum);

  nullableNum ??= 4;
  print(nullableNum);

  // 값 비교 연산자
  int intNumber1 = 1;
  int intNumber2 = 1;

  print(intNumber1 > intNumber2);
  print(intNumber1 < intNumber2);
  print(intNumber1 >= intNumber2);
  print(intNumber1 <= intNumber2);
  print(intNumber1 == intNumber2);
  print(intNumber1 != intNumber2);

  // 타입 비교 연산자
  int intNumber3 = 3;
  print(intNumber3 is int);
  print(intNumber3 is String);
  print(intNumber3 is! int);
  print(intNumber3 is! String);

  // 논리 연산자
  bool result = 12 > 10 && 1 > 0;
  print(result);

  bool result2 = 12 > 10 && 0 > 1;
  print(result);

  bool result3 = 12 > 10 || 1 > 0;
  print(result);

  bool result4 = 12 > 10 || 0 > 1;
  print(result);

  bool result5 = 12 < 10 || 0 > 1;
  print(result);

  /**
   * 제어문
   */
  // if문
  int intNumber4 = 4;
  if ( intNumber4 % 3 == 0 ) {
    print('3의 배수입니다.');
  } else if ( intNumber4 % 3 == 1) {
    print('나머지가 1입니다.');
  } else {
    print('맞는 조건이 없습니다.');
  }

  // switch문
  Status status2 = Status.approved;

  switch(status2) {
    case Status.approved:
      print('승인 상태');
      break;
    case Status.pending:
      print('대기 상태');
      break;
    case Status.rejected:
      print('거절 상태');
      break;
    default:
      print('알 수 없는 상태');
  }

  print(Status.values); // Enum의 모든 수를 리스트로 반환
}