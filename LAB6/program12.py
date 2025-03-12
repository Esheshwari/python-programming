lines=["First line\n", "sec line\n", "Third line\n"]
file_handle=open("textfile1", "w")
file_handle.writelines(lines)
file_handle.close()
