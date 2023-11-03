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

class BoyGroup extends Idol {
  BoyGroup(
      String name,
      int membersCount
      ) : super (
    name, membersCount
  );

  void sayMale() {
    print('저는 남자 아이돌입니다.');
  }
}

class GirlGroup extends Idol {
  GirlGroup(
      String name,
      int membersCount,
      ) : super(
    name, membersCount
  );

  void sayFemale() {
    print('저는 여자 아이돌입니다.');
  }
}

void main() {
  BoyGroup bts = BoyGroup('BTS', 7);

  bts.sayName();
  bts.sayMembersCount();
  bts.sayMale();
}