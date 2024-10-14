import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.font_manager import FontProperties
# 设置字体
font_path="./fonts/SimHei.ttf"

prop = FontProperties(fname=font_path,size=12)
task_dict={
    "1-1": "法条背诵",
    "1-2": "知识问答",
    "2-1": "文件校对",
    "2-2": "纠纷焦点识别",
    "2-3": "婚姻纠纷鉴定",
    "2-4": "问题主题识别",
    "2-5": "阅读理解",
    "2-6": "命名实体识别",
    "2-7": "舆情摘要",
    "2-8": "论点挖掘",
    "2-9": "事件检测",
    "2-10": "触发词提取",
    "3-1": "法条预测(基于事实)",
    "3-2": "法条预测(基于场景)",
    "3-3": "罪名预测",
    "3-4": "刑期预测(无法条内容)",
    "3-5": "刑期预测(给定法条内容)",
    "3-6": "案例分析",
    "3-7": "犯罪金额计算",
    "3-8": "咨询"
}
# 读取CSV数据
data = pd.read_csv('./results.csv')

# 按任务分组并计算平均得分
task_scores = data.groupby('task')['score'].mean().reset_index()

# 绘制柱状图
plt.figure(figsize=(10, 6))
task_names = [task_dict[task_id] for task_id in task_scores['task']]
scores=task_scores['score']
#keep only on decimal for each score
scores = [round(float(x)*100, 1) for x in scores]
avg_score= sum(scores)/len(scores)
print(avg_score)

# plt.bar(task_names, task_scores['score'], color='skyblue')
# # plt.bar(task_scores['task'], task_scores['score'], color='skyblue')

# # 添加标题和标签
# plt.title('Average Score by Task')
# plt.xlabel('Task')
# plt.ylabel('Average Score')

# # 显示图形
# # plt.show()
# plt.savefig("./lawbench_ds.png")
fig, ax = plt.subplots(figsize=(15, 9))
bars = ax.bar(task_names, scores, color='skyblue')
# ax.set_xlabel('任务类型', fontproperties=prop)
# ax.set_ylabel('分数', fontproperties=prop)
ax.set_title('Legalbrain-DS LawBench Eval', fontproperties=prop)

ax.set_xticks(range(len(task_names)))
ax.set_xticklabels(task_names, rotation=45, fontproperties=prop)
plt.tight_layout()

# Add numbers on top of each bar
ax.bar_label(bars, labels=[f'{c}' for c in scores], padding=3, fontproperties=prop)

# 显示图表
plt.show()
fig.savefig('./legalbrain_ds_lawbench.jpg', dpi=300, bbox_inches='tight')