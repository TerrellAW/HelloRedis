For persistent storage in redis run:

``` bash
docker run --rm --name redis -d -p 6379:6379 -v /path/on/computer:/data --network flask redis
docker run --rm --name python-server -d --network flask -p 8001:80 python-server:latest
```
