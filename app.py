import urllib.request

urls_file = open("urls.txt")
content = urls_file.readlines()
urls_file.close()
    

def check_connectivity(url):
    try:
        a = urllib.request.urlopen(url).getcode()
        print(f"{i}: Website is working.\n")

    except:
        print(f"{i}: Website is not working!\n")

for i in content:
    check_connectivity(i)

