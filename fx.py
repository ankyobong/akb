import argparse
import textwrap

""" # 정수 배열을 받아 합계 또는 최대값을 출력하는 프로그램
parser = argparse.ArgumentParser(description='Process some integers.')
parser.add_argument('integers', metavar='N', type=int, nargs='+',
                    help='an integer for the accumulator')
parser.add_argument('--sum', dest='accumulate', action='store_const',
                    const=sum, default=max,
                    help='sum the integers (default: find the max)')
parser.add_argument('--foo', help='foo help')
args = parser.parse_args()
print(args.accumulate(args.integers))
"""
""" #prog = 프로그램이름설정
import argparse
parser = argparse.ArgumentParser()
parser.add_argument('--foo', help='foo help')
args = parser.parse_args()
"""
"""  # usage= 키워드 인자
parser = argparse.ArgumentParser(prog='PROG', usage='%(prog)s [options]')
parser.add_argument('--foo', nargs='?', help='foo help')
parser.add_argument('bar', nargs='+', help='bar help')
parser.print_help()
"""
"""  #usage 바로 아래 텍스트 프로그램기능과 작동방식 간략한 설명에 주로사용
parser = argparse.ArgumentParser(description='A foo that bars')
parser.print_help()
"""
"""  #epilog = 맨뒷줄 텍스트
parser = argparse.ArgumentParser(
    description='A foo that bars', 
    epilog="And that's how you'd foo a bar") 
parser.print_help()
"""
"""#parents
prent_parser = argparse.ArgumentParser(add_help=False)
prent_parser.add_argument('--parent', type=int)

foo_parser = argparse.ArgumentParser(parents=[prent_parser])
foo_parser.add_argument('foo')
a = foo_parser.parse_args(['--parent', '2', 'XXX'])
print(a)

bar_parser = argparse.ArgumentParser(parents=[prent_parser])
bar_parser.add_argument('--bar')
a = bar_parser.parse_args(['--bar', 'YYY'])
print(a)
"""
"""
parser = argparse.ArgumentParser(
     prog='PROG',
     description='''this description
         was indented weird
             but that is okay''',
     epilog='''
             likewise for this epilog whose whitespace will
         be cleaned up and whose words will be wrapped
         across a couple lines''')
parser.print_help()
"""
""" #RawDescriptionHelpFormatter = 원하는 대로 텍스트의 줄을 조정할때 사용 맨앞에 \사용해야함
parser = argparse.ArgumentParser(
    prog='PROG',
    formatter_class=argparse.RawDescriptionHelpFormatter,
    description=textwrap.dedent('''\
    Plwease do not mess up this text!
    ---------------------------------
        I have indented it
        exactly the way
        I want it
    '''))
parser.print_help()
"""
""" #ArgumentDefaultsHelpFormatter 각인자의 도움말 메시지를 자동으로 추가
parser = argparse.ArgumentParser(
    prog='PROG',
    formatter_class=argparse.ArgumentDefaultsHelpFormatter)
parser.add_argument('--foo', type=int, default=42, help='FOO!')
parser.add_argument('bar', nargs='*', default=[1, 2, 3], help='BAR!')
parser.print_help()
"""
"""
parser = argparse.ArgumentParser(
    prog='PROG',
    formatter_class=argparse.MetavarTypeHelpFormatter)
parser.add_argument('--foo', type=int)
parser.add_argument('bar', type=float)
parser.print_help()
"""
"""
parser = argparse.ArgumentParser(prog='PROG', prefix_chars='-+')
parser.add_argument('+f')
parser.add_argument('++bar')
a = parser.parse_args('+f X ++bar Y'.split())
print(a)
"""
"""
with open('args.txt', 'w') as fp:
       fp.write('-f\nbar')
parser = argparse.ArgumentParser(fromfile_prefix_chars='@')
parser.add_argument('-f')
a = parser.parse_args(['-f', 'foo', '@args.txt'])
print(a)
"""
"""
parser = argparse.ArgumentParser(argument_default=argparse.SUPPRESS)
parser.add_argument('--foo')
parser.add_argument('bar', nargs='?')
a=parser.parse_args(['--foo', '1', 'BAR'])
print(a)
a=parser.parse_args([])
print(a)
"""
"""# conflict_handler='resolve' 를 사용하면 같은 옵션의 문자열 사용가능
parser = argparse.ArgumentParser(prog='PROG', conflict_handler='resolve')
parser.add_argument('-f', '--foo', help='old foo help')
parser.add_argument('--foo', help='new foo help')
parser.print_help()
"""
""" #도움말 
parser = argparse.ArgumentParser()
parser.add_argument('--foo', help='foo help')
args = parser.parse_args()
"""
# add_argument()
# action
parser = argparse.ArgumentParser()
"""#action-store
parser.add_argument('--foo')
a = parser.parse_args('--foo 1'.split())
print(a)
#action-store_const
parser.add_argument('--g', action='store_const', const=42)
b = parser.parse_args(['--g', '--foo', '1'])
print(b)
"""
"""#action-store_true/false
parser.add_argument('--foo', action='store_true')
parser.add_argument('--bar', action='store_false')
parser.add_argument('--baz', action='store_false')
a=parser.parse_args('--foo --bar'.split())
print(a)
"""
"""
#action-append 리스트에 저장 /추가
parser = argparse.ArgumentParser()
parser.add_argument('--foo', action='append')
a=parser.parse_args('--foo 1 --foo 2'.split())
print(a)
"""
"""
#action-append_const 리스트에 저장하고 키워드인자로 지정된 값을 리스트에 추가
parser = argparse.ArgumentParser()
parser.add_argument('--str', dest='types', action='append_const', const=str)
parser.add_argument('--int', dest='types', action='append_const', const=int)
a = parser.parse_args('--str --int'.split())
print(a)
"""
#action-count 키워드 인자가 등장한 횟수를 계산
#help  파서의 모든 옵션에 대한 도움말 메시지
"""#version 버전정보를 출력함
parser = argparse.ArgumentParser(prog='PROG')
parser.add_argument('--version', action='version', version='%(prog)s 2.0')
a=parser.parse_args(['--version'])
print(a)
"""
class FooAction(argparse.Action):
       def __init__(self, option_strings, dest, nargs=None, **kwargs):
              if nargs is not None:
                     raise ValueError("nargs not allowed")
              super(FooAction, self).__init__(option_strings, dest, **kwargs)
       def __call__(self, parser, namespace, values, option_string=None):
              print('%r %r %r' % (namespace, values, option_string))
              setattr(namespace, self.dest, values)

parser = argparse.ArgumentParser()
parser.add_argument('--foo', action= FooAction)
parser.add_argument('bar', action=FooAction)
args = parser.parse_args('1 --foo 2'.split())
print(args)