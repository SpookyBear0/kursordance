import argparse
from kursordance.game import init

parser = argparse.ArgumentParser(description="Cursordancing bot in python")

parser.add_argument("-map", "-m", metavar="map", type=str, nargs=1)
parser.add_argument("-difficulty", "-d", metavar="difficulty", type=str, nargs=1)
parser.add_argument("--mirror", metavar="mirror", type=bool, nargs="?", const=True, default=False)
parser.add_argument("--download", "--dl", metavar="download", type=bool, nargs="?", const=True, default=False)

args = parser.parse_args()

if __name__ == "__main__":
    init(args.map, args.difficulty, args.mirror, args.download)