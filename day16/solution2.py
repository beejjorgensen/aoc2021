data = None

TYPE_LITERAL = 0b100  # 4

LENGTH_TYPE_TOTAL = 0b0
LENGTH_TYPE_COUNT = 0b1

length_bits = {
    LENGTH_TYPE_TOTAL: 15,
    LENGTH_TYPE_COUNT: 11
}

def product(a):
    r = 1

    for i in a:
        r *= i

    return r

operator = {
    0: sum,
    1: product,
    2: min,
    3: max,
    5: lambda x: 1 if x[0] > x[1] else 0,
    6: lambda x: 1 if x[0] < x[1] else 0,
    7: lambda x: 1 if x[0] == x[1] else 0,
}

def read_data(sample=None):
    sample_map = {
        1: "8A004A801A8002F478",             # 16
        2: "620080001611562C8802118E34",     # 12
        3: "C0015000016115A2E0802F182340",   # 23
        4: "A0016C880162017C3686B18A3D4780", # 31

        'A': "d2fe28",                       # Literal 2021
        'B': "38006f45291200",               # Op and literal 10 then 20, length
        'C': "EE00D40C823060",               # Op and 3 literals, count

        'D': "C200B40A82", # finds the sum of 1 and 2, resulting in the value 3.
        'E': "04005AC33890", # finds the product of 6 and 9, resulting in the value 54.
        'F': "880086C3E88112", # finds the minimum of 7, 8, and 9, resulting in the value 7.
        'G': "CE00C43D881120", # finds the maximum of 7, 8, and 9, resulting in the value 9.
        'H': "D8005AC2A8F0", # produces 1, because 5 is less than 15.
        'I': "F600BC2D8F", # produces 0, because 5 is not greater than 15.
        'J': "9C005AC2F8F0", # produces 0, because 5 is not equal to 15.
        'K': "9C0141080250320F1802104A08", # produces 1, because 1 + 3 = 2 * 2.
    }

    global data

    if sample is None:
        INPUT = "input.txt"

        fp = open(INPUT)
        hex_data = fp.readline().strip()
        fp.close()

    else:
        hex_data = sample_map[sample]

    data = ""

    for d in hex_data:
        data += f"{int(d, 16):04b}"

    return data

def value_of(data, offset=0):

    def ds(a, ln=1):
        b = a + ln
        #print()
        #print(a, ln, b)
        #print(offset, a+offset, b+offset)
        return int(data[offset+a:offset+b], 2)
    
    version = ds(0, 3)
    type_id = ds(3, 3)  # operator
    packet_len = 6

    if type_id == TYPE_LITERAL:
        have_more = 1
        pos = 0
        total = 0

        while have_more == 1:
            have_more = ds(6 + 5 * pos)
            value = ds(6 + 5 * pos + 1, 4)
            total <<= 4
            total |= value
            pos += 1
            packet_len += 5

        return total, packet_len 
        
    # return operator on all subpackets, recursively
    def compute_total(v):
        nonlocal total

        if total is None:
            total = v

        else:
            total += v  # TODO unhardcode operator

    done = False

    length_type = ds(6)
    length_bit_count = length_bits[length_type]
    length = ds(7, length_bit_count)

    packet_len += 1 + length_bit_count

    operands = []

    count = 0

    assert(length_type == LENGTH_TYPE_TOTAL or length_type == LENGTH_TYPE_COUNT)

    while not done:
        sub_value, sub_length = value_of(data, offset + packet_len)

        packet_len += sub_length
        operands.append(sub_value)
        
        if length_type == LENGTH_TYPE_TOTAL:
            count += sub_length 
            
        elif length_type == LENGTH_TYPE_COUNT:
            count += 1

        done = count >= length

    result = operator[type_id](operands)

    return result, packet_len

data = read_data()
#print(data)

t, _ = value_of(data)

print(t, _)
