# coding=utf-8
import inspect
import traceback
import sys


def get_exception_info():
    '''
    获取stacktrace
    '''
    exc_type, exc_value, exc_traceback = sys.exc_info()
    exc = traceback.format_exception(exc_type, exc_value, exc_traceback)
    info = {'exception': '%s' % exc}
    return info


def build_func_args_item(stack_info):
    '''
    创建单调函数调用记录
    '''
    func_name = stack_info[3]
    args_info = inspect.getargvalues(stack_info[0])
    frame = stack_info[0]
    item = {'function': func_name,
            'object': '%s' % frame.f_locals.get('self'),
            'arguments': inspect.formatargvalues(args_info.args, args_info.varargs, args_info.keywords, args_info.locals)}
    return item


def get_func_args():
    '''
    获取外层函数调用参数，注意调用栈顺序，最多取最后3层调用
    '''
    stacks = inspect.stack()[:3]
    result = []
    for stack in stacks:
        item = build_func_args_item(stack)
        result.append(item)
    return result


def pdb_pm():
    # 使用 pdb 进入异常现场。
    from sys import exc_info
    from traceback import print_exc
    try:
        from ipdb import post_mortem
    except:
        from pdb import post_mortem
    _, _, tb = exc_info()
    print_exc()
    post_mortem(tb)