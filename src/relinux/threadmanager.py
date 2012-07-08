'''
Thread Managing Class
@author: MiJyn
'''

from relinux import config
from relinux.modules.osweaver import isoutil, squashfs, tempsys
import time

threads = tempsys.threads
threadsdone = []
threadsrunning = []


# Finds threads that can currently run (and have not already run)
def findRunnableThreads():
    returnme = []
    for i in threads:
        if not i in threadsdone:
            deps = 0
            depsl = len(i["deps"])
            for x in i["deps"]:
                if x in threadsdone:
                    deps = deps + 1
            if deps >= depsl:
                returnme.append(i)
    return returnme


# Run a thread
def runThread(thread):
    threadsrunning.append(thread)
    thread.thread.start()


# Check if a thread is alive
def checkThread(thread):
    if thread in threadsrunning:
        if not thread.thread.isAlive():
            threadsrunning.remove(thread)


# Thread loop
def threadLoop():
    while config.ThreadStop is False:
        # Clear old threads
        for x in threadsrunning:
            checkThread(x)
        # Run runnable threads
        for x in findRunnableThreads():
            runThread(x)
        time.sleep(1 / config.ThreadRPS)