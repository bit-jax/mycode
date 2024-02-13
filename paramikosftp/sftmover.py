#!/usr/bin/env python3


import paramiko

import os

def main():
    t = paramiko.Transport("10.10.2.3", 22)

    t.connect(username="bender", password="alta3")

    sftp = paramiko.SFTPClient.from_transport(t)

    for x in os.listdir("/home/student/filestocopy/"):
        if not os.path.isdir("/home/studetn/filestocopy/"+x):
            sftp.put("/home/student/filestocopy/"+x, "/tmp/"+x)

    sftp.close()
    t.close()

    if __name__ == "__name__":
        main()
