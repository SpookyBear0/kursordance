import argparse

parser = argparse.ArgumentParser(description="Cursordancing bot in python")

parser.add_argument("-m", "-map", metavar="map", type=str, nargs=1)
parser.add_argument("-d", "-difficulty", metavar="difficulty", type=str, nargs=1)
parser.add_argument("--mirror", metavar="mirror", type=bool, nargs="?", const=True, default=False)
parser.add_argument("--dl", "--download", metavar="download", type=bool, nargs="?", const=True, default=False)

args = parser.parse_args()

if __name__ == "__main__":
    from kursordance.game import init
    init(args.map, args.difficulty, args.mirror, args.download)