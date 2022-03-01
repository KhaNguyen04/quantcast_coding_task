import sys
import csv
from datetime import datetime

#Condition for input arguments
def main():
    if ((len(sys.argv))!=4):
        print("Incorrect number of argument!")
        sys.exit()

    if (sys.argv[2]!="-d"):
        print("-d UTC: Please enter the right timezone")
        sys.exit()

    try:
        datetime.strptime(sys.argv[3], "%Y-%m-%d")
    except ValueError:
        print("Error: Date Format: YYYY-MM-DD")
        sys.exit()

    file=sys.argv[1]
    inputZone=sys.argv[2]
    inputDate=sys.argv[3]

    def getCountCookie(countCookie):
        mostActive=[]
        if len(countCookie)!=0:
            mostFrequent=max(countCookie.values())
            for cookie, count in countCookie.items():
                if count==mostFrequent:
                    mostActive.append(cookie)
            return mostActive

    try:
        with open(file,'r') as csv_file:
            csv_reader=csv.reader(csv_file)
            next(csv_reader)
            countCookie={}
            sameTimeData=[]
            mostActiveCookie=[]
            #Getting the data with the same Time from the input
            for line in csv_reader:
                dateTime=line[1].split("T")
                if dateTime[0]==inputDate:
                    sameTimeData.append(line)
            #Count the number of cookie on the input date
            for data in sameTimeData:
                if data[0] not in countCookie:
                    countCookie[data[0]]=0
                countCookie[data[0]]+=1
            mostActiveCookie=getCountCookie(countCookie)
            for cookie in mostActiveCookie:
                print(cookie)
    except FileNotFoundError:
        print(file,": No such file or directory")

if __name__ == '__main__':
    main()