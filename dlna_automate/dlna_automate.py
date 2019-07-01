#!/usr/bin/env python3

import os, fnmatch, shutil, requests

dlna_path = "/Users/your_user/dlna"

downloads_path = "/Users/your_user/Downloads/"

patterns = ['*.mkv', '*.avi']

def find_files(patterns, path):
    result = []
    for root, dirs, files in os.walk(path):
        for pattern in patterns:
            for name in files:
                if fnmatch.fnmatch(name, pattern):
                    result.append(os.path.join(root, name))
    return result


#Python 2
# def refresh_serviio(*arg):
#     connection = httplib2.HTTPConnection('127.0.0.1.:23423')
#     body_content = '<action><name>forceLibraryRefresh</name></action>'
#     connection.request('POST', '/rest/acetion', body_content)
#     result = connection.getresponse()
#     if result.status == 200:
#         print("Updated Serviio Library")
#     else:
#         print("Update Failed")

def refresh_serviio(*arg):
    headers = {
        'Content-Type': 'text/xml',
    }

    data = '<action><name>forceLibraryRefresh</name></action>'

    response = requests.post('http://127.0.0.1:23423/rest/action', headers=headers, data=data)

    print(response)


if __name__ == "__main__":

    files = find_files(patterns, downloads_path)

    for file in files:
        shutil.move(file, dlna_path)

    refresh_serviio()