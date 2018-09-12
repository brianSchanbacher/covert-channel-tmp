from pathlib import Path

DATA_FILE = Path("/tmp/covert/DATA")
DSR_FILE = Path("/tmp/covert/DSR")
DRD_FILE = Path("/tmp/covert/DRD")

def check_files():
    return(DATA_FILE.is_file(), DSR_FILE.is_file(), DRD_FILE.is_file())

def create_file(file_obj):
    open(file_obj.as_posix(), 'w').close()

def delete_file(file_obj):
    file_obj.unlink()


