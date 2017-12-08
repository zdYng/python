csvf = 'one-minute.json'
with open(csvf) as f:
    for row in f:
        time, predict = row['time'], row['*.AV']
        print(time,predict)
        break