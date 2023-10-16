/// 믹스인은 특정 클래스에 원하는 기능들만 골라 넣을 수 있는 기능
/// 특정 클래스를 지정해서 속성들을 정의할 수 있으며, 지정한 클래스를 상속하는 클래스에서도 사용할 수 있음

class Idol {
  final String name;
  final int membersCount;

  Idol(this.name, this.membersCount);

  void sayName(){
    print('저는 ${this.name}입니다.');
  }

  void sayMembersCount(){
    print('${this.name} 멤버는 총 ${this.membersCount}명 입니다.');
  }
}

mixin IdolSingMixin on Idol {
  /// Idol 클래스에 sing이라는 기능(method)을 추가
  void sing(){
    print('${this.name}이 노래를 부릅니다.');
  }
}

class BoyGroup extends Idol with IdolSingMixin {
  BoyGroup(super.name, super.membersCount);

  void sayMale(){
    print('저는 남자 아이돌입니다.');
  }
}

void main(){
  BoyGroup bts = BoyGroup('BTS', 8);

  bts.sing();
}