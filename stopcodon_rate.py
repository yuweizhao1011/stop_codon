import os


def add_otutab_total():
    # 定义文件路径
    input_file = os.path.join(os.getcwd(), 'stop_codon', 'stopcodon_otutab1.txt')
    otutab_file = os.path.join(os.getcwd(), 'result', 'otutab.txt')
    output_file = os.path.join(os.getcwd(), 'stop_codon', 'stopcodon_rate.txt')

    # 检查输入文件是否存在
    if not os.path.exists(input_file):
        print(f"错误：输入文件不存在 - {input_file}")
        return
    if not os.path.exists(otutab_file):
        print(f"错误：otutab文件不存在 - {otutab_file}")
        return

    # 读取otutab.txt计算各样本总序列数
    sample_totals = {}
    with open(otutab_file, 'r') as f:
        header = f.readline().strip().split('\t')
        if len(header) < 2:
            print("错误：otutab.txt格式不正确")
            return
        samples = header[1:]

        for line in f:
            parts = line.strip().split('\t')
            if len(parts) < len(samples) + 1:
                print(f"警告：跳过格式错误的行 - {line}")
                continue
            for i, sample in enumerate(samples):
                try:
                    sample_totals[sample] = sample_totals.get(sample, 0) + int(parts[i + 1])
                except ValueError:
                    print(f"警告：otutab.txt中发现非整数数据 - {line}")
                    continue

    # 检查样本匹配性
    with open(input_file, 'r') as f:
        input_header = f.readline().strip().split('\t')
        input_samples = input_header[1:]

        if set(input_samples) != set(samples):
            print("错误：样本名称不匹配")
            return

    # 生成新行数据（all_zotutotalxvlie行）
    new_row = ['all_zotutotalxvlie']
    for sample in input_samples:
        new_row.append(str(sample_totals.get(sample, 0)))

    # 读取stopcodon_otutab1.txt内容
    with open(input_file, 'r') as f:
        lines = f.readlines()

    # 查找stopcodon_total行
    stopcodon_total_index = None
    for i, line in enumerate(lines):
        if line.startswith('stopcodon_total'):
            stopcodon_total_index = i
            break
    if stopcodon_total_index is None:
        print("错误：未找到stopcodon_total行")
        return
    stopcodon_total_values = lines[stopcodon_total_index].strip().split('\t')[1:]

    # 生成stopcodon_rate行
    stopcodon_rate_row = ['stopcodon_rate']
    for i in range(len(input_samples)):
        try:
            rate = float(stopcodon_total_values[i]) / float(new_row[i + 1])
            stopcodon_rate_row.append(str(rate))
        except ZeroDivisionError:
            stopcodon_rate_row.append('nan')
        except ValueError:
            print(f"警告：数据转换错误，无法计算第 {i + 2} 列的比率")
            stopcodon_rate_row.append('nan')

    # 写入输出文件
    with open(output_file, 'w') as out_f:
        # 写入原文件内容
        out_f.writelines(lines)
        # 写入all_zotutotalxvlie行
        out_f.write('\t'.join(new_row) + '\n')
        # 写入stopcodon_rate行
        out_f.write('\t'.join(stopcodon_rate_row) + '\n')

    print(f"成功生成文件：{output_file}")
    print(f"各样本总序列数：{dict(zip(input_samples, new_row[1:]))}")
    print(f"各样本stopcodon比率：{dict(zip(input_samples, stopcodon_rate_row[1:]))}")


# 执行函数
add_otutab_total()