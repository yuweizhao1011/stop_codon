##合并结果
import os


def merge_files():
    result = ""
    # 遍历当前目录下所有以p开头的子目录
    for root, dirs, files in os.walk('.'):
        for dir_name in dirs:
            if dir_name.startswith('p'):
                file_path = os.path.join(root, dir_name,'stop_codon','stopcodon_rate_clean.txt')
                if os.path.isfile(file_path):
                    with open(file_path, 'r', encoding='utf-8') as f:
                        lines = f.readlines()
                        # 处理文件第一行（表头）
                        if lines:
                            header = lines[0].strip()
                            new_header = '样本文件夹\t' + header
                            if not result:
                                result += new_header + '\n'
                        # 处理文件数据行
                        for line in lines[1:]:
                            data = line.strip()
                            new_line = dir_name + '\t' + data
                            result += new_line + '\n'

    # 将合并后的内容写入新文件
    output_path = os.path.join('.', 'all_act_sopcodon_rate.txt')
    with open(output_path, 'w', encoding='utf-8') as f:
        f.write(result)


if __name__ == '__main__':
    merge_files()