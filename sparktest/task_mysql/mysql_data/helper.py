# -*- coding:utf-8 -*-
#!/usr/bin/python2
import sys
import os
import signal
import time
need_exit = False

program_path = os.path.split(os.path.realpath(__file__))[0]
print( 'program_path',program_path)


if '/' in program_path:
	parent_path = program_path[:program_path.rfind('/')]
elif '\\' in program_path:
	parent_path = program_path[:program_path.rfind('\\')]
print( 'parent_path', parent_path )
if os.path.isdir(parent_path):
	sys.path.append(parent_path)

grandparent_path = None
if os.path.isdir(program_path + '/common'):
	common_path = program_path + '/common'
elif '/' in program_path:
	common_path = program_path[:program_path.rfind('/')] + '/common'
	if not os.path.isdir(common_path):
		grandparent_path = parent_path[:parent_path.rfind('/')]
		common_path = parent_path[:parent_path.rfind('/')] + '/common'
elif '\\' in program_path:
	common_path = program_path[:program_path.rfind('\\')] + '\\common'
	if not os.path.isdir(common_path):
		grandparent_path = parent_path[:parent_path.rfind('\\')]
		common_path = parent_path[:parent_path.rfind('\\')] + '\\common'
print( 'common_path', common_path)
if os.path.isdir(common_path):
	sys.path.append(common_path)
else:
	print( 'error helper: common_path do not exist', common_path)
	exit()
if grandparent_path:
	sys.path.append(grandparent_path)

import utils
import storage
def update_conf_file_name(conf_file_name):
	params = sys.argv[1:]
	for param in params:
		key,val = param.split('=')
		if key == 'conf_file_name':
			conf_file_name = val
			break
	return conf_file_name

def load_settings(conf_file_name = 'settings.conf'):
	import settings
	settings.conf_file_name = update_conf_file_name(conf_file_name)

	utils.log_force('program_path', program_path)
	if '\\' in program_path:
		storage.load_conf('%s\\%s'%(program_path, settings.conf_file_name), settings)
	else:
		storage.load_conf('%s/%s' % (program_path, settings.conf_file_name), settings)
	utils.log_force('sys.argv', sys.argv)
	params = sys.argv[1:]
	settings.param_line = ';'.join(params)

	override_settings(params)

def override_settings(params):
	import settings
	for param in params:
		res = param.split('=')
		assert len(res) == 2, ('invalid override param, split', param)
		key,val = res
		key = key.strip()
		val = val.strip()
		assert ' ' not in key, ('invalid override param, key', param)
		assert ' ' not in val, ('invalid override param, val', param)
		try:
			val = eval(val)
		except:
			val = val
		setattr(settings, key , val)
		utils.log_force('settings.%s=%s'%(key, val))

def on_terminate(signum = 0, e = 0):
	global need_exit
	utils.log_force('helper.on_terminate: receive signal')
	need_exit = 1

def sleep(sec):
	if sec < 1:
		time.sleep(sec)
		return
	count = int(sec)
	for i in range(count):
		time.sleep(1)
		if need_exit:
			return
	time.sleep(sec - count)

def check_path(path, need_create = True):
	if os.path.isdir(path):
		return True
	elif os.path.isfile(path):
		utils.log_force('check_path fail: path', path, 'is file')
		return False
	elif need_create:
		os.mkdir(path)
		if os.path.isdir(settings.output_path):
			utils.log_force('check_path succ: create path', path)
			return True
		else:
			utils.log_force('check_path fail: can not create path', path)
			return False
	else:
		utils.log_force('check_path fail: path', path, 'not exist')
		return False

signal.signal(signal.SIGINT, on_terminate)
