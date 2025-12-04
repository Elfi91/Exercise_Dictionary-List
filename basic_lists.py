'''
Goal: Familiarize with basic list methods.

'''

server: list[str] = ["web01", "db01", "cache01"]

server.append("backup01")

server.insert(0, "proxy01")

server.remove("cache01")

print(server)
print(f"Number of server: {len(server)}")

