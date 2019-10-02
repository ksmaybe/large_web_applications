import requests
import timeit
import sys


def main():
    # url=sys.argv[1]+":80"
    # filePath=sys.argv[2]
    url="http://nyus.edu:80"
    try:
        response=requests.get(url)
        print(response.status_code)
    except:
        print(-1)



    # while True:
    #     start=timeit.timeit()
    #
    #     if start>30:
    #
    #         start=timeit.timeit()
    #         pass

    pass


main()
