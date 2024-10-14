import os

# 定义文件夹路径
folder_path = "./"  # 请根据实际情况修改路径

# 获取文件夹中的所有文件
files = os.listdir(folder_path)

# 遍历文件并重命名
for file_name in files:
    # 检查文件名是否符合原始格式
    if file_name.startswith("lawbench-") and file_name.endswith("-0-shot.json"):
        # 提取文件名中的数字部分
        parts = file_name.split("-")
        if len(parts) >= 4:
            # 提取前两个数字
            first_number = parts[1]
            second_number = parts[2]
            # 构建新的文件名
            new_file_name = f"{first_number}-{second_number}.json"
            # 重命名文件
            os.rename(os.path.join(folder_path, file_name), os.path.join(folder_path, new_file_name))
            print(f"Renamed: {file_name} -> {new_file_name}")

print("Renaming completed.")
