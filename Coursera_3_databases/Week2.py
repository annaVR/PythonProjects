__author__ = 'anna'

import sqlite3

conn=sqlite3.connect('domaindb.sqlite')
cur=conn.cursor()

cur.execute('''
drop table if exists Counts''')

cur.execute('''
create table Counts (org text,count integer)''')

fname=raw_input("Enter file name:")
if len(fname)<1: fname=mbox.txt
fhandle=open(fname)

for line in fhandle:
    if not line.startswith("From:"): continue
    pieces=line.split()
    email=pieces[1]
    pieces_1=email.split("@")
    organisation=pieces_1[1]
    cur.execute('select count from Counts where org = ?', (organisation, ))
    try:
        cur.fetchone()[0]
        cur.execute("update Counts set count=count+1 where org=?", (organisation, ))
    except:
        cur.execute("insert into Counts (org, count) values (?,1)", (organisation, ))
    conn.commit()

sqlstr="select org,count from Counts order by count desc limit 10"
for row in cur.execute(sqlstr):
    print str(row[0]),row[1]
cur.close()

