def convert_to_menit(minggu, hari, jam, menit):
    return (minggu * 7 * 24 * 60) + (hari * 24 * 60) + (jam * 60) + menit

def curried_converter(minggu):
    def curry1(hari):
        def curry2(jam):
            def curry3(menit):
                return convert_to_menit(minggu, hari, jam, menit)
            return curry3
        return curry2
    return curry1

data = ["3 minggu 3 hari 7 jam 21 menit",
        "5 minggu 5 hari 8 jam 11 menit",
        "7 minggu 1 hari 5 jam 33 menit"]

output_data = []

for entry in data:
    parts = entry.split()
    minggu = int(parts[0])
    hari = int(parts[2])
    jam = int(parts[4])
    menit = int(parts[6])
    
    converter = curried_converter(minggu)(hari)(jam)(menit)
    output_data.append(converter)

print(output_data)
