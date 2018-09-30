# -*- coding: utf-8 -*-
from ctypes import *
import os

libc = cdll.LoadLibrary("libc.so.6")

# namespace flag
CLONE_NEWNS = 0x00020000  # /* New mount namespace group */
CLONE_NEWUTS = 0x04000000  # /* New utsname namespace */
CLONE_NEWIPC = 0x08000000  # /* New ipc namespace */
CLONE_NEWUSER = 0x10000000  # /* New user namespace */
CLONE_NEWPID = 0x20000000  # /* New pid namespace */
CLONE_NEWNET = 0x40000000  # /* New network namespace */


def clone(func, stack, flags):
    result = libc.clone(func, stack, flags)
    if result < 0:
        err = get_errno()
        raise OSError(err, os.strerror(err))
    return result


def sethostname(hostname):
    result = libc.sethostname(hostname, len(hostname))
    if result < 0:
        err = get_errno()
        raise OSError(err, os.strerror(err))
    return  result

