#-*- coding: GB18030 -*-
import json
import os
import utils
encoding = 'gbk'

def read_json_file(file_name):
	in_file = open(file_name, 'r')
	lines = in_file.readlines()
	res = []
	for line in lines:
		line = line.strip()
		if line.startswith('//'):
			continue
		res.append(line)
	in_file.close()
	data_str = '\n'.join(res)
	return data_str

def load_data(file_name):
	if not os.path.isfile(file_name):
		return {}
	data_str = read_json_file(file_name)
	return json.loads(data_str, encoding = encoding, object_hook=_decode_dict)

def save_data(file_name, data):
	dump_data(file_name, data)
def dump_data(file_name, data):
	out_file = open(file_name, 'w').readlines()
	data_str = json.dumps(data, encoding= encoding, sort_keys = True, indent = 4 )
	out_file.write(data_str)
	out_file.close()


# def _decode_list(data):
# 	rv = []
# 	for item in data:
# 		if isinstance(item, unicode):
# 			item = item.encode(encoding)
# 		elif isinstance(item, list):
# 			item = _decode_list(item)
# 		elif isinstance(item, dict):
# 			item = _decode_dict(item)
# 		rv.append(item)
# 	return rv

# def _decode_dict(data):
# 	rv = {}
# 	for key, value in data.iteritems():
# 		if isinstance(key, unicode):
# 			key = key.encode(encoding)
# 		if isinstance(value, unicode):
# 			value = value.encode(encoding)
# 		elif isinstance(value, list):
# 			value = _decode_list(value)
# 		elif isinstance(value, dict):
# 			value = _decode_dict(value)
# 		rv[key] = value
# 	return rv

def get_all_keys(data):
	all_keys = set()
	if isinstance(data, dict):
		for log in data.itervalues():
			if not isinstance(log, dict):
				continue
			for k in log:
				all_keys.add(k)
	else:
		for log in data:
			if not isinstance(log, dict):
				continue
			for k in log:
				all_keys.add(k)
	all_keys = list(all_keys)
	all_keys.sort()
	return all_keys

def load_conf(filename, mod):
	settings = mod
	in_file = open(filename, 'r')
	lines = in_file.readlines()
	for line in lines:
		line = line.strip()
		if line.startswith('#'):
			continue
		if line == '':
			continue
		if '=' not in line:
			raise RuntimeError('load_conf error: line %s illegal conf format in %s'%(line, filename))
		try:
			key, val = line.split('=')
			key = key.strip().split(' ')[0]
			if "'" in val:
				val = eval(val)
			else:
				val = eval(val.strip().split(' ')[0])
			setattr(mod, key , val)
		except Exception as e:
			raise RuntimeError('load_conf error [%s]: illegal conf format in %s %s'%(line, filename, e))
	in_file.close()
