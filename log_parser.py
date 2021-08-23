import sys
import os
import subprocess
import select
import time


def classify_log(file_name):
    directory = 'classified_logs'
    # f = open(file_name, 'r')
    # lines = f.readlines()
    try:
        if not os.path.exists(directory):
            os.makedirs(directory)
    except OSError:
        print('Error : Creating Directory ' + directory)

    # for line in lines:
    #     pidLocationStart, pidLocationEnd = line.find('[')+1, line.find(']')
    #     if pidLocationStart == -1 or pidLocationEnd == -1:
    #         continue
    #     pid = line[pidLocationStart:pidLocationEnd]
    #     dateInfo = list(line[:6])
    #     if dateInfo[4] == ' ':
    #         dateInfo[4] = '0'
    #     dateInfo[3] = '-'
    #     dateInfo = "".join(dateInfo)
    #     newFileName = directory + "/" + pid + "-" + dateInfo + ".log"
    #     newFile = open(newFileName, 'a')
    #     newFile.write(pid + ':')
    #     newFile.write(line[pidLocationEnd + 2:] + '\n')
    #     newFile.close()

    tf = subprocess.Popen(['tail', '-F', file_name],
                          stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    tp = select.poll()
    tp.register(tf.stdout)
    while True:
        if tp.poll(1):
            line = tf.stdout.readline().decode()
            if not line:
                break
            pidLocationStart, pidLocationEnd = line.find('[')+1, line.find(']')
            if pidLocationStart == -1 or pidLocationEnd == -1:
                continue
            pid = line[pidLocationStart:pidLocationEnd]
            dateInfo = list(line[:6])
            if dateInfo[4] == ' ':
                dateInfo[4] = '0'
            dateInfo[3] = '-'
            dateInfo = "".join(dateInfo)
            timeInfo = line[7:15]
            newFileName = directory + "/" + pid + "-" + dateInfo + ".log"
            newFile = open(newFileName, 'a')
            newFile.write(timeInfo + ' ' + pid + ':')
            newFile.write(line[pidLocationEnd + 2:] + '\n')
            newFile.close()
        time.sleep(0.001)


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
    # classify_log('guacd.log')
    main()
