참여학교들 = ["가 고등학교", "나 고등학교", "다 고등학교", "라 고등학교", "마 고등학교", "가 고등학교", "나 고등학교", "다 고등학교"]

세트 = set()
# for 학교 in 참여학교들:
#     세트.add(학교)

세트.update(참여학교들)

print(f"{len(세트)}개 학교, {세트}")