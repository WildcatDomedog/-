import random

# 13个内容，名称和挡位
content_names = [
    "暴击", "爆伤", "百分比攻击", "百分比生命", "共鸣效率", "共鸣技能", "共鸣解放", "重击", "普攻", "百分比防御", "固定生命值", "固定攻击", "固定防御"
]

# 挡位概率分布
prob_8_double_crit = [23.31, 22.01, 26.55, 6.51, 7.51, 8.09, 3.10, 2.96]  # 双爆词条
prob_8_special = [6.77, 7.75, 19.60, 24.20, 17.57, 13.75, 6.15, 3.34]      # 特殊词条
prob_4_small = [12.15, 46.67, 38.76, 2.43]                                 # 小词条

# 权重分布
double_crit_weights = [7.6700, 8.4843, 9.2986, 10.1129, 10.9271, 11.7414, 12.5557, 13.3700]
special_valid_weights = [4.0900, 4.5643, 5.0386, 5.5129, 5.9871, 6.4614, 6.9357, 7.4100]
special_invalid_weights = [0, 0, 0, 0, 0, 0, 0, 0]
small_valid_weights = [1.7600, 2.3633, 2.9667, 3.5700]
small_invalid_weights = [0, 0, 0, 0]

# 词条类型分配
# 双爆词条：暴击、爆伤
# 特殊有效词条：共鸣解放
# 特殊无效词条：百分比攻击、百分比生命、共鸣效率、共鸣技能、重击、普攻、百分比防御、固定生命值
# 小有效词条：固定攻击
# 小无效词条：固定防御
contents = []
for i, name in enumerate(content_names):
    if i < 2:
        contents.append({"name": name, "levels": 8, "weights": prob_8_double_crit, "level_weights": double_crit_weights})
    elif name == "共鸣解放":
        contents.append({"name": name, "levels": 8, "weights": prob_8_special, "level_weights": special_valid_weights})
    elif name == "固定攻击":
        contents.append({"name": name, "levels": 4, "weights": prob_4_small, "level_weights": small_valid_weights})
    elif name == "固定防御":
        contents.append({"name": name, "levels": 4, "weights": prob_4_small, "level_weights": small_invalid_weights})
    else:
        contents.append({"name": name, "levels": 8, "weights": prob_8_special, "level_weights": special_invalid_weights})



