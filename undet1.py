# 读取merged1.fq中的所有注释行
merged1_ids = set()
with open('./temp/merged1.fq', 'r') as f:
    while True:
        # 读取四行为一个记录
        header = f.readline()  # @行
        if not header:
            break
        seq = f.readline()     # 序列行
        plus = f.readline()    # +行（跳过但不存储）
        qual = f.readline()    # 质量行
        
        # 将@行存入集合
        merged1_ids.add(header.strip())  # 添加strip()处理换行符差异

# 处理merged0.fq并输出差异记录
with open('./temp/merged0.fq', 'r') as fin, open('./temp/undet.fq', 'w') as fout:
    while True:
        header = fin.readline()  # @行
        if not header:
            break
        seq = fin.readline()     # 序列行
        plus = fin.readline()    # +行（原始内容）
        qual = fin.readline()    # 质量行
        
        # 如果当前@行不在merged1中
        if header.strip() not in merged1_ids:  # 统一用strip()比较
            # 写入修改后的四行记录
            fout.write(header)        # 保持原始头行
            fout.write(seq)           # 保持原始序列
            fout.write("+\n")         # 强制第三行只写+（关键修改点）
            fout.write(qual)          # 保持原始质量分数