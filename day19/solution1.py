INPUT = "input1.txt"

def read_data():
    data = []

    with open(INPUT) as fp:
        line_data = []

        for line in fp:

            line = line.strip()

            if line == "": continue

            if line[:3] == "---":
                scanner_id = int(line.split()[2])
                if scanner_id > 0:
                    data.append(line_data)
                    line_data = []
                continue

            line_data.append(line.split(","))

        data.append(line_data)
        line_data = []

    return data

data = read_data()
