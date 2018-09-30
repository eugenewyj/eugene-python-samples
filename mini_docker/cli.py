# -*- coding: utf-8 -*-
import os
from ctypes import *

from mini_docker import libc
from signal import SIGCHLD

STACK_SIZE = 1024


def child_func():
    print("child pid=%d ppid=%d" % (os.getpid(), os.getppid()))
    libc.sethostname("mytest")
    os.system("hostname")
    return 0


def main():
    child = CFUNCTYPE(c_int)(child_func)
    child_stack = create_string_buffer(STACK_SIZE)
    child_stack_pointer = c_void_p(cast(child_stack, c_void_p).value + STACK_SIZE)
    flags = libc.CLONE_NEWUTS
    pid = libc.clone(child,  child_stack_pointer, flags | SIGCHLD)
    print("parent pid=%d ppid=%d child_pid=%d" % (os.getpid(), os.getppid(), pid))
    os.waitpid(pid, 0)


if __name__ == "__main__":
    main()