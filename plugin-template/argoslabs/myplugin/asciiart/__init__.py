#!/usr/bin/env python
# coding=utf8
"""
====================================
 :mod:`argoslabs.myplugin.asciiart`
====================================
.. moduleauthor:: Jerry Chae <mcchae@argos-labs.com>
.. note:: ARGOS-LABS License

Description
===========
ARGOS LABS plugin module sample
"""
# Authors
# ===========
#
# * Jerry Chae
#
# Change Log
# --------
#
#  * [2019/03/08]
#     - add icon
#  * [2018/11/28]
#     - starting

################################################################################
import os
import sys
from _ast import BinOp

from alabs.common.util.vvargs import ModuleContext, func_log, \
    ArgsError, ArgsExit, get_icon_path


################################################################################
@func_log
def do_binop(mcxt, argspec):
    mcxt.logger.info('>>>starting...')
    try:
        bo = BinOp(argspec, logger=mcxt.logger)
        r = 0  # 0 means success
        return r
    except Exception as e:
        msg = 'argoslabs.filesystem.op Error: %s' % str(e)
        mcxt.logger.error(msg)
        sys.stderr.write('%s%s' % (msg, os.linesep))
        raise
    finally:
        mcxt.logger.info('>>>end...')


################################################################################
def _main(*args):
    """
    Build user argument and options and call plugin job function
    :param args: user arguments
    :return: return value from plugin job function
    """
    with ModuleContext(
        owner='MyCompany',
        group='api',
        version='1.0',
        platform=['windows', 'darwin', 'linux'],
        output_type='text',
        display_name='CRM Op',
        icon_path=get_icon_path(__file__),
        description='Our Company CRM API',
    ) as mcxt:
        # ######################################## for app dependent options
        mcxt.add_argument('--type', '-t',
                          display_name='Value Type', show_default=True,
                          choices=["auto", "string", "int", "float", "date", "datetime"],
                          default='auto',
                          help='Set Value type, one of {"auto", "int", "float", "date", "datetime"}.'
                               ' Default is auto which means try to guess the best type of value')
        mcxt.add_argument('--date-format',
                          display_name='Date Format',
                          choices=list(BinOp.DATE_FORMAT.keys()),
                          default='YYYYMMDD',
                          help='Set the format of Date')
        mcxt.add_argument('--datetime-format',
                          display_name='DateTime Format',
                          choices=list(BinOp.DATETIME_FORMAT.keys()),
                          default='YYYYMMDD-HHMMSS',
                          help='Set the format of DateTime')

        # ##################################### for app dependent parameters
        mcxt.add_argument('left',
                          display_name='Left Val',
                          help='Left operand for binary operation')
        mcxt.add_argument('operation',
                          display_name='Operator',
                          choices=['+', '-', '*', '/', '%'],
                          help='Binary operation, one of "+(add),-(subtract),*(multiply),/(divide),%%(modular)"')
        mcxt.add_argument('right',
                          display_name='Right Val',
                          help='Right operand for binary operation')
        argspec = mcxt.parse_args(args)
        return do_binop(mcxt, argspec)


################################################################################
def main(*args):
    try:
        return _main(*args)
    except ArgsError as err:
        sys.stderr.write('Error: %s\nPlease -h to print help\n' % str(err))
    except ArgsExit as _:
        pass
