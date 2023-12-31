/// 일반적으로 프라이빗 변수는 클래스 내부에서만 사용하는 변수를 칭하지만, 다트에서는 같은 파일에서만 접근이 가능한 변수

class Idol {
  /// '_'로 변수명을 시작하면 프라이빗 변수를 선언할 수 있음
  String _name;

  /// 게터
  String get name {
    return this._name;
  }

  /// 세터
  set name(String name) {
    this._name = name;
  }

  Idol(this._name);
}

void main(){
  Idol blackPink = Idol('블랙핑크');

  /// 같은 파일 내에서는 _name 변수에 접근할 수 있지만, 다른 파일에서는 _name 변수에 접근할 수 없다.
  print(blackPink._name);

  blackPink.name = 'xxxx';
  print(blackPink.name);
}