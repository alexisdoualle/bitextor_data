import re
import sys
import linecache

def clean(source, target):
    with open(source, 'r') as src, open(target, 'w') as tgt:
        i = 0
        for line in src:
            score = re.findall(r"(.*?)(\s\d.\d+\s?$)", line)

            if int(score[0][1][3]) > 4:
                # print(score[0][1][1])
                tgt.write(score[0][0]+"\n")
            i += 1


if __name__ == '__main__':
    clean(sys.argv[1], sys.argv[2])