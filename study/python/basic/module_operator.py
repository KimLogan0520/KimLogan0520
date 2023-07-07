import operator

books = [
    {
        "title": "book 11",
        "price": 18000
    },
    {
        "title": "book 22",
        "price": 26000
    },
    {
        "title": "book 33",
        "price": 24000
    }
]

print("# 가장 저렴한 책")
print(min(books, key=operator.itemgetter("price")))
print()

print("# 가장 비싼 책")
print(max(books, key=operator.itemgetter("price")))
print()