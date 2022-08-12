
import json
import logging
import os
import stat
import sys
import time
from zipfile import ZipFile
import click
from xdg import XDG_CONFIG_HOME, XDG_CACHE_HOME
import nlgeval
import nlgeval.utils
# if True:
data_path = os.getenv('NLGEVAL_DATA', os.path.join(XDG_CACHE_HOME, 'nlgeval'))
    # from nlgeval.word2vec.generate_w2v_files import generate
    #
    # with ZipFile(os.path.join(data_path, 'glove.6B.zip')) as z:
    #     z.extract('glove.6B.300d.txt', data_path)
    # generate(data_path)
    # for p in [
    #     os.path.join(data_path, 'glove.6B.zip'),
    #     os.path.join(data_path, 'glove.6B.300d.txt'),
    #     os.path.join(data_path, 'glove.6B.300d.model.txt'),
    # ]:
    #     if os.path.exists(p):
    #         os.remove(p)

path = os.path.join(nlgeval.__path__[0], 'multibleu','multi-bleu.perl')
stats = os.stat(path)
os.chmod(path, stats.st_mode | stat.S_IEXEC)

cfg_path = os.path.join(XDG_CONFIG_HOME, "nlgeval")
if not os.path.exists(cfg_path):
    os.makedirs(cfg_path)
rc = dict()
try:
    with open(os.path.join(cfg_path, "rc.json"), 'rt') as f:
        rc = json.load(f)
except:
    print("WARNING: could not read rc.json in %s, overwriting" % cfg_path)
rc['data_path'] = data_path
with open(os.path.join(cfg_path, "rc.json"), 'wt') as f:
    f.write(json.dumps(rc))