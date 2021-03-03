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

parser = argparse.ArgumentParser(
    prog='PROG',
    formatter_class=argparse.MetavarTypeHelpFormatter)
parser.add_argument('--foo', type=int)
parser.add_argument('bar', type=float)
parser.print_help()