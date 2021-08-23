import sys
import os


def classify_log(file_name):
    f = open(file_name, 'r')
    directory = 'classified_logs'
    lines = f.readlines()
    try:
        if not os.path.exists(directory):
            os.makedirs(directory)
    except OSError:
        print('Error : Creating Directory ' + directory)

    for line in lines:
        pidLocationStart, pidLocationEnd = line.find('[')+1, line.find(']')
        if pidLocationStart == -1 or pidLocationEnd == -1:
            continue
        pid = line[pidLocationStart:pidLocationEnd]
        newFileName = directory + "/" + pid + ".log"
        newFile = open(newFileName, 'a')
        newFile.write(pid + ':')
        newFile.write(line[pidLocationEnd + 2:] + '\n')
        newFile.close()


def classify_log_test(istr):
    pidLocationStart, pidLocationEnd = istr.find('[')+1, istr.find(']')
    pid = istr[pidLocationStart:pidLocationEnd]
    print(pid, ':', end='')
    print(istr[pidLocationEnd+2:])


def main():
    file_name = sys.argv[1]
    if not file_name:
        print("please input guacd file name")
        sys.exit()
    else:
        classify_log(file_name)


if __name__ == "__main__":
    main()
