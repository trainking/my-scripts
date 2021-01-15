#!/usr/bin/python3

# dos2unix 将Windows下的CRLF更换为LF

import os
import sys
import threading
import queue
import time
from rich.console import Console

# Rich Console
console = Console()

MAX_THREADS = 4

workQueue = queue.Queue() # 数据队列
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
            if not self.q.empty():
                filename = self.q.get()
                if os.path.isdir(filename):
                    _list_f = os.listdir(filename)
                    for i in _list_f:
                        self.q.put(filename + os.path.sep + i)
                queueLock.release()
                if os.path.isfile(filename):
                    console.print("%d:%s -- run -- %s" % (self.threadID, self.name, filename))
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
    args = []
    script_name = os.path.basename(__file__)
    if len(sys.argv) > 0 and script_name in sys.argv[0]:
        args = sys.argv[1:]

    if len(args) == 0:
        console.print("")
        console.print("====This's a CRLF to LF Script====", style="bold red")
        console.print("")
        console.print("Author: trainking.github.com")
        console.print("Usage:")
        console.print(":point_right:"," - dos2uinx.py [bold magenta]a.txt [bold magenta]b.txt [bold magenta]c.txt")
        console.print(":point_right:", " - dos2uinx.py ./sr/ ...")
        console.print("")
        console.print("may the force be with you!", ":bride_with_veil:")
        console.print("")
        return

    console.print("Start...")
    
    queueLock.acquire()
    for x in args:
        workQueue.put(x)
    queueLock.release()

    for i in range(0, MAX_THREADS):
        thread = SimpleThread(i, "thread-"+str(i), workQueue)
        thread.start()
        threads.append(thread)

    # 保证每个队列不是空开始
    while not workQueue.empty():
        pass

    for t in threads:
        t.join()
    console.print("End!")

if __name__ == "__main__":
    main()