import os
import json

# 定义文件夹路径
folder_path = "./"  # 请根据实际情况修改路径

# 获取文件夹中的所有文件
files = os.listdir(folder_path)
cleaned_dir="./cleaned"
# 遍历文件并提取所需字段
for file_name in files:
    if file_name.endswith(".json"):
        file_path = os.path.join(folder_path, file_name)
        final_info = {}
        with open(file_path, 'r', encoding='utf-8') as file:
            data = json.load(file)
            for key, item in data.items():
                print(f"key:{key}")
                origin_prompt = item.get("origin_prompt")
                prediction = item.get("prediction")
                gold = item.get("gold")
                
                _origin_prompt = origin_prompt[0].get("prompt")
                _prediction = prediction
                _refr= gold
                
                final_info[key]=dict(origin_prompt=_origin_prompt,prediction=_prediction,refr=_refr)
        cleaned_path = os.path.join(cleaned_dir, file_name)
        with open(cleaned_path ,"w") as fp:
            # save final_info to "./cleaned/"   
            json.dump(final_info, fp, ensure_ascii=False, indent=4)


print("Extraction completed.")
