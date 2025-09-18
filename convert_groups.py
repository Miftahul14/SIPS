

input_file = 'groups.json' 
output_file = 'groups.json'

with open(input_file, 'rb') as f:
    data = f.read()

with open(output_file, 'w', encoding='utf-8') as f:
    f.write(data.decode('utf-8-sig'))

print("File groups.json berhasil dikonversi ke UTF-8 tanpa BOM")
