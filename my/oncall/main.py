#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# main.py - main

# Date   : 2020/12/11
import logging
import time
import os
import sys
import getopt
import json
import oncall

VERSION = '0.0.1'

def init_logging(basedir, debug):
    logger = logging.getLogger('abc')
    logger.setLevel(logging.DEBUG)

    logfile = os.path.join(basedir, "oncall.log")

    if debug:
        formatter = logging.Formatter('[%(asctime)s] - %(filename)s[line:%(lineno)d] - %(levelname)s: %(message)s')
    else:
        formatter = logging.Formatter('[%(asctime)s] %(levelname)5s - %(message)s')

    fh = logging.FileHandler(logfile)
    fh.setFormatter(formatter)
    fh.setLevel(logging.DEBUG)
    logger.addHandler(fh)

    if debug:
        sh = logging.StreamHandler()
        sh.setFormatter(formatter)
        sh.setLevel(logging.DEBUG)
        logger.addHandler(sh)

    return logger

def get_path():
    tm = time.localtime()
    basedir = os.path.join(os.getcwd(), '{:04d}_{:02d}_{:02d}_{:02d}_{:02d}_{:02d}'.format(
        tm.tm_year, tm.tm_mon, tm.tm_mday, tm.tm_hour, tm.tm_min,
        tm.tm_sec
    ))
    if not os.path.exists(basedir):
        os.mkdir(basedir)
    return basedir

def main():
    try:
        opts, _ = getopt.getopt(sys.argv[1:],'vdh', ['version', 'debug', 'help'])
    except Exception as e:
        print(e)
        sys.exit(1)

    debug = False
    for opt, val in opts:
        if opt in ('-v', '--version'):
            print('version: {}'.format(VERSION))
            sys.exit(0)
        elif opt in ('-d', '--debug'):
            debug = True
        else:
            print('{} [-v | --version] [-d | --debug] [-h | --help]'.format(sys.argv[0]))
            sys.exit(0)

    basedir = get_path()
    logger = init_logging(basedir, debug);
    try:
        logger.info('{} start'.format(sys.argv[0]))
        oncall.run(basedir, debug)
        logger.info("{} done".format(sys.argv[0]))
    except Exception as e:
        logger.error(e)
        logger.info("{} failed".format(sys.argv[0]))
        raise(e)

# TODO: split OnCall class
# TODO: add config.json
if __name__ == '__main__':
    main()
