import sys
import os
sys.path.append(os.path.dirname(__file__))
from main import contents
import random

def judge_quality(total_weight):
    if total_weight < 16.1:
        return "C"
    elif total_weight < 21.5:
        return "B"
    elif total_weight < 26:
        return "A"
    elif total_weight < 29.6:
        return "S"
    elif total_weight < 32.3:
        return "SS"
    else:
        return "SSS"


def method_221(n=100):
    print("\n方法：method_221")
    quality_count = {"SSS":0, "SS":0, "S":0, "A":0, "B":0, "C":0, "废品":0}
    dog_food_consumption = 0
    for _ in range(n):
        # 先抽取五个内容及其权重
        selected = random.sample(contents, 5)
        weights = []
        for item in selected:
            level = random.choices(range(1, item["levels"]+1), weights=item["weights"])[0]
            weight = item["level_weights"][level-1]
            weights.append(weight)
        # 第一步：前两个权重和
        sum2 = weights[0] + weights[1]
        if sum2 < 3:
            quality_count["废品"] += 1
            dog_food_consumption += 14
            continue
        # 第二步：前四个权重和
        sum4 = sum(weights[:4])
        if sum4 < 9:
            quality_count["废品"] += 1
            dog_food_consumption += 28
            continue
        # 第三步：五个权重和
        dog_food_consumption += 50
        sum5 = sum(weights)
        quality = judge_quality(sum5)
        quality_count[quality] += 1
    print(f"模拟{n}次结果：")
    print(f"平均狗粮消耗: {dog_food_consumption/n}")
    print(f"废品: {quality_count['废品']}")
    total_non_feipin = sum(v for k, v in quality_count.items() if k != '废品')
    for k, v in quality_count.items():
        if k != '废品':
            print(f"{k}: {v} ({(v/total_non_feipin*100 if total_non_feipin else 0):.2f}%)")

def method_212(n=100):
    print("\n方法：method_212")
    quality_count = {"SSS":0, "SS":0, "S":0, "A":0, "B":0, "C":0, "废品":0}
    dog_food_consumption = 0
    for _ in range(n):
        # 先抽取五个内容及其权重
        selected = random.sample(contents, 5)
        weights = []
        for item in selected:
            level = random.choices(range(1, item["levels"]+1), weights=item["weights"])[0]
            weight = item["level_weights"][level-1]
            weights.append(weight)
        # 第一步：前两个权重和
        sum2 = weights[0] + weights[1]
        if sum2 < 3:
            quality_count["废品"] += 1
            dog_food_consumption += 14
            continue
        # 第二步：前三个权重和
        sum3 = sum(weights[:3])
        if sum3 < 6:
            quality_count["废品"] += 1
            dog_food_consumption += 21
            continue
        # 第三步：五个权重和
        dog_food_consumption += 50
        sum5 = sum(weights)
        quality = judge_quality(sum5)
        quality_count[quality] += 1
    print(f"模拟{n}次结果：")
    print(f"平均狗粮消耗: {dog_food_consumption/n}")
    print(f"废品: {quality_count['废品']}")
    total_non_feipin = sum(v for k, v in quality_count.items() if k != '废品')
    for k, v in quality_count.items():
        if k != '废品':
            print(f"{k}: {v} ({(v/total_non_feipin*100 if total_non_feipin else 0):.2f}%)")

def method_2111(n=100):
    print("\n方法：method_2111")
    quality_count = {"SSS":0, "SS":0, "S":0, "A":0, "B":0, "C":0, "废品":0}
    dog_food_consumption = 0
    for _ in range(n):
        # 先抽取五个内容及其权重
        selected = random.sample(contents, 5)
        weights = []
        for item in selected:
            level = random.choices(range(1, item["levels"]+1), weights=item["weights"])[0]
            weight = item["level_weights"][level-1]
            weights.append(weight)
        # 第一步：前两个权重和
        sum2 = weights[0] + weights[1]
        if sum2 < 3:
            quality_count["废品"] += 1
            dog_food_consumption += 14
            continue
        # 第二步：前三个权重和
        sum3 = sum(weights[:3])
        if sum3 < 6:
            quality_count["废品"] += 1
            dog_food_consumption += 21
            continue
        # 第三步：前四个权重和
        sum4 = sum(weights[:4])
        if sum4 < 9:
            quality_count["废品"] += 1
            dog_food_consumption += 28
            continue
        # 第四步：五个权重和
        dog_food_consumption += 50
        sum5 = sum(weights)
        quality = judge_quality(sum5)
        quality_count[quality] += 1
    print(f"模拟{n}次结果：")
    print(f"平均狗粮消耗: {dog_food_consumption/n}")
    print(f"废品: {quality_count['废品']}")
    total_non_feipin = sum(v for k, v in quality_count.items() if k != '废品')
    for k, v in quality_count.items():
        if k != '废品':
            print(f"{k}: {v} ({(v/total_non_feipin*100 if total_non_feipin else 0):.2f}%)")

def method_32(n=100):
    print("\n方法：method_32")
    quality_count = {"SSS":0, "SS":0, "S":0, "A":0, "B":0, "C":0, "废品":0}
    dog_food_consumption = 0
    for _ in range(n):
        # 先抽取五个内容及其权重
        selected = random.sample(contents, 5)
        weights = []
        for item in selected:
            level = random.choices(range(1, item["levels"]+1), weights=item["weights"])[0]
            weight = item["level_weights"][level-1]
            weights.append(weight)
        # 第一步：前三个权重和
        sum3 = sum(weights[:3])
        if sum3 < 7:
            quality_count["废品"] += 1
            dog_food_consumption += 21
            continue
        # 第二步：五个权重和
        dog_food_consumption += 50
        sum5 = sum(weights)
        quality = judge_quality(sum5)
        quality_count[quality] += 1
    print(f"模拟{n}次结果：")
    print(f"平均狗粮消耗: {dog_food_consumption/n}")
    print(f"废品: {quality_count['废品']}")
    total_non_feipin = sum(v for k, v in quality_count.items() if k != '废品')
    for k, v in quality_count.items():
        if k != '废品':
            print(f"{k}: {v} ({(v/total_non_feipin*100 if total_non_feipin else 0):.2f}%)")

def method_311(n=100):
    print("\n方法：method_311")
    quality_count = {"SSS":0, "SS":0, "S":0, "A":0, "B":0, "C":0, "废品":0}
    dog_food_consumption = 0
    for _ in range(n):
        # 先抽取五个内容及其权重
        selected = random.sample(contents, 5)
        weights = []
        for item in selected:
            level = random.choices(range(1, item["levels"]+1), weights=item["weights"])[0]
            weight = item["level_weights"][level-1]
            weights.append(weight)
        # 第一步：前三个权重和
        sum3 = sum(weights[:3])
        if sum3 < 7:
            quality_count["废品"] += 1
            dog_food_consumption += 21
            continue
        # 第二步：前四个权重和
        sum4 = sum(weights[:4])
        if sum4 < 9:
            quality_count["废品"] += 1
            dog_food_consumption += 28
            continue
        # 第三步：五个权重和
        dog_food_consumption += 50
        sum5 = sum(weights)
        quality = judge_quality(sum5)
        quality_count[quality] += 1
    print(f"模拟{n}次结果：")
    print(f"平均狗粮消耗: {dog_food_consumption/n}")
    print(f"废品: {quality_count['废品']}")
    total_non_feipin = sum(v for k, v in quality_count.items() if k != '废品')
    for k, v in quality_count.items():
        if k != '废品':
            print(f"{k}: {v} ({(v/total_non_feipin*100 if total_non_feipin else 0):.2f}%)")

def method_41(n=100):
    print("\n方法：method_41")
    quality_count = {"SSS":0, "SS":0, "S":0, "A":0, "B":0, "C":0, "废品":0}
    dog_food_consumption = 0
    for _ in range(n):
        # 先抽取五个内容及其权重
        selected = random.sample(contents, 5)
        weights = []
        for item in selected:
            level = random.choices(range(1, item["levels"]+1), weights=item["weights"])[0]
            weight = item["level_weights"][level-1]
            weights.append(weight)
        # 第一步：前四个权重和
        sum4 = sum(weights[:4])
        if sum4 < 9:
            quality_count["废品"] += 1
            dog_food_consumption += 28
            continue
        # 第二步：五个权重和
        dog_food_consumption += 50
        sum5 = sum(weights)
        quality = judge_quality(sum5)
        quality_count[quality] += 1
    print(f"模拟{n}次结果：")
    print(f"平均狗粮消耗: {dog_food_consumption/n}")
    print(f"废品: {quality_count['废品']}")
    total_non_feipin = sum(v for k, v in quality_count.items() if k != '废品')
    for k, v in quality_count.items():
        if k != '废品':
            print(f"{k}: {v} ({(v/total_non_feipin*100 if total_non_feipin else 0):.2f}%)")
    
def method_5(n=100):
    print("\n方法：method_5")
    quality_count = {"SSS":0, "SS":0, "S":0, "A":0, "B":0, "C":0, "废品":0}
    dog_food_consumption = 0
    for _ in range(n):
        # 先抽取五个内容及其权重
        selected = random.sample(contents, 5)
        weights = []
        for item in selected:
            level = random.choices(range(1, item["levels"]+1), weights=item["weights"])[0]
            weight = item["level_weights"][level-1]
            weights.append(weight)
        # 五个权重和
        dog_food_consumption += 50
        sum5 = sum(weights)
        quality = judge_quality(sum5)
        quality_count[quality] += 1
    print(f"模拟{n}次结果：")
    print(f"平均狗粮消耗: {dog_food_consumption/n}")
    print(f"废品: {quality_count['废品']}")
    total_non_feipin = sum(v for k, v in quality_count.items() if k != '废品')
    for k, v in quality_count.items():
        if k != '废品':
            print(f"{k}: {v} ({(v/total_non_feipin*100 if total_non_feipin else 0):.2f}%)")
    
if __name__ == "__main__":
    method_221(100000)
    method_212(100000)
    method_2111(100000)
    method_32(100000)
    method_311(100000)
    method_41(100000)
    method_5(100000) 

