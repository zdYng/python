# -*- coding: UTF-8 -*-

import time
import sys
import binascii
import uuid
import socket
import struct
import os
import math
import decorator
import shutil

split = ''

LOG_INTERVAL = 5


def getTimeDes(sec=None):
    if sec is None:
        sec = int(time.time())
    tplSec = time.localtime(sec)
    # return '%d-%d-%d %d:%d:%d' % tplSec[:6]
    return time.strftime('%Y-%m-%d %X', tplSec)



def getTimeDay(sec=None):
    if sec is None:
        sec = int(time.time())
    tplSec = time.localtime(sec)
    return '%04d-%02d-%02d' %tplSec[:3]


def getTimeSec(desc):
    if isinstance(desc, int):
        desc = str(desc)
    if len(desc) == 0:
        return getNow()
    if len(desc) <= 10:
        return getDateSec(desc)
    if desc.count('-') == 1:
        time_local = time.strptime(desc, '%Y%m%d-%H:%M:%S')
    elif desc.count('-') == 2:
        time_local = time.strptime(desc, '%Y-%m-%d %H:%M:%S')
    return int(time.mktime(time_local))


def getDateSec(desc):
    time_local = time.strptime(desc, '%Y%m%d')
    return int(time.mktime(time_local))


def getHMSec(desc):
    time_local = time.strptime(desc, '%H:%M')
    return time_local.tm_hour * 3600 + time_local.tm_min * 60


class Logger(object):
    def __init__(self):
        self.lastPrintTime = 0
        self.log_file = None

    def _set_log_file(self, filename):
        self.log_file = open(filename, 'w')

    def _reset_log_file(self, ):
        if self.log_file:
            self.log_file.close()
        self.log_file = None

    def _print(self, msg):
        info = '%s : %s' % (getTimeDes(), msg)
        print(info)
        sys.stdout.flush()
        if self.log_file:
            self.log_file.write(info + '\n')
            self.log_file.flush()
        self.lastPrintTime = time.time()

    def log(self, msg, isDirect):
        if isDirect:
            self._print(msg)
            return

        if time.time() - self.lastPrintTime > LOG_INTERVAL:
            self._print(msg)


logger = Logger()


def log(msg, isDirect=True):
    logger.log(msg, isDirect)


def log_force(*args):
    info = [str(i) for i in args]
    logger.log(' '.join(info), True)


def set_log_file(filename):
    log_force('set_log_file', filename)
    logger._set_log_file(filename)


def reset_log_file():
    log_force('reset_log_file')
    logger._reset_log_file()


def log_easy(*args):
    info = [str(i) for i in args]
    logger.log(' '.join(info), False)


def output_dict(file_name, data, isAppend=False):
    if isAppend:
        of = open(file_name, 'a')
    else:
        of = open(file_name, 'w')

    of.write('# -*- coding: GB18030 -*-  \n')
    of.write('data = {\n')
    for k, v in data.iteritems():
        of.write("\t%s : %s ,\n" % (repr(k), repr(v)))

    of.write('}\n')
    of.close()


def _get_file_name(stat_name, type_name):
    return '%s.%s' % (stat_name, type_name)


def output_txt(stat_name, data, col_names, isAppend=False):
    if not data:
        return
    file_name = _get_file_name(stat_name, 'txt')
    if isAppend:
        of = open(file_name, 'a')
    else:
        of = open(file_name, 'w')

    of.write(split + '\n')
    head = '\t'.join(col_names)
    of.write(head + '\n')
    cache_col_names = col_names[1:]
    keys = data.keys()
    keys.sort()
    # for key, cache in data.iteritems():
    for key in keys:
        cache = data[key]
        row = '%s' % str(key)
        if isinstance(cache, dict):
            for col_name in cache_col_names:
                row += '\t%s' % repr_val(cache.get(col_name, 0))
        else:
            row += '\t%s' % repr_val(cache)
        of.write(row + '\n')
    of.write('\n\n')
    of.close()


def repr_val(val):
    if isinstance(val, float):
        return '%.2f' % val
    return repr(val)


def bytes_to_char(bytes):
    return binascii.hexlify(bytes).upper()


def getTableOriginName(tableName):
    if tableName[-8:].isdigit():
        return tableName[:-9]
    else:
        return tableName


def getTableDateSec(tableName):
    date_str = tableName[-8:]
    if not date_str.isdigit():
        return 0
    date = time.strptime(date_str, "%Y%m%d")
    return int(time.mktime(date))


def getNow():
    return int(time.time())


def getHour(sec=None):
    if sec is None:
        sec = getNow()
    return time.localtime(sec).tm_hour


def getHourSecond(sec=None):
    if sec is None:
        sec = getNow()
    tplSec = time.localtime(sec)
    diff = tplSec[4] * 60 + tplSec[5]
    hour = sec - diff
    return hour


def getMinSecond(sec=None):
    if sec is None:
        sec = getNow()
    tplSec = time.localtime(sec)
    diff = tplSec[5]
    hour = sec - diff
    return hour


def getDaySecond(sec=None):
    # ���ص���0:00:00��timestamp
    if sec is None:
        sec = getNow()

    tplSec = time.localtime(sec)

    diff = tplSec[3] * 60 * 60 + tplSec[4] * 60 + tplSec[5]

    wee = sec - diff

    return wee


def getDayTime(sec=None):
    tplSec = time.localtime(sec)
    diff = tplSec[3] * 60 * 60 + tplSec[4] * 60 + tplSec[5]
    return diff


def convert_to_const(data, **kwargs):
    return data


def getDigitDay(sec=None):
    if sec is None:
        sec = getNow()
    tplSec = time.localtime(sec)
    return '%4d%02d%02d' % tuple(tplSec[:3])


def getDigitMonth(sec=None):
    if sec is None:
        sec = getNow()
    tplSec = time.localtime(sec)
    return '%4d%02d01' % tuple(tplSec[:2])

def _time(t):
    if t is None:
        return ''
    if isinstance(t, str):
        return t
    if isinstance(t, unicode):
        return t
    return time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(int(t)))


def _ip(ip):
    if not ip:
        return ''

    if not isinstance(ip, int) and not isinstance(ip, long):
        return ip
    reverseStr = socket.inet_ntoa(struct.pack('I', socket.htonl(ip)))
    resList = reverseStr.split('.')
    resList.reverse()
    return '.'.join(resList)


def _dur_min(dur):
    return '%.1f min' % (dur / 60.0)


def _dur(dur):
    if dur < 60:
        return '%d sec' % dur
    elif dur < 3600:
        return '%.1f min' % (dur / 60.0)
    elif dur < 86400:
        return '%.1f hour' % (dur / 3600.0)
    else:
        return '%.1f day' % (dur / 86400.0)

def getJsonData(res, keys=None, printers=None):
    data = []
    for d in res:
        item = _getJsonData(d, keys, printers)
        data.append(item)
    return data


def _getJsonData(d, keys, printers):
    item = {}
    if keys:
        printer = None
        for key in keys:
            if key not in d:
                item[key] = ''
                continue
            if printers:
                printer = printers.get(key)
            val = d[key]
            if printer == '_time':
                item[key] = _time(val)
            elif printer == '_ip':
                item[key] = _ip(val)
            elif printer == '_dur':
                item[key] = _dur(val)
            elif printer == '_dur_min':
                item[key] = _dur_min(val)
            else:
                # try:
                #	if isinstance(val, unicode):
                #		sval = val.encode('UTF-8')
                #	item[key] = sval
                # except:
                item[key] = val

    else:
        for key, val in d.iteritems():
            item[key] = val
    return item


def get_output_file_name(table_name, begin_t, end_t, ext='log'):
    begin_t = begin_t.replace('-', '').replace(':', '')
    end_t = end_t.replace('-', '').replace(':', '')
    begin_t = begin_t[4:12]
    end_t = end_t[4:12]
    if table_name[-8:].isdigit():
        table_name = table_name[:-9]
    return 'logs/%s_%s_%s.%s' % (table_name, begin_t, end_t, ext)

def get_wait_dur(num):
    if num > 10000:
        return 0.3
    elif num > 1000:
        return 0.2
    else:
        return 0.1


def getRealTables(tableName, t, te, expire_data):
    expireType = expire_data.get(tableName, {}).get('type', None)
    if expireType is None:
        raise RuntimeError('%s table has no index' % tableName)
    if expireType == 1:
        if getDigitDay(t) != getDigitDay(te):
            realTables = [
                '%s_%s' % (tableName, getDigitDay(t)),
                '%s_%s' % (tableName, getDigitDay(te)),
            ]
        else:
            realTables = [
                '%s_%s' % (tableName, getDigitDay(t)),
            ]
    elif expireType == 2:
        if getDigitMonth(t) != getDigitMonth(te):
            realTables = [
                '%s_%s' % (tableName, getDigitMonth(t)),
                '%s_%s' % (tableName, getDigitMonth(te)),
            ]
        else:
            realTables = [
                '%s_%s' % (tableName, getDigitMonth(t)),
            ]
    else:
        realTables = [tableName, ]
    return realTables


def getFatStr(val, num):
    if len(val) < num:
        left = (num - len(val)) / 2
        right = (num - len(val)) - left
        val = ' ' * left + val + ' ' * right
    return val


def getHtmlData(rows, titles, keys):
    if not rows:
        return ''
    res = ['<html><body><table border="1" bordercolor="black" rules="all"> ']
    cache = []
    for t in titles:
        cache.append('<th>%s</th>' % t)
    res.append('<tr>%s</tr>' % ''.join(cache))
    for row in rows:
        cache = []
        for key in keys:
            val = row.get(key, '-')
            if type(val) is unicode:
                val = val  # .encode('gbk')
            elif type(val) is not str:
                val = str(val)
            cache.append('<td>%s</td>' % val)
        res.append('<tr>%s</tr>' % ''.join(cache))
    res.append('</table></body></html>')
    return '\r\n'.join(res)


def getWeekSecond(sec=None):
    if sec is None:
        sec = getNow()
    tplSec = time.localtime(sec)
    diff = tplSec[3] * 60 * 60 + tplSec[4] * 60 + tplSec[5] + tplSec[6] * 3600 * 24
    return sec - diff


def getMonthSec(sec=None):
    if sec is None:
        sec = getNow()
    tplSec = time.localtime(sec)
    diff = (tplSec[2] - 1) * 3600 * 24 + tplSec[3] * 3600 + tplSec[4] * 60 + tplSec[5]
    return sec - diff


def getMonth(sec=None):
    if sec is None:
        sec = getNow()
    tplSec = time.localtime(sec)
    return tplSec[1]


def getYear(sec=None):
    if sec is None:
        sec = getNow()
    tplSec = time.localtime(sec)
    return tplSec[0]


def getYearSecond(sec=None):
    if sec == None:
        sec = getNow()
    tplSec = time.localtime(sec)
    return getTimeSec('%d-01-01 00:00:00' % tplSec[0])


def getMaintenceSec(sec=None):
    if sec is None:
        sec = getNow()
    mainTime = getWeekSecond(sec) + 3600 * 24 * 3 + 3600 * 8
    if sec < mainTime:
        mainTime -= 3600 * 24 * 7
    return mainTime

def getHexUUID(b):
    return str(uuid.UUID(bytes=b))


def oppositeCamp(camp):
    if camp == 1:
        return 2
    elif camp == 2:
        return 1
    return 0

def get_match_dirs(path, match_name, end=None, need_local_name=False):
    match_dirs = []
    names = os.listdir(path)
    for name in names:
        if not name.startswith(match_name):
            continue
        file_name = '%s/%s' % (path, name)
        if not os.path.isdir(file_name):
            continue
        if need_local_name:
            match_dirs.append(name)
        else:
            match_dirs.append(file_name)
    return match_dirs

def get_match_files(path, match_name, end=None, need_local_name=False):
    match_files = []
    names = os.listdir(path)
    for name in names:
        if not name.startswith(match_name):
            continue
        if end and not name.endswith(end):
            continue
        file_name = '%s/%s' % (path, name)
        if not os.path.isfile(file_name):
            continue
        if need_local_name:
            match_files.append(name)
        else:
            match_files.append(file_name)
    return match_files

# 得到全部二级目录下的指定文件
def get_second_file_list(input_dir, dir_start, file_start, file_end):
    ret_file_list = []
    file_dirs = get_match_dirs(input_dir, dir_start)
    for file_dir in file_dirs:
        file_list = get_match_files(file_dir, file_start, file_end)
        ret_file_list.extend(file_list)
    return ret_file_list


def get_file_date(file_name, split_name=''):
    if not split_name:
        return parse_file_date(file_name)
    start = file_name.rfind(split_name) + len(split_name)
    while not file_name[start].isdigit():
        start += 1
    end = file_name.rfind('.')
    if start > end:
        raise RuntimeError('get_file_date.error : can not get file date for %s' % file_name)
    return file_name[start:end]


def get_raw_name(file_name, keep_date=False):
    if '/' in file_name:
        file_name = file_name[file_name.rfind('/') + 1:]
    if '.' in file_name:
        file_name = file_name[:file_name.rfind('.')]
    if keep_date:
        return file_name
    cols = file_name.split('_')
    vals = [col for col in cols if not col.isdigit()]
    return '_'.join(vals)


def get_local_name(file_name):
    if '/' in file_name:
        return file_name[file_name.rfind('/') + 1:]
    else:
        return file_name


def parse_file_date(file_name):
    if '/' in file_name:
        file_name = file_name[file_name.rfind('/') + 1:]
    if '.' in file_name:
        file_name = file_name[:file_name.rfind('.')]
    if '(' in file_name:
        file_name = file_name[:file_name.rfind('(')]
    cols = file_name.split('_')
    if len(cols) >= 3 and cols[-3].isdigit() and cols[-2].isdigit():
        return '%s_%s' % (cols[-3], cols[-2])
    elif cols[-2].isdigit() and cols[-1].isdigit():
        return '%s_%s' % (cols[-2], cols[-1])
    else:
        # raise RuntimeError('get_file_date.error : can not get file date for %s'%file_name)
        return ''


def get_file_pairs(*args):
    date_pairs = {}
    count = 0
    for file_names in args:
        count += 1
        for file_name in file_names:
            file_date = get_file_date(file_name)
            cache = date_pairs.setdefault(file_date, [])
            cache.append(file_name)
    res = {}
    for date, cache in date_pairs.iteritems():
        if len(cache) != count:
            continue
        res[date] = cache
    return res


def list_plus(list_a, list_b, list_c):
    for i in xrange(len(list_a)):
        list_c[i] = list_a[i] + list_b[i]


def list_multi(list_a, list_b, list_c):
    for i in xrange(len(list_a)):
        list_c[i] = list_a[i] * list_b[i]


def list_multi_weight(list_a, weight, list_c):
    for i in xrange(len(list_a)):
        list_c[i] = list_a[i] * weight


def list_diff(list_a, list_b, list_c):
    for i in xrange(len(list_a)):
        list_c[i] = list_a[i] - list_b[i]


def list_max(list_a, list_b, list_c):
    for i in xrange(len(list_a)):
        list_c[i] = max(list_a[i], list_b[i])


def list_min(list_a, list_b, list_c):
    for i in xrange(len(list_a)):
        list_c[i] = min(list_a[i], list_b[i])


def list_sqrt(list_a, list_b):
    for i in xrange(len(list_a)):
        list_b[i] = math.sqrt(list_a[i])

@decorator.decorator
def log_call(func, self, *args, **kwargs):
    t1 = getNow()
    func_name = '%s.%s' % (self.__class__.__name__, func.__name__)
    if args:
        log_force(func_name, args, '...')
    else:
        log_force(func_name, '...')
    res = func(self, *args, **kwargs)
    t2 = getNow()
    if args:
        log_force(func_name, args, 'complete, cost %d seconds,' % (t2 - t1), 'res =', res)
    else:
        log_force(func_name, 'complete, cost %d seconds,' % (t2 - t1), 'res =', res)

    return res


cost_cache = {}


@decorator.decorator
def log_cost(func, self, *args, **kwargs):
    t1 = time.time()
    res = func(self, *args, **kwargs)
    t2 = time.time()
    func_name = '%s.%s' % (self.__class__.__name__, func.__name__)
    cost_cache[func_name] = cost_cache.get(func_name, 0.0) + (t2 - t1)
    return res


def show_cost():
    l = [(v, k) for k, v in cost_cache.iteritems()]

    l.sort(reverse=True)
    for v, k in l:
        log_force('method', k, 'cost', v)


def reset_cost():
    cost_cache.clear()


def get_scalars_info(scalars):
    if len(scalars) < 10:
        return 'dim = %d vals = %s' % (len(scalars), str(scalars))
    else:
        head_vals = ','.join([str(s) for s in scalars[:3]])
        end_vals = ','.join([str(s) for s in scalars[-3:]])
        return 'dim = %d vals = [%s,...,%s] max_val = %s min_val = %s' % (
        len(scalars), head_vals, end_vals, max(scalars), min(scalars))


def evaluate_error(y_origin, y_predict):
    info = []
    num = len(y_origin)
    avg_err = 0
    sqr_err = 0
    max_err = 0
    os = []
    ps = []

    avg_pre = 0
    avg_ori = 0

    for i in xrange(num):
        if i < 10:
            os.append('%.4f' % y_origin[i][0])
            ps.append('%.4f' % y_predict[i])
        err = abs(y_origin[i] - y_predict[i])
        max_err = max(err, max_err)
        avg_err += err
        sqr_err += err * err
        avg_pre += y_predict[i]
        avg_ori += y_origin[i][0]
    avg_pre = avg_pre / num
    avg_ori = avg_ori / num

    std_pre = 0
    std_ori = 0
    for i in xrange(num):
        std_pre += (y_predict[i] - avg_pre) * (y_predict[i] - avg_pre)
        std_ori += (y_origin[i][0] - avg_ori) * (y_origin[i][0] - avg_ori)

    std_pre = math.sqrt(std_pre / num)
    std_ori = math.sqrt(std_ori / num)

    avg_err = avg_err / num
    sqr_err = math.sqrt(sqr_err / num)
    info.append('origin  = ' + '\t'.join(os))
    info.append('predict = ' + '\t'.join(ps))
    info.append('avg_ori = %s , std_ori = %s' % (avg_ori, std_ori))
    info.append('avg_pre = %s , std_pre = %s' % (avg_pre, std_pre))
    return avg_err, std_pre, '\n'.join(info)


def simplify_value(val, val_range=None):
    if val_range == None:
        val_range = val
    if val_range > 100000:
        return int(val / 1000.0) * 1000
    elif val_range > 10000:
        return int(val / 100.0) * 100
    elif val_range > 1000:
        return int(val / 10.0) * 10
    elif val_range > 100:
        return int(val)
    elif val_range > 10:
        return int(val * 10) / 10.0
    elif val_range > 1:
        return int(val * 100) / 100.0
    elif val_range > 0.1:
        return int(val * 1000) / 1000.0
    elif val_range > 0.01:
        return int(val * 10000) / 10000.0
    else:
        return val


def is_scalar(val):
    return isinstance(val, int) or isinstance(val, float)


def _cp_file(src_dir, dst_dir, file_name, need_override):
    src_file_name = "%s/%s" % (src_dir, file_name)
    dst_file_name = "%s/%s" % (dst_dir, file_name)
    if not os.path.isfile(src_file_name):
        log_force('warning: cp_scalar_infos miss scalar_names.txt')
        return
    if not os.path.isdir(dst_dir):
        log_force('waring: _cp_file dst_dir not exist', dst_dir)
        return
    if os.path.isfile(dst_file_name) and not need_override:
        log_force('skip exist dst_file_name', dst_file_name)
        return
    log_force('cp file_name', file_name)
    shutil.copyfile(src_file_name, dst_file_name)
    time.sleep(1)


def cp_scalar_infos(src_dir, dst_dir, need_override):
    _cp_file(src_dir, dst_dir, 'scalar_names.txt', need_override)
    _cp_file(src_dir, dst_dir, 'scalar_info.txt', need_override)
    _cp_file(src_dir, dst_dir, 'scalar_normalize_data.npz', need_override)


def trans(data):
    n = len(data)
    m = len(data[0])
    new_data = [
    ]
    for j in xrange(m):
        new_data.append([None for i in xrange(n)])
    for i in xrange(n):
        for j in xrange(m):
            new_data[j][i] = data[i][j]

    return new_data


num_chs = ('-', '0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '.',)


def is_num(val):
    if not val:
        return False
    for ch in val:
        if ch not in num_chs:
            return False
    if val.count('-') > 1:
        return False
    if val.count('.') > 1:
        return False

    return True


def parse_vals(vals):
    res = []
    for val in vals:
        val = val.strip()
        if '(' in val and ')' in val:
            val = val[:val.find('(')] + val[val.find(')') + 1:]
        if not is_num(val):
            res.append(val)
        else:
            n = eval(val)
            res.append(n)
    return res


def parse_brace_vals(vals):
    res = []
    for val in vals:
        val = val.strip()
        if '(' in val and ')' in val:
            val = val[val.find('(') + 1: val.find(')')]
        if not is_num(val):
            res.append(val)
        else:
            n = eval(val)
            res.append(n)
    return res


def generate_week_times(start_date, end_date):
    start_time = getDaySecond(getTimeSec(start_date)) + 8 * 3600
    end_time = getDaySecond(getTimeSec(end_date)) + 8 * 3600
    if start_time != getMaintenceSec(start_time):
        log_force('generate_week_times warning: start_date', start_date, 'is not maintence date')
    start_times = []
    end_times = []
    if end_time > getNow():
        end_time -= 24 * 3600
    cur_time = start_time
    while cur_time < end_time:
        nex_time = cur_time + 7 * 24 * 3600
        nex_time = min(nex_time, end_time)
        start_times.append(getTimeDes(cur_time))
        end_times.append(getTimeDes(nex_time))
        log_force('generate_week_times start_time', getTimeDes(cur_time), 'end_time', getTimeDes(nex_time))
        cur_time = nex_time
    return start_times, end_times
