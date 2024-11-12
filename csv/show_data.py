# %%
import os
os.chdir(os.path.dirname(os.path.abspath(__file__)))  # 设置工作目录为脚本所在目录
import pandas as pd
command_data = pd.read_csv('command_data.csv')
command_a=['k8s_cluster_info_commands', 'k8s_resource_management_commands']
command_data = command_data[command_data['command_group'].isin(command_a)]

# %%
command_data

# %%


# %%
count_data = pd.read_csv('count.csv')
count_data

# %%
merged_data = pd.merge(command_data, count_data, left_on='id', right_on='command_id', how='left')
merged_data


# %%
summary = (
    merged_data.groupby('id_x')
    .agg(
        count_id_x=('id_x', 'count'),
        command_x=('command_x', 'first'),
        des=('description', 'first'),
        total_count=('command_y', 'count'),
        correct_count=('is_correct', lambda x: (x == True).sum())
    )
    .reset_index()
    .sort_values(by=['total_count', 'correct_count'], ascending=[True, True])  # Sort by total_count, then correct_count
)
print(summary.to_string(index=False))

# summary = merged_data.groupby(['id_x', 'command_x', 'description'])['command_id'].count().reset_index(name='count_num')
# print(summary.to_string(index=False))

# %%
import matplotlib.pyplot as plt

fig, ax = plt.subplots(figsize=(10, 6))

# 创建一个条形图，展示 total_count 和 correct_count，不让条形覆盖
import numpy as np

# 设置条形的宽度和位置
bar_width = 0.35
index = np.arange(len(summary['command_x']))

# 画出 total_count 和 correct_count，设置条形不重叠
ax.bar(index, summary['total_count'], width=bar_width, label='Total Count', color='skyblue', align='center')
ax.bar(index + bar_width, summary['correct_count'], width=bar_width, label='Correct Count', color='green', align='center')

# 更新 x 轴标签位置
ax.set_xticks(index + bar_width / 2)
ax.set_xticklabels(summary['command_x'], rotation=45, ha='right')

# 设置标签和标题
ax.set_xlabel('Command')
ax.set_ylabel('Count')
ax.set_title('Total Count vs Correct Count for Each Command')
ax.set_xticklabels(summary['des'], rotation=45, ha='right')

# 显示图例
ax.legend()

# 调整布局并显示
plt.tight_layout()
plt.show()


# After creating the plot
plt.savefig('plot.png')  # Saves the plot as a PNG file

# If you prefer a different format (e.g., JPEG), you can specify the file extension
# plt.savefig('plot.jpg')  # Saves the plot as a JPEG file

import os

# Save the plot
plt.savefig('plot.png')  # Saves the plot as a PNG file

# Open the plot in VS Code
# file_path = os.path.abspath('plot.png')

# %%


# %%
# top_10_count = summary.nlargest(10, 'count_num')
# print(top_10_count.to_string(index=False))

# # %%
# min_10_count = summary.nsmallest(10, 'count_num')
# print(min_10_count.to_string(index=False))


# %%


# %%


# %%


# %%


# %%


# %%


# %%


# %%


# %%


# %%


# %%


# %%


# %%


# %%



