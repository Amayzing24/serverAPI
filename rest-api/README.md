# Bare metal server access service

## List all servers

'GET' call to '/servers'

Output:

```json
{
    "servers": "List of current servers in the database in types dict"
}
```

## Get a specific server

'GET' call to '/servers/<server_name>'

Output:

```json
{
    "server": "Server called for by server_name in type dict"
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

Output:

```json
{
    "server": "New server created in type dict"
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

Output:

```json
{
    "server": "Content of the updated server"
}
```
Throws 404 error if not found
Throws 400 error if not valid input

## Delete a server

'DELETE' call to '/servers/<server_name>'

Output:

```json
{
    "Result": True
}
```
Throws 404 error if not found



