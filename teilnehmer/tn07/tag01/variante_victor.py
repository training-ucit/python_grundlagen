try:
    with open(src_file, "r") as src:
        text = src.read()
        pos = text.find("127.0.0.1")
        while pos >= 0 :
            print(pos)
            pos = text.find("127.0.0.1", pos+1)
except Exception as e:
    print ("Unexpected error:", e)
    raise
finally:
    print ("Finita")