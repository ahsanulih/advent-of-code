import hashlib

def convert_to_md5(data):
    # Encode the string into bytes using UTF-8
    encoded_data = data.encode('utf-8')
    # Create an MD5 hash object and update it with the data
    m = hashlib.md5(encoded_data)
    # Get the hash as a 32-character hexadecimal string
    md5_hash = m.hexdigest()
    return md5_hash

# Part 1 and 2
# Brute force
input_string = "iwrupvqb"
i = 1
while True:
    new_string = input_string + str(i)
    converted = convert_to_md5(new_string)
    found1 = False
    found2 = False
    if converted[:5] == "00000":
        print("Result 1:", i)
        found1 = True 
    if converted[:6] == "000000":
        print("Result 2:", i)
        found2 = True
    if found1 and found2:
        break 
    i += 1


