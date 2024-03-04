import time
message = "hello world"
alphabet = "abcdefghijklmnopqrstuvwxyz"

# Print all possible prefixes
for i in range(len(message)):
    for j in range(len(alphabet)):
        prefix = alphabet[j]
        current_str = message[:i] + prefix
        
        if current_str == message[:i+1]:
            print(current_str)
            break
        print(current_str)
