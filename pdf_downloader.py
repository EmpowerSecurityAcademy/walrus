import urllib2

def main():
    download_file("http://anh.cs.luc.edu/python/hands-on/3.1/Hands-onPythonTutorial.pdf")

def download_file(download_url):
    response = urllib2.urlopen(download_url)
    file = open("./tmp/document.pdf", 'w')
    file.write(response.read())
    file.close()
    print("Completed")

if __name__ == "__main__":
    main()