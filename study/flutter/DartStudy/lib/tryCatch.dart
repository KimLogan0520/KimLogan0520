void main() {
  try {
    final myName = 'Chan';
    throw Exception('이름이 잘못되었습니다(강제 에러 발생)');
    print(myName);
  } catch(e) {
    print(e);
  }
}