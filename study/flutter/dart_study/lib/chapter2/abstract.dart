abstract class Idol {
  final String name;
  final int membersCount;

  Idol(this.name, this.membersCount); // 생성자 선언

  void sayName(); // 추상 메서드 선언
  void sayMembersCount(); // 추상 메서드 선언
}

class GirlGroup implements Idol {
  final String name;
  final int membersCount;

  GirlGroup(this.name, this.membersCount);

  @override
  void sayName(){
    print('저는 여자 아이돌 ${this.name}입니다.');
  }

  @override
  void sayMembersCount(){
    print('${this.name} 멤버는 총 ${this.membersCount}명 입니다.');
  }
}

void main() {
  GirlGroup xxxx = GirlGroup('XXXX', 48);

  xxxx.sayName();
  xxxx.sayMembersCount();
}