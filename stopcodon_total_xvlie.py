import os

def calculate_column_sums():
    # 指定文件路径
    input_file = os.path.join(os.getcwd(), 'stop_codon', 'stopcodon_otutab.txt')
    output_file = os.path.join(os.getcwd(), 'stop_codon', 'stopcodon_otutab1.txt')
    
    # 检查输入文件是否存在
    if not os.path.exists(input_file):
        print(f"错误：输入文件不存在 - {input_file}")
        return
    
    # 读取文件内容
    with open(input_file, 'r') as f:
        lines = f.readlines()
    
    # 解析表头
    if not lines:
        print("错误：文件为空")
        return
    
    header = lines[0].strip().split('\t')
    sample_columns = header[1:]  # 提取样本列名
    num_samples = len(sample_columns)
    
    # 初始化各列总和
    column_sums = [0] * num_samples
    
    # 逐行处理数据
    for line_num, line in enumerate(lines[1:], start=2):  # 行号从2开始（第一行为表头）
        parts = line.strip().split('\t')
        if len(parts) < num_samples + 1:
            print(f"警告：跳过格式错误的行（行号 {line_num}） - {line.strip()}")
            continue
        
        for i in range(1, num_samples + 1):
            value = parts[i]
            if not value.isdigit():
                print(f"警告：行号 {line_num} 第 {i} 列包含非整数 '{value}'，已跳过")
                continue
            column_sums[i-1] += int(value)
    
    # 生成新行
    new_line = ['stopcodon_total'] + list(map(str, column_sums))
    
    # 写入输出文件（覆盖模式）
    with open(output_file, 'w') as f:
        # 写入原始内容
        f.writelines(lines)
        # 追加新行
        f.write('\t'.join(new_line) + '\n')
    
    print(f"成功生成新文件：{output_file}")
    print(f"各样本列总和：{dict(zip(sample_columns, column_sums))}")

# 执行函数
calculate_column_sums()