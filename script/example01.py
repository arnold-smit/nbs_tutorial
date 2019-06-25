## when a script is passed as argument to the python program __name__ is set to "__main__"
## this therefore is the entry point for any python script
if __name__ == "__main__":

    with open('../data/sentiment140_train_data.csv','r') as f: 
        f.seek(238802000)
        for line in f:
            print(line)

    with open('../data/sentiment140_train_data.csv','r') as f: 
        for _ in range(10):
            line = f.readline().strip()
            cols = line.split(",")
            print(",".join(cols[3:]))
