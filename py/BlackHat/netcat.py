#!/usr/bin/python
#coding: utf-8

import sys
import socket
import getopt
import threading
import subprocess

# 定义常量
listen = False
command = False
upload = False
execute = ""
target = ""
upload_destination = ""
port = 0

def usage():
    print "Netcat Net Tool"
    print
    print "Usage: netcat.py -t target_host -p port"
    print "-l --listen  - listen on [host]:[port] for incoming connections"
    print "-e --execute=file_to_run - execute the given file upon receiving a connection"
    print "-c --command  - initialize a command shell"
    print "-u --upload=destination  - upon receiving connection uplaod a file and write to [destination]"
    print
    print
    print "Examples："
    print "netcat.py -t 192.168.0.1 -p 5555 -l -c"
    print "netcat.py -t 192.168.0.1 -p 5555 -l -u=c:\\target.exe"
    print "netcat.py -t 192.168.0.1 -p 5555 -l -e=\"cat /etc/passwd\""
    print "echo 'ABCDEFGHI' | ./netcat.py -t 192.168.11.12 -p 135"
    sys.exit(0)

def client_sender(buffer):
    pass

def server_loop():
    pass

def client_handler(client_socket):
    pass

def main():
    global listen
    global port
    global execute
    global command
    global upload_destination
    global target

    if not len(sys.argv[1:]):
        usage()

    # 读取命令行选项
    try:
        opts, args = getopt.getopt(sys.argv[1:], "hle:t:p:cu:", ["help", "listen", "execute", "target", "port", "command", "upload"])
    except getopt.GetoptError as err:
        print str(err)
        usage()

    for o,a in opts:
        if o in ("-h", "--help"):
            usage()
        elif o in ("-l", "--listen"):
            listen = True
        elif o in ("-e", "--execute"):
            execute = a
        elif o in ("-c", "--commandshell"):
            command = True
        elif o in ("-u", "--upload"):
            upload_destination = a
        elif o in ("-t", "--target"):
            target = a
        else:
            assert False, "Unhandled Option"

    # 监听 or 标准输入数据
    if not listen and len(target) and port > 0:
        buffer = sys.stdin.read()
        client_sender(buffer)

    if listen:
        server_loop()

if __name__ == "__main__":
    main()