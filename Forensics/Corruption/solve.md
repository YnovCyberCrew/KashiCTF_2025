Photorec on the file

Then :

```
find . -type f -exec strings {} \; | grep -E '.*Kashi.*'
```
