input_filename = "./models.py"
output_filename = "./models2.py"

with open(input_filename, "rb") as input_file:
    content = input_file.read()

content_without_nulls = content.replace(b'\x00', b'')

with open(output_filename, "wb") as output_file:
    output_file.write(content_without_nulls)