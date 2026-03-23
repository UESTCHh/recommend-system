# 实现 3 个核心功能：
# 功能 1：统计每部电影的平均评分，输出「电影名称 + 平均分」
# 功能 2：统计每个用户的评分次数、平均评分，输出「用户 ID + 评分次数 + 平均分」
# 功能 3：找出评分最高的 3 部电影，输出排名、电影名称、平均分

# 电影评分统计 - 推荐系统入门实战
print("=== 电影评分统计系统 ===")

ratings = [
    {"user_id": 1, "movie_id": 101, "rating": 4.5, "movie_name": "肖申克的救赎"},
    {"user_id": 1, "movie_id": 102, "rating": 3.5, "movie_name": "霸王别姬"},
    {"user_id": 2, "movie_id": 101, "rating": 5.0, "movie_name": "肖申克的救赎"},
    {"user_id": 2, "movie_id": 103, "rating": 4.0, "movie_name": "阿甘正传"},
    {"user_id": 3, "movie_id": 102, "rating": 4.5, "movie_name": "霸王别姬"},
    {"user_id": 3, "movie_id": 103, "rating": 4.5, "movie_name": "阿甘正传"},
    {"user_id": 4, "movie_id": 104, "rating": 4.8, "movie_name": "盗梦空间"},
    {"user_id": 4, "movie_id": 105, "rating": 3.8, "movie_name": "泰坦尼克号"},
    {"user_id": 5, "movie_id": 104, "rating": 4.9, "movie_name": "盗梦空间"},
]

print(ratings)
# 1. 统计每部电影平均分
movie_scores = {}
movie_count = {}

for r in ratings:
    name = r["movie_name"]
    score = r["rating"]
    if name not in movie_scores:
        movie_scores[name] = 0
        movie_count[name] = 0
    movie_scores[name] += score
    movie_count[name] += 1

print(movie_scores)
print(movie_count)
print("\n【电影平均分】")
for name in movie_scores:
    avg = movie_scores[name] / movie_count[name]
    print(f"{name} : {avg:.2f} 分")


# 2. 统计每个用户评分情况
users = {}
for i in ratings:
    uid = i["user_id"]
    uscore = i["rating"]
    if uid not in users:
        users[uid] = {"total": 0, "count":0}
    users[uid]["total"] += uscore
    users[uid]["count"] += 1

print(users)
print("\n【用户统计】")
for uid, stat in users.items():
    avg = stat["total"] / stat["count"]
    print(f"用户{uid}: 共{stat["count"]}次评分，平均分为{avg:.2f}")

# 3.找出评分最高的 3 部电影
print("\n=== 功能3：评分最高的3部电影（Top3） ===")
movie_avg_list = []
for name in movie_scores:
    avg = movie_scores[name] / movie_count[name]
    movie_avg_list.append([name, avg])

temp_list = movie_avg_list.copy()
top_count = min(3, len(movie_avg_list))
top3 = []
# 找3次，每次找第1、2、3名
for i in range(3):
    # 先假设第一个是当前最高分
    current_max = temp_list[0]
    # 遍历剩下的，找真正的最高分
    for item in temp_list:
        if item[1] > current_max[1]:
            current_max = item
    # 找到后，加入Top3列表
    top3.append(current_max)
    # 从临时列表里移除这个最高分，下次找第二高的
    temp_list.remove(current_max)

print("排名  电影名称        平均分")
print("-----------------------------")
for rank in range(top_count):
    avg_score = top3[rank][1]
    movie_name = top3[rank][0]
    print(f"第{rank+1}名   {movie_name}    {avg_score:.2f}分")