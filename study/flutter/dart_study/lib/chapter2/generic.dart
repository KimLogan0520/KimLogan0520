/// 흔히 사용되는 제네릭 문자들
/// T : 변수 타입을 표현할 때, 예) T value;
/// E : 리스트 내부의 요소들의 타입을 표현할 때, 예) List<E>
/// K : 키를 표현할 때, 예) Map<K, V>
/// V : 값을 표현할 때, 예) Map<K, V>
class Cache<T> {
  final T data;

  Cache({
    required this.data,
  });
}

void main(){
  final cache = Cache<List<int>>(
    data: [1, 2, 3],
  );

  print(cache.data.reduce((value, element) => value + element));
}