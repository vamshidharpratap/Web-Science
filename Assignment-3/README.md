# Implementing a simplified HTTP GET Request

The goal of this exercise is to review the hypertext transfer protocol and gain a better
understanding of how it works.

Your task is to use the python programming language to create an HTTP client (httpclient.py that takes a URL as a command line argument and is able to download an arbitrary file from the World Wide Web and store it on your hard drive (in the same directory as your python code is running).
The program should also print out the complete HTTP header of the response. Your program should only use the socket library so that you can open a TCP socket and sys library to do command line parsing.

Your program should be able to successfully download: 
<br>
  • https://west.uni-koblenz.de/studying/ws2223/introduction-web-science

## 2.1 Hints:

There will be quite some challenges in order to finish the task Your program only has to be able to process HTTP-responses with status 200 OK.

• Make sure you receive the full response from your TCP socket. (create a function
  handling this task)  
• Separated the HTTP header from the body (again create a function to do this)
<br>
• If a binary file is requested make sure it is not stored in a corrupted way

## 2.2 Example

1: python httpclient.py http://west.uni-koblenz.de/index.php <br/>
2: <br/>
3: HTTP/1.1 200 OK <br/>
4: Date: Wed, 16 Nov 2016 13:19:19 GMT 5: Server: Apache/2.4.7 (Ubuntu) <br/>
6: X-Powered-By: PHP/5.5.9-1ubuntu4.20 <br/>
7: X-Drupal-Cache: HIT 8: Etag: 1479302344 - 01 <br/>
9: Content-Language: de <br/>
10: X-Frame-Options: SAMEORIGIN <br/>
11: X-UA-Compatible: IE=edge, chrome-1 <br/>
12: X-Generator: Drupal 7 (http://drupal.org) <br/>
13: Link: <http://west.uni-koblenz.de/de>; rel="canonical", <http://west- <br/>
14: Cache-Control: public, max-age=0 <br/>
15: Last-Modified: Wed, 16 Nov 2016 13:19:04 GMT <br/>
16: Expires: Sun, 19 Nov 1978 05:00:00 GMT <br/>
17: Vary: Cookie, Accept-Encoding <br/>
18: Connection: close <br/>
19: Content-Type: text/html; charset=utf-8 <br/>

The header will be printed and the retrieved html document will be stored in inder.php
