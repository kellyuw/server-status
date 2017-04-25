import pandas as pd
from datetime import datetime
import os

epoch = datetime.utcfromtimestamp(0)
project_dir = "/Users/kelly89/Projects/ServerStatus/"
project_dir = ""
server_list = project_dir + "MachineList.txt"
t = datetime.now()
ofile = project_dir + "logfiles/" + datetime.strftime(t,"%Y%m%d-%H%M%S") + ".csv"
print(ofile)

def unix_time (dt):
    return (dt - epoch).total_seconds()

def get_ping_results():
    servers = [s.strip("\n") for s in open(server_list).readlines()]
    results = []

    for s in servers:
        hostname = s + ".ibic.washington.edu"
        r = ping_server(hostname)
        results += [[r, s, t]]
    return(results)

def ping_server(n):
    print 'pinging ' + str(n)
    return "success" if os.system("ping -c 1 -t 3 " + n) == 0 else "fail"

data = get_ping_results()
df = pd.DataFrame.from_records(data, columns = ['result','server','time'])
df['time_since_epoch'] = int((t - epoch).total_seconds())
df.to_csv(ofile, sep = ',', index = False, header = True)
