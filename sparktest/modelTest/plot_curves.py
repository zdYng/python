import const
import sys
import utils
import matplotlib

print("matplotlib.use('Agg')")
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np

output_dir = ''


def do_plot(data_file_name):
    # matplotlib.use('Agg')
    global output_dir
    output_dir = data_file_name[:data_file_name.rfind('/')]
    in_file = open(data_file_name, 'r')
    # 根据---------将数据分块，一块画一张图
    data_blocks = []
    data_lines = []
    for line in in_file:
        line = line.strip()
        if not line:
            continue
        if line.startswith('--------------'):
            data_blocks.append(data_lines)
            data_lines = []
            continue
        data_lines.append(line)
    in_file.close()
    for i, data_lines in enumerate(data_blocks):
        print('plot', i, 'curve', 'data lines num', len(data_lines))
        if is_row_format(data_lines):
            info = _load_row_plot_data(data_lines)
        else:
            info = _load_col_plot_data(data_lines)
        plot_curve(info)


def is_row_format(data_lines):
    pos = -1
    for i, line in enumerate(data_lines):
        if 'format' in line and 'row' in line:
            pos = i
    if pos != -1:
        data_lines.pop(pos)
        return True
    else:
        return False


def _load_col_plot_data(data_lines):
    print( '_load_col_plot_data', len(data_lines))
    # 读取数据
    file_name = data_lines.pop(0)
    if file_name.startswith('[file_name]'):
        file_name = file_name.replace('[file_name]', '')
    file_name = file_name.strip()
    file_name = file_name.replace(' ', '_')
    print('file_name', file_name)

    title = file_name
    if data_lines[0].startswith('[title]'):
        title = data_lines.pop(0)
    title = title.strip()
    print('title', title)

    curve_names = data_lines.pop(0)
    curve_names = curve_names.split('\t')
    print('curve_names', curve_names)

    x_lables = []
    data = []
    for line in data_lines:
        vals = line.split('\t')
        x_lables.append(vals[0])
        vals = utils.parse_vals(vals[1:])
        data.append(vals)
    curve_vals = utils.trans(data)
    x_vals = [i for i in range(len(x_lables))]
    print
    ('x_lables', x_lables)
    print
    ('x_vals', x_vals)
    for i, curve_val in enumerate(curve_vals):
        print
        ('curve_val', i, curve_val)
    if len(curve_names) > len(curve_vals):
        curve_names = curve_names[-len(curve_vals):]
    info = {
        'file_name': file_name,
        'title': title,
        'curve_names': curve_names,
        'x_lables': x_lables,
        'x_vals': x_vals,
        'curve_vals': curve_vals,
    }
    return info


def _load_row_plot_data(data_lines):
    print('_load_row_plot_data', len(data_lines))
    # 读取数据
    file_name = data_lines.pop(0)
    if file_name.startswith('[file_name]'):
        file_name = file_name.replace('[file_name]', '')
    file_name = file_name.strip()
    file_name = file_name.replace(' ', '_')
    print
    ('file_name', file_name)

    title = file_name
    if data_lines[0].startswith('[title]'):
        title = data_lines.pop(0)
    title = title.strip()
    print
    ('title', title)

    curve_names = []
    data = []
    for line in data_lines:
        vals = line.split('\t')
        curve_names.append(vals[0])
        vals = utils.parse_vals(vals[1:])
        data.append(vals)
    print
    ('curve_names', curve_names)
    x_lables = [str(v) for v in data[0]]
    x_vals = [i for i in range(len(x_lables))]
    print
    'x_lables', x_lables
    print
    'x_vals', x_vals
    curve_vals = data[1:]
    for i, curve_val in enumerate(curve_vals):
        print
        'curve_val', i, curve_val
    if len(curve_names) > len(curve_vals):
        curve_names = curve_names[-len(curve_vals):]
    info = {
        'file_name': file_name,
        'title': title,
        'curve_names': curve_names,
        'x_lables': x_lables,
        'x_vals': x_vals,
        'curve_vals': curve_vals,
    }
    return info


def plot_curve(info):
    # 导入 matplotlib 的所有内容（numpy 可以用 np 这个名字来使用）
    # 创建一个 8 * 6 点（point）的图，并设置分辨率为 80
    # matplotlib.use('Agg')
    matplotlib.rcParams['font.size'] = 18
    plt.figure(figsize=(16, 9), dpi=80)

    # 创建一个新的 1 * 1 的子图，接下来的图样绘制在其中的第 1 块（也是唯一的一块）
    plt.subplot(1, 1, 1)

    file_name = info['file_name']
    title = info['title']

    x_vals = info['x_vals']
    x_lables = info['x_lables']

    curve_names = info['curve_names']
    curve_vals = info['curve_vals']
    # 使用蓝色的、连续的、宽度为 1 （像素）的线条
    for i, curve in enumerate(curve_vals):
        print
        'x_vals', x_vals, 'curve', curve
        plt.plot(x_vals, curve, 'o', color=const.colors[i], linewidth=2.0, linestyle="-", label=curve_names[i])
    print
    'plot', len(curve_vals), 'curves'
    plt.title(title)

    min_x = min(x_vals)
    max_x = max(x_vals)
    num_x = len(x_vals)
    # 设置横轴的上下限
    plt.xlim(min_x, max_x)
    if len(x_vals) > 10:
        num = len(x_vals)
        interval = int(num // 10 + 1)
        # 只显示部分x_label
        x_lables = [x_lables[i] if i % interval == 0 else '' for i in range(num)]
    # 设置横轴记号
    print
    'x_vals', len(x_vals), 'x_lables', len(x_lables)
    plt.xticks(x_vals, x_lables)

    # 设置纵轴的上下限
    min_y = 1e09
    max_y = -1e09
    for curve_val in curve_vals:
        max_y = max(max_y, max(curve_val))
        non_zero_vals = [v for v in curve_val if v != 0.0]
        if non_zero_vals:
            min_y = min(min_y, min(non_zero_vals))
    if min_y == max_y or min_y == -1e09:
        min_y = max_y - 1.0
    min_y = min_y - (max_y - min_y) * 0.1
    max_y = max_y + (max_y - min_y) * 0.1
    plt.ylim(min_y, max_y)
    print
    'min_y,max_y = ', min_y, max_y
    # 设置纵轴记号
    plt.yticks(np.linspace(min_y, max_y, 10, endpoint=True))
    plt.legend(loc='upper right')
    fig_name = '%s/%s.jpg' % (output_dir, file_name)
    plt.savefig(fig_name)
    print
    'save fig_name', fig_name, 'complete'
    plt.close()


if __name__ == '__main__':
    if len(sys.argv) >= 2:
        data_file_name = sys.argv[1]
        print('plot ', data_file_name)
    else:
        data_file_name = '/home/data/avatar_features/dist/dist_battle_stats.txt'
        data_file_name = '/home/data/avatar_features/model/plain_dnn_model_20170503021637/fit_curve.txt'
        print('plot default data', data_file_name)
    do_plot(data_file_name)
