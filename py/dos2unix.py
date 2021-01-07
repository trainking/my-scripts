#!/usr/bin/python3

# dos2unix 将Windows下的CRLF更换为LF

import os
import sys
import threading
import queue
import time

workQueue = queue.Queue(10) # 数据队列
queueLock = threading.Lock() # 锁

threads = [] # 线程集合

class SimpleThread(threading.Thread):
    '''
        简单的线程执行实例
    '''

    def __init__(self, threadID, name, q):
        threading.Thread.__init__(self)
        self.threadID = threadID
        self.name = name
        self.q = q

    def run(self):
        while True:
            queueLock.acquire()
            if not workQueue.empty():
                filename = self.q.get()
                queueLock.release()
                print ("%d:%s -- run -- %s" % (self.threadID, self.name, filename))
                dos2unix(filename)
            else:
                queueLock.release()
                break
        print("exit ", self.name)

def dos2unix(filename):
    '''
    dos2unix 执行更换换行符，filename文件路径
    '''
    temp_path = filename + ".temp" # 临时文件
    with open(filename, 'rb') as infile, open(temp_path, 'wb') as outfile:
        for line in infile:
            if line[-2:] == b'\r\n':
                line = line[:-2] + b'\n'
            outfile.write(line)
    os.remove(filename)
    os.rename(temp_path, filename)


def main():
    '''
    Usage:
        python dos2uinx.py a.txt b.txt c.txt
    '''
    args = sys.argv[1:]
    if args[0] == 'dos2unix.py':
        args = args[1:]

    print("strat!")
    
    queueLock.acquire()
    for x in args:
        workQueue.put(x)
    queueLock.release()

    for i in range(1, 3):
        thread = SimpleThread(i, "thread-"+str(i), workQueue)
        thread.start()
        threads.append(thread)

    while not workQueue.empty():
        pass

    for t in threads:
        t.join()
    print("end!")

if __name__ == "__main__":
    main()