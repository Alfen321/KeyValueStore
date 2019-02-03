#! /usr/bin/python3


def main():
    # byte_offset = save_to_file('somedata')
    db_set('somekey', 'some value')
    val = db_get('somekey')
    print(val)
    # print(read_part(0))


offset_memory = {}


def reload_offset_memory():
    global offset_memory
    offset = 0
    size = 0
    offset_memory = {}
    with open('data.db', 'rb') as f:
        size = len(f.read())
        while offset < size:
            f.seek(offset)
            length = int.from_bytes(f.read(8), byteorder='big')
            offset += 8
            f.seek(offset)
            key = f.read(length).decode('utf-8')
            offset_memory[key] = offset - 8
            offset += length
            f.seek(offset)
            length = int.from_bytes(f.read(8), byteorder='big')
            offset += 8 
            offset += length 
    return offset_memory


def offsets_get():
    return offset_memory


def db_set(key, value):
    offset = save_to_file(key, value)
    offset_memory[key] = offset


def db_get(key):
    if key in offset_memory:
        return read_part(offset_memory[key])
    else:
        return None


def read_part(offset):
    with open('data.db', 'rb') as f:
        f.seek(offset)
        length = int.from_bytes(f.read(8), byteorder='big')
        offset += 8
        f.seek(offset)
        # key = f.read(length).decode('utf-8') # might not be needed
        offset += length
        f.seek(offset)
        length = int.from_bytes(f.read(8), byteorder='big')
        return f.read(length).decode('utf-8')


def save_to_file(key, value):
    with open('data.db', 'ab') as f:
        offset = f.tell()
        f.write((len(key)).to_bytes(8, byteorder='big'))
        f.write(bytes(key, 'utf-8'))
        f.write((len(value)).to_bytes(8, byteorder='big'))
        f.write(bytes(value, 'utf-8'))
        return offset


if __name__ == "__main__":
    main()
