#!/usr/bin/python

file_path="./qmq_info_delete.sql"
with open(file_path, "a+") as f:
    start = 3258339
    end = 53429533
    batch = 10000
    i = start
    while i < end:
        f.write("delete from hotel_direct_qmq_info where id >= "+`i`+" and id < "+`i+batch`+";\n")
        i = i + batch