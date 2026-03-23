# 练习 1：创建 list 存储 5 个电影名称，完成切片取前 3 个、倒数 2 个、添加 / 删除元素，熟悉 list 操作
# 练习 2：创建 dict 存储用户 ID 和用户名，完成增删改查，对应 C++ 的 unordered_map
# 练习 3：写一个函数，接收多个电影评分，返回平均分、最高分、最低分（Python 多返回值特性）
# 练习 4：用for...in遍历 dict，打印所有用户 ID 和用户名，熟悉循环语法
# 测试Python基础：列表、字典、循环、函数
print("=== Day1 Python 基础练习 ===")

# 1. 列表（电影列表）
movies = ["肖申克的救赎", "霸王别姬", "阿甘正传", "盗梦空间", "活着"]
print(movies[:3])
print(movies[-2:])
movies.append("星际穿越")
print(movies)
movies.pop()
print(movies)
movies.pop(2)
print(movies)

# 2. 字典（用户信息）
user = {"id": 1001, "name": "UESTCHh", "age": 22}
print(user)
user["age"] = 20
print(user)
user.pop("id")
print(user)

# 3. 函数（计算平均分）
def calc_score(scores):
    avg = sum(scores) / len(scores)
    return avg, max(scores), min(scores)

scores = [4.5, 5.0, 3.5, 4.0]
avg, max_s, min_s = calc_score(scores)
print(f"平均分:{avg}, 最高分:{max_s}, 最低分:{min_s}")