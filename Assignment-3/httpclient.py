#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Nov 20 00:38:09 2022

@author: vamshidharpratap
"""

import socket
import sys

print("The argument passed is:")
print(sys.argv[1])
url = sys.argv[1]

#create a socket object
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)


def get_header(response):
    """
    This function will accept the http response object and process the Http 
    response
    :param response : the http response object
    
    returns http response header if status code is 200 else returns 0
    """
    response = str(response.decode('utf-8'))
    http_statuscode = response[8:13]
    
    
    if int(http_statuscode) == 200 :
        
        temp = response.find('<!doctype html>')
        reaponse_header = response[:temp]
        return reaponse_header
    
    else:
    
        print("The staus code for the request is ",http_statuscode)
    return False


def get_response(socket_obj):

    """
    This function will receives the full response from socket.
    
    :param socket_obj : sockect object of the TCP socket where the response is 
                        received.
    
    returns : response recieved will be returned                    
    """
    '''
    while True:
        
        response = socket_obj.recv(16594)
        if not response:
            break
        else:
            response_data = response
    ''' 
    response_data  = socket_obj.recv(16594)          
    return response_data


#url = "https://west.uni-koblenz.de/studying/ws2223/introduction-web-science"

#url = "www.example.com"


double_slash_pos = url.find("//")
single_slash_pos = url[double_slash_pos + 2 :].find('/')

if double_slash_pos > 0 :

    host = url[double_slash_pos + 2 : double_slash_pos + 2 + single_slash_pos ]

else :
    # For the given url domain name is missing
    #print("Enter the valid url the domain name is not present")
    host = url

#make the connection
# Http port always run on port 80

sock.connect((host, 80))
print("\nConnection made successfully\n")
try:

    request = "GET / HTTP/1.1\r\nHost:%s\r\n\r\n" %url
    #print(request)
    sock.send(request.encode('utf-8'))

    response = get_response(sock)  
    
    response_header = get_header(response)
    if response_header :
        print(response_header)


finally:
 
    sock.close()



