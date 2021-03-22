import decimal
import os
import numpy as np
import matplotlib.pyplot as plt
import imageio
import matplotlib as mpl

def pi():
    #took this simple formula from another website but forgot where so can't give the source
    decimal.getcontext().prec += 2  
    three = decimal.Decimal(3)      
    lasts, t, s, n, na, d, da = 0, three, 3, 1, 0, 0, 24
    while s != lasts:
        lasts = s
        n, na = n + na, na + 8
        d, da = d + da, da + 32
        t = (t * n) / d
        s += t
    decimal.getcontext().prec -= 2
    return +s             


decimal.getcontext().prec = 100 #how many digits you want
pie = pi()
pie = str(pie).replace(".","")
filenames = []
sizes = [0]*10
labels = np.arange(10) 
plt.style.use('ggplot') #change style to your liking


#these are just for the videospeed
slow = 30
medium = 60
fast = 100


mpl.rcParams['font.size'] = 15
for i, digit in enumerate(pie):
    plt.figure(figsize=(10,10))
    plt.xlabel(f"n={i}", loc="right", size=20)
    sizes[int(digit)] += 1
    plt.title("Frequency of digits in π")
    p, tx, autotexts = plt.pie(sizes, labels=labels, autopct="")
    if sizes.count(0) <= 2:
        for j, a in enumerate(autotexts):
            a.set_text("{}".format(sizes[j]))
    filename = f'{i}.png'
    filenames.append("figures/"+filename)
    
    #these are just for the videospeed
    if (i <= slow):
            for i in range(4):
                filenames.append("figures/"+filename)
    if (i <= medium and i > slow):
            for i in range(2):
                filenames.append("figures/"+filename)
    if (i <= fast and i > medium):
                filenames.append("figures/"+filename)
            
            
    plt.savefig("figures/"+filename, dpi=96, facecolor='#95A4AD')
    #plt.show()
    plt.close()
    
    
# creates the video (fps parameter changes the speed)    
with imageio.get_writer('16fpsbig1.gif', fps=16) as writer:
    for filename in filenames:
        image = imageio.imread(filename)
        writer.append_data(image)


# deletes the .png files after the conversion
dir_name = "figures/"
test = os.listdir(dir_name)

for item in test:
    if item.endswith(".png"):
        os.remove(os.path.join(dir_name, item))
