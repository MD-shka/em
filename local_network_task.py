class IPGenerator:
    next_ip_adress = 1


class Server:
    def __init__(self):
        self.ip = IPGenerator.next_ip_adress
        IPGenerator.next_ip_adress += 1
        self.buffer = []

    def send_data(self, data):
        Router().buffer.append(data)

    def get_data(self):
        data = self.buffer.copy()
        self.buffer.clear()
        return data

    def get_ip(self):
        return self.ip


class Router:
    _instance = None

    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
            cls._instance.buffer = []
            cls._instance.linked_servers = []
        return cls._instance

    def link(self, server):
        if server not in self.linked_servers:
            self.linked_servers.append(server)

    def unlink(self, server):
        if server in self.linked_servers:
            self.linked_servers.remove(server)

    def send_data(self):
        for data in self.linked_servers:
            for server in self.linked_servers:
                if server.get_ip() == data.ip:
                    server.buffer.append(data)
                    break
        self.buffer.clear()


class Data:
    def __init__(self, data, ip):
        self.data = data
        self.ip = ip
