from collections import OrderedDict

# 给定的列表
original_list = ["sciUp", "ccf", "utd24", "ajg", "sciBase", "ssci", "sci", "swufe", "cufe", "ssci", "sci", "sciif", "jci", "sciif5", "ahci", "fdu", "sjtu", "xmu", "cssci", "ruc", "cscd", "swjtu", "uibe", "pku", "xdu", "sdufe", "eii", "nju", "zhongguokejihexin", "cqu", "hhu", "ajg", "xju", "cug", "fms", "scu", "utd24", "ft50", "sciUp", "sciBase", "sciwarn", "cju", "zju"]

# 使用OrderedDict去除重复项并保持原始顺序
unique_ordered_list = list(OrderedDict.fromkeys(original_list))

# 将结果输出
formatted_result = ', '.join(unique_ordered_list)
print(formatted_result)
