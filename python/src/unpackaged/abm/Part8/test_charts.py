import matplotlib.pyplot
import csv

neighbourhood_diameter = 30

f1 = open('in.txt', newline='')
reader = csv.reader(f1, quoting=csv.QUOTE_NONNUMERIC)

image = []

for row in reader:
    rowlist = []				
    for item in row:				
        rowlist.append(item)
    image.append(rowlist)

        
processed_image = []
for i in range(len(image)):
    row_list = []
    for j in range(len(image[i])):
        row_list.append(0)
    processed_image.append(row_list)

    
if neighbourhood_diameter < 1:
    neighbourhood_diameter = 1
    
if neighbourhood_diameter % 2 == 0:
    neighbourhood_diameter = neighbourhood_diameter + 1

neighbourhood_radius =  int((neighbourhood_diameter - 1) / 2)
    
    
for i in range(0 + neighbourhood_radius, len(image) - neighbourhood_radius):
    for j in range(0 + neighbourhood_radius, len(image[0]) - neighbourhood_radius):
        sum = 0
        for y in range(i - neighbourhood_radius, i + neighbourhood_radius + 1):     
            for x in range(j - neighbourhood_radius, j + neighbourhood_radius + 1):
                sum += image[y][x]
        average = sum / (neighbourhood_diameter * neighbourhood_diameter)
        processed_image[i][j] = average

        
matplotlib.pyplot.xlim(0, 299)
matplotlib.pyplot.ylim(0, 299)
sp1 = matplotlib.pyplot.subplot(1, 2, 1)
sp1.set_title("Original")
matplotlib.pyplot.imshow(image)        
#matplotlib.pyplot.plot(image)
 
sp2 = matplotlib.pyplot.subplot(1, 2, 2)
sp2.set_title("Smoothed")
matplotlib.pyplot.imshow(processed_image)   
#matplotlib.pyplot.plot(processed_image)     
matplotlib.pyplot.show()  


f2 = open('out.txt', 'w', newline='')
writer = csv.writer(f2, quoting=csv.QUOTE_NONNUMERIC)
for row in processed_image:		
    writer.writerow(row)		
f2.close()