import requests
import fileinput
import urllib3
import sys

#color_codes
black   = "\033[0;30m"
red     = "\033[0;31m"
green   = "\033[0;32m"
yellow  = "\033[0;33m"
blue    = "\033[0;34m"
white   = "\033[0;37m"
nocolor = "\033[0m"

def banner():
    print(f"""
  ____        _             ___      _ _____ 
 / ___| _   _| |__     ___ / _ \  __| |___ / 
 \___ \| | | | '_ \   / __| | | |/ _` | |_ \ 
  ___) | |_| | |_) | | (__| |_| | (_| |___) |
 |____/ \__,_|_.__/   \___|\___/ \__,_|____/ 

                                - vignesh-user
          
{yellow}[Please be patient; it takes some time to generate the output]{nocolor}
""")

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

def main(filename):
    try:
        lines=[]
        with open(filename, 'r') as file:
            lines = file.readlines()
        banner()
        for url in lines:
            url = url.strip()
            # print(url)
            if url.startswith("https://"):
                try:
                    https = (url)
                    # print(https)
                    req=requests.get(https,verify=False)
                    s_code(req,url)
                except requests.exceptions.ConnectionError:
                    print(f"Connection error for {url}: Skipping to the next URL")
                except requests.exceptions.ReadTimeout:
                    print(f"Read timeout for {url}: Skipping to the next URL")
                except requests.exceptions.RequestException:
                    print(f"Request exception for {url}: Skipping to the next URL")
            elif url.startswith("http://"):
                try:
                    http = (url)
                    # print(http)
                    req=requests.get(http,verify=False)
                    s_code(req,url)
                except requests.exceptions.ConnectionError:
                    print(f"Connection error for {url}: Skipping to the next URL")
                except requests.exceptions.ReadTimeout:
                    print(f"Read timeout for {url}: Skipping to the next URL")
                except requests.exceptions.RequestException:
                    print(f"Request exception for {url}: Skipping to the next URL")

            elif not url.startswith("https://"):
                try:
                    https = (f"https://{url}")
                    # print(https)
                    req=requests.get(https,verify=False)
                    s_code(req,url)
                except requests.exceptions.ConnectionError:
                    print(f"Connection error for {url}: Skipping to the next URL")
                except requests.exceptions.ReadTimeout:
                    print(f"Read timeout for {url}: Skipping to the next URL")
                except requests.exceptions.RequestException:
                    print(f"Request exception for {url}: Skipping to the next URL")
            elif not url.startswith("http://"):
                try:
                    http = (f"http://{url}")
                    # print(http)
                    req=requests.get(http,verify=False)
                    s_code(req,url)
                except requests.exceptions.ConnectionError:
                    print(f"Connection error for {url}: Skipping to the next URL")
                except requests.exceptions.ReadTimeout:
                    print(f"Read timeout for {url}: Skipping to the next URL")
                except requests.exceptions.RequestException:
                    print(f"Request exception for {url}: Skipping to the next URL")
            else:
                print("")
    except:
        print("""
    Usage: python subcode.py <filename>
              """)

status_messages = {
    100: "100 Continue",
    101: "101 Switching Protocols",
    102: "102 Processing (WebDAV)",
    103: "103 Early Hints",
    200: f"{green}200 OK{nocolor}",
    201: f"{green}201 Created{nocolor}",
    202: f"{green}202 Accepted{nocolor}",
    203: f"{green}203 Non-Authoritative Information{nocolor}",
    204: f"{green}204 No Content{nocolor}",
    205: f"{green}205 Reset Content{nocolor}",
    206: f"{green}206 Partial Content{nocolor}",
    207: f"{green}207 Multi-Status (WebDAV){nocolor}",
    208: f"{green}208 Already Reported (WebDAV){nocolor}",
    226: f"{green}226 IM Used{nocolor}",
    300: f"{blue}300 Multiple Choices{nocolor}",
    301: f"{blue}301 Moved Permanently{nocolor}",
    302: f"{blue}302 Found (Moved Temporarily){nocolor}",
    303: f"{blue}303 See Other{nocolor}",
    304: f"{blue}304 Not Modified{nocolor}",
    305: f"{blue}305 Use Proxy (deprecated){nocolor}",
    307: f"{blue}307 Temporary Redirect{nocolor}",
    308: f"{blue}308 Permanent Redirect{nocolor}",
    400: f"{red}400 Bad Request{nocolor}",
    401: f"{red}401 Unauthorized{nocolor}",
    402: f"{red}402 Payment Required{nocolor}",
    403: f"{red}403 Forbidden{nocolor}",
    404: f"{red}404 Not Found{nocolor}",
    405: f"{red}405 Method Not Allowed{nocolor}",
    406: f"{red}406 Not Acceptable{nocolor}",
    407: f"{red}407 Proxy Authentication Required{nocolor}",
    408: f"{red}408 Request Timeout{nocolor}",
    409: f"{red}409 Conflict{nocolor}",
    410: f"{red}410 Gone{nocolor}",
    411: f"{red}411 Length Required{nocolor}",
    412: f"{red}412 Precondition Failed{nocolor}",
    413: f"{red}413 Payload Too Large{nocolor}",
    414: f"{red}414 URI Too Long{nocolor}",
    415: f"{red}415 Unsupported Media Type{nocolor}",
    416: f"{red}416 Range Not Satisfiable{nocolor}",
    417: f"{red}417 Expectation Failed{nocolor}",
    418: f"{red}418 I'm a teapot{nocolor}",
    421: f"{red}421 Misdirected Request{nocolor}",
    422: f"{red}422 Unprocessable Entity (WebDAV){nocolor}",
    423: f"{red}423 Locked (WebDAV{nocolor})",
    424: f"{red}424 Failed Dependency (WebDAV){nocolor}",
    425: f"{red}425 Too Early{nocolor}",
    426: f"{red}426 Upgrade Required{nocolor}",
    428: f"{red}428 Precondition Required{nocolor}",
    429: f"{red}429 Too Many Requests{nocolor}",
    431: f"{red}431 Request Header Fields Too Large{nocolor}",
    451: f"{red}451 Unavailable For Legal Reasons{nocolor}",
    500: f"{yellow}500 Internal Server Error{nocolor}",
    501: f"{yellow}501 Not Implemented{nocolor}",
    502: f"{yellow}502 Bad Gateway{nocolor}",
    503: f"{yellow}503 Service Unavailable{nocolor}",
    504: f"{yellow}504 Gateway Timeout{nocolor}",
    505: f"{yellow}505 HTTP Version Not Supported{nocolor}",
    506: f"{yellow}506 Variant Also Negotiates{nocolor}",
    507: f"{yellow}507 Insufficient Storage (WebDAV){nocolor}",
    508: f"{yellow}508 Loop Detected (WebDAV){nocolor}",
    510: f"{yellow}510 Not Extended{nocolor}",
    511: f"{yellow}511 Network Authentication Required{nocolor}"
}

def s_code(req, url):
    status_code = req.status_code
    if status_code in status_messages:
        print(url, status_messages[status_code])
    else:
        print(f"{url} {status_code} Unknown Status Code")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python subcode.py <filename>")
    else:
        filename = sys.argv[1]
        main(filename)
