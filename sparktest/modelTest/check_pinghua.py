import settings
import helper
helper.load_settings()
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import pandas as pd

def draw(dt1, dt2):
    plt.figure(figsize=(16,5))
    plt.subplot(111)
    plt.plot(dt1.values, label='origin')
    plt.plot(dt2.values, label='pinghua')
    plt.legend()
    plt.savefig('./pinghua_diff.png')

def Main():
    origin_data = pd.read_csv(settings.origin_data, index_col=0)
    pinghua_data = pd.read_csv(settings.pinghua_data_dir+'/May.csv', index_col=0)
    print(pinghua_data[settings.boiler_columns.get('real_power')])
    draw(origin_data[settings.boiler_columns.get('real_power')],
         pinghua_data[settings.boiler_columns.get('real_power')])


if __name__ == '__main__':
    Main()
