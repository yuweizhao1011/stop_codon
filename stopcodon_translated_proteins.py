import os
# 当前路径，假设当前路径是 /disks/node3_RAID6_120TB/zhaoyuwei/meta/lc2/p* 中的一个具体文件夹
current_path = os.getcwd()
# 获取当前文件夹名称
folder_name = os.path.basename(current_path)
# 构建输入文件路径
input_file = os.path.join(current_path, 'temp', 'translated_proteins.faa')
# 构建输出文件夹路径
stop_codon_folder = os.path.join(current_path,'stop_codon')
# 构建输出文件路径
output_file = os.path.join(stop_codon_folder, f'{folder_name}_stopcodon_translated_proteins.faa')

# 检查输入文件是否存在
if os.path.exists(input_file):
    # 检查输出文件夹是否存在，不存在则创建
    if not os.path.exists(stop_codon_folder):
        os.makedirs(stop_codon_folder)
    with open(input_file, 'r') as infile, open(output_file, 'w') as outfile:
        current_header = ''
        current_sequence = ''
        for line in infile:
            if line.startswith('>'):
                # 如果遇到新的注释信息
                if '*' in current_sequence:
                    # 如果上一个序列包含 *，则写入输出文件
                    outfile.write(current_header)
                    outfile.write(current_sequence)
                # 更新当前注释信息和序列
                current_header = line
                current_sequence = ''
            else:
                # 累加序列信息
                current_sequence += line
        # 处理最后一个序列
        if '*' in current_sequence:
            outfile.write(current_header)
            outfile.write(current_sequence)