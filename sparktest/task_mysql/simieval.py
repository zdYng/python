# -*- coding: utf-8 -*-
__author__ = 'llj'
# 定时执行程序，检查有无新的样本需要训练，有则下载到本地并进行训练
import random
import subprocess
import sfhd_origin_data_extract
import helper
import settings
helper.load_settings()
import time
import os
import utils
from tools import sync_remote_files
import do_ping_hua
import generate_sample

crontab = '''
#m	h	dom	mon	dow	user	command
*	*	*	*	*	*		$ process
0	1	*	*	*	*		$ process
#10	14	*	*	*	*		$ process
#08	*	*	*	*	*		python t.py
#0	8	*	*	4	*		python t.py
#0	8	1	*	*	*		python t.py
#
'''


class task_item(object):
    def __init__(self, line):
        self.line = line
        line = line.replace('\t', ' ')
        while '  ' in line:
            line = line.replace('  ', ' ')
        vals = line.split(' ')
        if len(vals) <= 6:
            raise RuntimeError('invalid crontab: %s' % line)
        self.m = int(vals[0]) if vals[0].isdigit() else None
        self.h = int(vals[1]) if vals[1].isdigit() else None
        self.dom = int(vals[2]) - 1 if vals[2].isdigit() else None
        self.mon = int(vals[3]) if vals[3].isdigit() else None
        self.dow = int(vals[4]) - 1 if vals[4].isdigit() else None
        if self.dom != None and self.dow != None:
            raise RuntimeError('dom and dow should not be set together: %s' % line)
        self.user = vals[5]
        self.commands = vals[6:]
        self.next_time = 0
        self.last_time = 0
        if vals[0:5].count('*') == 5:
            # 只运行一次
            self._run()
            self.next_time = utils.getNow() + 3600 * 24 * 365
        else:
            self.next_time = self.calc_next_time()

    def test(self):
        utils.log_force('test', self.line)
        cur_time = utils.getNow()
        for i in xrange(10):
            next_time = self.calc_next_time(cur_time)
            utils.log_force('cur_time', utils.getTimeDes(cur_time), 'next_time', utils.getTimeDes(next_time))
            cur_time = next_time + random.randint(-3600 * 24 * 60, 3600 * 24 * 60)

    def calc_next_time(self, now=None):
        if now is None:
            now = utils.getNow()
        next_time = now
        if self.m is not None:
            next_time = utils.getHourSecond(next_time) + self.m * 60
            if next_time < now:
                next_time += 3600

        if self.h is not None:
            offset = next_time - utils.getHourSecond(next_time)
            next_time = utils.getDaySecond(next_time) + self.h * 3600 + offset
            if next_time < now:
                next_time += 3600 * 24

        if self.dow is not None:
            offset = next_time - utils.getDaySecond(next_time)
            next_time = utils.getWeekSecond(next_time) + self.dow * 3600 * 24 + offset
            if next_time < now:
                next_time += 3600 * 24 * 7

        if self.dom is not None:
            offset = next_time - utils.getDaySecond(next_time)
            next_time = utils.getMonthSec(next_time) + self.dom * 3600 * 24 + offset
            if next_time < now:
                for i in xrange(28, 32):
                    next_time += 3600 * 24 * i
                    offset = next_time - utils.getDaySecond(next_time)
                    next_time = utils.getMonthSec(next_time) + self.dom * 3600 * 24 + offset
                    if next_time >= now:
                        break

        if self.mon is not None:
            offset = next_time - utils.getMonthSec(next_time)
            next_time = utils.getTimeSec('%d-%d-01 00:00:00' % (utils.getYear(), self.mon)) + offset
            if next_time < now:
                next_time = utils.getTimeSec('%d-%d-01 00:00:00' % (utils.getYear() + 1, self.mon)) + offset
        return next_time

    def _run(self):
        utils.log_force('run', self.commands, '...')
        if self.commands[0] == '$':
            getattr(self, self.commands[1])()
        else:
            # res = commands.getoutput(self.commands)
            # res = os.system(self.commands)
            child = subprocess.Popen(self.commands)
            child.wait()
        utils.log_force('run', self.commands, 'compelete')
        helper.sleep(3)

    def run(self):
        now = utils.getNow()
        if now < self.next_time:
            return self.next_time
        if self.last_time < self.next_time:
            self.last_time = self.next_time
            self._run()
        self.next_time = self.calc_next_time()
        return max(self.next_time, now + 600)

    def process(self):

        start_time = utils.getTimeSec(utils.getDigitDay(time.time() - 86400 * 10))
        end_time = utils.getTimeSec(utils.getDigitDay(time.time()))
        sfhd_origin_data_extract.time_main(start_time, end_time,settings.tablename,settings.columns)

        do_ping_hua.Main()
        time.sleep(1)
        generate_sample.Main()


class task_manager(object):
    def __init__(self):
        self.task_items = []

    def load_crontab(self, contrab):
        lines = contrab.split('\n')
        for line in lines:
            if line.startswith('#'):
                continue
            line = line.strip()
            if not line:
                continue
            item = task_item(line)
            item.test()
            self.task_items.append(item)

    def run(self):
        while True:
            min_next_time = utils.getNow() + 3600
            for item in self.task_items:
                if helper.need_exit:
                    break
                next_time = item.run()
                min_next_time = min(next_time, min_next_time)
            if min_next_time < utils.getNow():
                min_next_time = utils.getNow() + 600
            wait = min_next_time - utils.getNow()
            utils.log_force('sleep', wait, 'next_time', utils.getTimeDes(min_next_time))
            helper.sleep(wait)
            if helper.need_exit:
                break


if __name__ == "__main__":
    utils.log_force('auto exporter start')
    manager = task_manager()
    manager.load_crontab(crontab)
    manager.run()
    utils.log_force('auto exporter complete')
