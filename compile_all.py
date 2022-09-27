import os

status = 0

for file in os.listdir():
    if os.path.isfile(file) and file.endswith(".yaml"):
        print(f"------- Compiling {file} -------")
        res = os.system(f"esphome compile {file}")
        print(f"------- Finished compiling {file} with status {res} -------")
        status += res

exit(status)
