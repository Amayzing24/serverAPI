import requests

# Clear out the servers first
response = requests.get("http://127.0.0.1:5000/servers")
for server in response.json()['servers']:
    requests.delete("http://127.0.0.1:5000/servers/" + server['name'])

# Test create_server (Empty before)
response = requests.post("http://127.0.0.1:5000/servers", json={'name': 'TestServer',
                                                                'type': 'Web Server',
                                                                'location': 'San Jose'})
if (response.json()['server']['name'] == 'TestServer'):
    print("create_server success")
else:
    print("create_server failed")

# Test get_servers (1 server added in the database)
response = requests.get("http://127.0.0.1:5000/servers")
if (response.json()['servers'][0]['name'] == 'TestServer'):
    print("get_servers success")
else:
    print("get_servers failed")

# Test get_server
response = requests.get("http://127.0.0.1:5000/servers/TestServer")
if (response.json()['server']['name'] == 'TestServer' and response.json()['server']['type'] == 'Web Server'):
    print("get_server success")
else:
    print("get_server failed")

# Test update server
response = requests.put("http://127.0.0.1:5000/servers/TestServer", json={'type': 'Proxy Server'})
if (response.json()['server']['type'] == 'Proxy Server'):
    print("update_server success")
else:
    print("update_server failed")

# Test delete_server
response = requests.delete("http://127.0.0.1:5000/servers/TestServer")
if (response.json()['result'] == True):
    print("delete_server success")
else:
    print("delete_server failed")
