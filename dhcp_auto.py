import csv
with open('dhcp.csv','r') as f:
    data = csv.reader(f)
    with open('dhcp_conf.txt','w') as conf:
        for row in data:
            conf.write("config host\n")
            conf.write("\t option ip \t '{0}'\n".format(row[1]))
            conf.write("\t option mac \t '{0}'\n".format(row[0]))
            conf.write("\t option name \t '{0}'\n".format(row[2]))
            conf.write("\n")
