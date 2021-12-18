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

t, _ = value_of(data)

print(t)
