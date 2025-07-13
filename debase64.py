import base64#A library in Python that does not need to be downloaded.
cipher="the_cipher_text"#No needed any explain to this part
ciphir=ciphir[::-1]#If the text is reversed
decode_bytes =base64.b64decode(ciphir)#in this part the code will decode the cipher the result for this process is bytes
decode_str=decode_bytes.decode('utf-8',errors='ignore')#in this part the code will convert from byte to string
print(decode_str)
