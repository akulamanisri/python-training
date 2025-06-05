try:
    file=open("./names.txt","r")
    print(f"result is {file.readline()}")
    file.close()
except Exception as ex:
    print(f"error is {ex}")
finally:
    print("bye")