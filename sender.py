import file_operations as io
import time

data = iter(list('11001100' * 1000000))
bit = next(data)

try:
    io.delete_file(io.DATA_FILE)
    io.delete_file(io.DSR_FILE)
    io.delete_file(io.DRD_FILE)
except FileNotFoundError:
    pass

while True:
    time.sleep(500/1000000.0) # Don't want to spin a core

    result = io.check_files()

    if result == (False, False, False): # Time to start communication
        if bit == "1":
            io.create_file(io.DATA_FILE)
        # set DSR because now the data has been written
        io.create_file(io.DSR_FILE)
        print("[SENDER] Bit set: " + bit)
        try:
            bit = next(data)
        except StopIteration:
            # No more bits to send!
            break

    elif result[2] == True and result[1] == True: # Remove DSR, because reciever removed DRD
        io.delete_file(io.DSR_FILE)
        try:
            io.delete_file(io.DATA_FILE)
        except FileNotFoundError:
            pass
        print("[SENDER] Bit reported as consumed")
