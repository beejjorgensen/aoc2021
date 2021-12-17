data = None

TYPE_LITERAL = 0b100  # 4

LENGTH_TYPE_TOTAL = 0b0
LENGTH_TYPE_COUNT = 0b1

length_bits = {
    LENGTH_TYPE_TOTAL: 15,
    LENGTH_TYPE_COUNT: 11
}

def read_data(sample=None):
    sample_map = {
        1: "8A004A801A8002F478",             # 16
        2: "620080001611562C8802118E34",     # 12
        3: "C0015000016115A2E0802F182340",   # 23
        4: "A0016C880162017C3686B18A3D4780", # 31

        'A': "d2fe28",                       # Literal 2021
    }

    global data

    if sample is None:
        INPUT = "input.txt"

        fp = open(INPUT)
        hex_data = fp.readline().strip()
        fp.close()

    else:
        hex_data = sample_map[sample]

    data = f"{int(hex_data,16):b}"

    return data

def read_packet(data):
    
    version = int(data[0:3], 2)
    type_id = int(data[3:6], 2)

    print(version, type_id)
    if type_id == TYPE_LITERAL:
        have_more = 1
        pos = 0
        total = 0

        while have_more == 1:
            have_more = int(data[6+5*pos])
            value = int(data[6+5*pos+1:6+5*pos+5], 2)
            total <<= 4
            total |= value
            pos += 1

        return total
        
    # return operator on all subpackets, recursively

    """
    # operator
    length_type = int(data[6], 2)
    bits = length_bits[length_type]
    subpacket_start = 7 + bits
    length = int(data[7:subpacket_start], 2)

    if length_type == LENGTH_TYPE_TOTAL:
        read_packet_set(data[subpacket_start:subpacket_start + length])

    elif length_type == LENGTH_TYPE_COUNT:
        for _ in range(length):
    """

    return None

data = read_data('A')
print(data)

t = read_packet(data)

print(t)

