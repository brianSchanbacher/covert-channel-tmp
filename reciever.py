import file_operations as io
import time

data = ''
timeout = 0


while True:
    timeout += 1

    time.sleep(500/1000000.0) # Don't want to spin a core

    result = io.check_files()

    if result[1] == True and result[2] == False: # Time to read, DSR is set

        timeout = 0
        print("[RECIEVER] Reading Data: " + str(result))
        if result[0] == True:
            data+='1'
        else:
            data+='0'
        print("[RECIEVER] Setting DRD")
        io.create_file(io.DRD_FILE)

    elif result[1] == False and result[2] == True: # Remove DRD, because sender removed DSR
        timeout = 0
        print("[RECIEVER] Removing DRD")
        io.delete_file(io.DRD_FILE)

    if timeout >= 10000:
        print("Data: " + data)
        break
