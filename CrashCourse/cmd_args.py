from argparse import ArgumentParser

parser=ArgumentParser()

parser.add_argument('--output',required=True, help="dest file of this program")
parser.add_argument('--text',required=True, help="text of this program")

args=parser.parse_args()
print(args.output)
