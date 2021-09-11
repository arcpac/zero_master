# import mysql.connector

# con = mysql.connector.connect(
# user = "localhost",
# password = "localhost",
# host = "127.0.0.1",
# database = "test_python"
# )

#print(range(4))
for n in range(4):
    # print(n)
    for i in range(n+1):
        print(i, end=" ")
    print("")