import html

encoded_str = "ɔpɣaːvə"
decoded_str = html.unescape(encoded_str)

print ("Encoded", encoded_str)
print ("Decoded ", decoded_str)