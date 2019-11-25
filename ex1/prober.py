import requests
import time
import sys
nl='\n'
repeat=30

def main(argv):
    if len(argv)<2 or len(argv)>3:
        print("Enter command line <url> <sample_file>")
        sys.exit(-1)
    url=sys.argv[1]+":80"
    if len(argv)==3:

        filePath=sys.argv[2]
    else: #assume url given but sample_file_name not given
        filePath="samples.txt"

    currTimer=time.time()
    start=int(currTimer)
    #try get initial response and write url to samples file
    try:
        response=requests.get(url,allow_redirects=False,timeout=30)
        print(response.status_code)
        with open(filePath,"w+") as file:
            file.write("URL="+url[7:-3]+nl)
            file.write(str(start)+','+str(response.status_code)+nl)

    except:
        print(-1)
        with open(filePath,"w+") as file:
            file.write("URL="+url[7:-3]+nl)
            file.write(str(start)+','+str(-1)+nl)


    #loop every 30 seconds
    while True:


        if time.time()-currTimer>repeat:
            try:
                print(start)
                start+=repeat
                currTimer=time.time()
                response=requests.get(url,allow_redirects=False,timeout=30)
                print(response.status_code)
                with open(filePath,"a+") as file:
                    file.write(str(start)+','+str(response.status_code)+nl)
            except:
                print(-1)
                with open(filePath,"a+") as file:
                    file.write(str(start)+','+str(-1)+nl)



main(sys.argv)
