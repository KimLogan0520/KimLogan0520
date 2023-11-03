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

void main(){
  Idol xxx = Idol('XXX', 7) ..sayName() ..sayMembersCount();
}