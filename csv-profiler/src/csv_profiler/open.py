# f=open("/jjj.csv","r")
# content=f.read()
# print(content)
# f.close()

with open("\\csv_profiler\\jjj.csv" ,mode="r") as f:
    content=f.read()
print(content)