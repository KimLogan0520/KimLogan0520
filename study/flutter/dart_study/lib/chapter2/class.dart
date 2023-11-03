class Chan {
  String name = 'Chan';

  void sayName(){
    // 클래스 내부의 속성을 지칭하고 싶을때는 this키워드를 사용하면된다. ( 결과적으로 this.name은 Idol클래스의 name변수를 지칭한다.
    print('저는 ${this.name}입니다.');
    // 스코프 안의 같은 속성 이름이 하나만 존재한다면, this를 생략할 수 있다.
    print('저는 $name입니다.');
  }
}

class Idol {
  final String name;

  Idol(String name) : this.name = name; // ===> Idol(this.name); 이렇게 this를 사용할 경우도 동일하게 동작한다.

  void sayName(){
    print('저는 ${this.name}입니다.');
  }
}

class Idol2 {
  final String name;
  final int membersCount;

  // 생성자
  Idol2(String name, int membersCount) : this.name = name, this.membersCount = membersCount;

  // 네임드 생성자
  Idol2.fromMap(Map<String, dynamic> map) : this.name = map['name'], this.membersCount = map['membersCount'];

  void sayName(){
    print('저는 ${this.name}입니다. ${this.name} 멤버는 총 ${this.membersCount}명 입니다.');
  }
}

void main(){
  Chan chan = Chan();
  chan.sayName();

  Idol blackPink = Idol('블랙핑크');
  blackPink.sayName();

  Idol bts = Idol('BTS');
  bts.sayName();

  // 기본 생성자 사용
  Idol2 blackPink2 = Idol2('블랙핑크', 4);
  blackPink2.sayName();

  // 네임드 생성자 사용 ( 네임드 생성자는 클래스를 여러 방식으로 인스턴스화할 때 유용하게 사용됩니다. )
  Idol2 bts2 = Idol2.fromMap({
    'name': 'BTS',
    'membersCount': 7
  });
  bts2.sayName();
}