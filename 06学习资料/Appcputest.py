#!/user/bin/python
import csv
import os
import time

class Controller(object):
    def __init__(self):
        self.alldata = [(id,vss,rss)]

    def analyzedata(self):
        content = self.readfile()
        i = 0
        for line in content:
            if "com.android.brower" in line:
                print line
                line = "#".join(line.split())
                vss = line.split("#")[5].strip("K")
                rss = line.split("#")[6].strip("K")

                self.alldata.append((i,vss,rss))
                i = i+1

                
    def SavaDataToCSV(self):
        csvfile = file('meminfo.csv','wb')
        writer = csv.writer(csvfile)
        writer.writerows(self.alldata)

    def readfile(self):
        mfile = file("meminfo","r")
        content = mfile.readlines()
        mfile.close()
        return content
        

if __name__ == "__main__":
    controller = Controller()
    controller.analyzedata()
    controller.SavaDataToCSV()
