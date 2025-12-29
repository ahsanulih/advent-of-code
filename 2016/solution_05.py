import hashlib

def convert_to_md5(data):
    # Encode the string into bytes using UTF-8
    encoded_data = data.encode('utf-8')
    # Create an MD5 hash object and update it with the data
    m = hashlib.md5(encoded_data)
    # Get the hash as a 32-character hexadecimal string
    md5_hash = m.hexdigest()
    return md5_hash

# Part 1
# Simulation
input = "ugkcyxxp"
res = ""
cur = 1
while True:
    md5_hash = convert_to_md5(input + str(cur))
    if md5_hash[:5] == "00000": 
        print(cur, md5_hash)
        res += md5_hash[5]
    cur += 1
    if len(res) == 8:
        break
print("Given the actual Door ID, what is the password?", res)

# Part 2
# Simulation
input = "ugkcyxxp"
nums = {'0', '1', '2', '3', '4', '5', '6', '7'}
res = [""] * 8
found = 0
cur = 1
while True:
    md5_hash = convert_to_md5(input + str(cur))
    if md5_hash[:5] == "00000" and md5_hash[5] in nums and res[int(md5_hash[5])] == "":
        print(cur, md5_hash)
        res[int(md5_hash[5])] = md5_hash[6]
        found += 1
    cur += 1
    if found == 8:
        break
print("Given the actual Door ID, what is the password?", ''.join(res))
