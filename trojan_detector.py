import tldextract  # can be downloaded from pip
import ssl
import socket
import sys


def verify_file(filename):
    # more extensions can be added as necessary
    # this is a simple demo, in practice all possible extensions should be on this list
    # source for extensions: fileinfo.com
    txt_extensions = [".txt", ".dat", ".csv", ".doc", ".pdf"]
    image_extensions = [".jpg", ".jpeg", ".png", ".gif", ".heic"]
    exec_extensions = [".sk", ".run", ".exe", ".bin", ".app"]
    zip_extensions = [".bz", ".zip", ".mint", ".tbz", ".pkg.tar.xz", ".7z"]
    for ext in txt_extensions:
        if filename.endswith(ext):
            return "text file, low risk"
    for ext in image_extensions:
        if filename.endswith(ext):
            return "image file, low risk"
    for ext in exec_extensions:
        if filename.endswith(ext):
            return "exec file, high risk.\nDO NOT DOWNLOAD THIS FILE AND CLICK ON IT IF YOU DON'T KNOW ITS CONTENTS"
    for ext in zip_extensions:
        if filename.endswith(ext):
            return "zipped file, high risk.\nDO NOT DOWNLOAD THIS FILE AND UNZIP IT IF YOU DON'T KNOW ITS CONTENTS"
    return "unknown file format, medium risk"


# taken from https://stackoverflow.com/questions/30862099/how-can-i-get-certificate-issuer-information-in-python
def verify_url(url):
    ext = tldextract.extract(url)
    # more popular domains can be added
    popularDomains = ["google", "facebook", "twitter", "youtube", "reddit"]
    for domain in popularDomains:
        if(ext.domain == domain):
            return "popular verified domain, low risk"
    hostname = ext.domain + "." + ext.suffix
    ctx = ssl.create_default_context()
    try:
        with ctx.wrap_socket(socket.socket(), server_hostname=hostname) as s:
            s.connect((hostname, 443))
            cert = s.getpeercert()
            return "unpopular domain but SSL certificate valid, low risk"
    except:
        return "no SSL, medium risk"


if(sys.argv[1] == "file"):
    print(verify_file(sys.argv[2]))
elif(sys.argv[1] == "url"):
    print(verify_url(sys.argv[2]))

# print(verify_url("http://icio.us/"))
# print(verify_url("https://www.youtube.com/watch?v=tlezBUdD53w"))
# print(verify_url("https://www.sjsu.edu/admissions/graduate/index.php"))
