import argparse
import sys


parser = argparse.ArgumentParser()
parser.add_argument('--first_coord', help='first coord of line', nargs='+', type=int)
parser.add_argument('--second_coord', help='second coord of line', nargs='+', type=int)
args = parser.parse_args()

if args.first_coord:
    print('first_coord =', args.first_coord)
    print('first_coord =', type(int(args.first_coord[0])), args.first_coord[1])
    first_coord = args.first_coord
if args.second_coord:
    print('second_coord =', args.second_coord)
    print('second_coord =', args.second_coord[0], args.second_coord[1])
    second_coord = args.second_coord


slope = sys.maxsize if first_coord[0]-second_coord[0] == 0 else (first_coord[1]-second_coord[1])/(first_coord[0]-second_coord[0])
print('slope =', slope)
