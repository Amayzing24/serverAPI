# Bare metal server access service

## List all servers

'GET' call to '/servers'

Outputs a list of the current servers in the database (key = 'servers'). Example:

```json
{
    "servers": [
        {
            "name":"NewServer1",
            "type":"Web Server",
            "location":"New York",
            "ipaddress":"1.72.68.901",
            "other":[]
        },
        {
            "name":"NewServer2",
            "type":"Proxy Server",
            "location":"Los Angeles",
            "ipaddress":"7.72.881.1",
            "other":[{"inUse": "True"}]
        }
    ]
}
```

## Get a specific server

'GET' call to '/servers/<server_name>'

Outputs the specific server called for (key = 'server'). Example:

```json
{
    "server": {
        "name":"NewServer1",
        "type":"Web Server",
        "location":"New York",
        "ipaddress":"1.72.68.901",
        "other":[]
    }
}
```
Throws 404 error if not found

## Create a server

'POST' call to '/servers' with 'Content-Type: application.json'

Arguments:
- '"name":string' - name of this specific server (serves as an ID)
- '"type":string' - type of the server (Proxy, Web, etc.)
- '"location":string' - location of the server
- '"ipaddress":string, default="111.1.1.111"' - IP address of the server's location
- '"other":list, default=[]' - any other information for the server

Outputs the server created (key = "server"). Example:

```json
{
    "server": {
        "name":"TestServer",
        "type":"Application Server",
        "location":"San Jose",
        "ipaddress":"1.1.1.1",
        "other":[]
    }
}
```
Gives 201 success code
Throws 400 error if not valid input or if a server with the given name already exists

## Update a server

'PUT' call to '/servers/<server_name>' with 'Content-Type: application.json'

Arguments:
- '"name":string' - new name of the server
- '"type":string' - new type of the serveer
- '"location":string' - new location of the server
- '"ipaddress":string' - new IP address
- '"other":list, default=[]' - new list of other information
All parameters do not need to be included. Only the ones that are being updated should be included.

Outputs the content of the updated server (key = "server). Example:

```json
{
    "server": {
        "name":"TestServer",
        "type":"Application Server",
        "location":"Cupertino",
        "ipaddress":"1.1.1.1",
        "other":[]
    }
}
```
Throws 404 error if not found
Throws 400 error if not valid input

## Delete a server

'DELETE' call to '/servers/<server_name>'

Outputs True (key = "result") to indicate the server was deleted:

```json
{
    "result": "True"
}
```
Throws 404 error if not found



