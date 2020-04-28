import re

categories = []
i = 0
while i < 68 :
    categories.append("")
    i += 1
categories[23] = 'Motorcycle Pack'
categories[24] = 'Mazda'
categories[24] = 'Mazda'
categories[25] = 'Nissan'
categories[26] = 'Toyota'
categories[27] = 'BMW'
categories[28] = 'Honda'
categories[29] = 'Lexus'
categories[30] = 'Volkswagen'
categories[31] = 'Subaru'
categories[32] = 'Bikes'
categories[33] = 'Range Rover'
categories[34] = 'Mercedes Benz'
categories[35] = 'Ferrari'
categories[36] = 'Vanilla'
categories[37] = 'Porsche'
categories[38] = 'Bugatti'
categories[39] = 'Kia'
categories[40] = 'Henry Clay'
categories[41] = 'Opel'
categories[42] = 'Aston Martin'
categories[43] = 'Mclaren'
categories[44] = 'Koenigsegg'
categories[45] = 'Lamborghini'
categories[46] = 'Ford'
categories[47] = 'Jeep'
categories[48] = 'Audi'
categories[49] = 'Mitsubishi'
categories[50] = 'Alpine'
categories[51] = 'Chevrolet'
categories[52] = 'Renault'
categories[53] = 'Saleen'
categories[54] = 'TVR'
categories[55] = 'Rolls Royce'
categories[56] = 'Pagani'
categories[57] = 'Boats'
categories[58] = 'Five-O'
categories[59] = 'Acura'
categories[60] = 'Hyundai'
categories[61] = 'Mini'
categories[62] = 'RAM'
categories[63] = 'Vanilla Edits'
categories[64] = 'ISUZU'
categories[65] = 'International'
categories[66] = 'Polaris'
categories[67] = 'GMC'

with open("D:/addon.txt") as file:
    for files in file.readlines():
            aline2 = re.split("\:+", files)
            number = int(aline2[2])
            carName = aline2[1]
            carModelName = aline2[0]
            for i in categories:
                if (number == categories.index(i)):
                    categoryName = i
                    print("Category Name: " + str(categoryName) + " - Model Name: " + carModelName + " - Car Name: "+ carName)
file.close()
