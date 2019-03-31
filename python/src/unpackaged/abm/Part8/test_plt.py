# -*- coding: utf-8 -*-
"""
Created on Tue Mar 12 22:42:04 2019

@author: hao2d9
"""

#import matplotlib.pyplot as plt
#import numpy as np
#
#carry_on = True
#
#def gen_function(b = [0]):
#    a = 0
#    print(a)
#    global carry_on #Not actually needed as we're not assigning, but clearer
#    while (a < 10) & (carry_on) :
#        print(a)
#        yield a			# Returns control and waits next call.
#        a = a + 1
#        print(a)
#
#x = np.arange(0, 10, 0.2)
#y = np.sin(x)
##fig = plt.figure()
##ax = fig.add_subplot(111)
##ax.plot(x, y)
##plt.show()
#
#gen_function()

#import numpy as np
#
#a = np.random.random((10,5))
#b = a[2:4,2:7]
#
#import numpy as np
#import matplotlib.pyplot as plt
#
## Data for plotting
#x1 = np.linspace(0.0, 5.0)
#x2 = np.linspace(0.0, 2.0)
#y1 = np.cos(2 * np.pi * x1) * np.exp(-x1)
#y2 = np.cos(2 * np.pi * x2)
#
## Create two subplots sharing y axis
#fig, (ax1, ax2) = plt.subplots(2, sharey=True)
#
#ax1.plot(x1, y1, 'ko-')
#ax1.set(title='A tale of 2 subplots', ylabel='Damped oscillation')
#
#ax2.plot(x2, y2, 'r.-')
#ax2.set(xlabel='time (s)', ylabel='Undamped')
#
#plt.show()

#import numpy as np
#import matplotlib.pyplot as plt
#from matplotlib.widgets import RadioButtons
#
#t = np.arange(0.0, 2.0, 0.01)
#s0 = np.sin(2*np.pi*t)
#s1 = np.sin(4*np.pi*t)
#s2 = np.sin(8*np.pi*t)
#
#fig, ax = plt.subplots()
#l, = ax.plot(t, s0, lw=2, color='red')
#plt.subplots_adjust(left=0.3)
#
#axcolor = 'lightgoldenrodyellow'
#rax = plt.axes([0.05, 0.7, 0.15, 0.15], facecolor=axcolor)
#radio = RadioButtons(rax, ('2 Hz', '4 Hz', '8 Hz'))
#
#
#def hzfunc(label):
#    hzdict = {'2 Hz': s0, '4 Hz': s1, '8 Hz': s2}
#    ydata = hzdict[label]
#    l.set_ydata(ydata)
#    plt.draw()
#radio.on_clicked(hzfunc)
#
#rax = plt.axes([0.05, 0.4, 0.15, 0.15], facecolor=axcolor)
#radio2 = RadioButtons(rax, ('red', 'blue', 'green'))
#
#
#def colorfunc(label):
#    l.set_color(label)
#    plt.draw()
#radio2.on_clicked(colorfunc)
#
#rax = plt.axes([0.05, 0.1, 0.15, 0.15], facecolor=axcolor)
#radio3 = RadioButtons(rax, ('-', '--', '-.', 'steps', ':'))
#
#
#def stylefunc(label):
#    l.set_linestyle(label)
#    plt.draw()
#radio3.on_clicked(stylefunc)
#
#plt.show()



#import matplotlib.pyplot as plt
#import numpy as np; np.random.seed(1)
#
#x = np.random.rand(15)
#y = np.random.rand(15)
#names = np.array(list("ABCDEFGHIJKLMNO"))
#c = np.random.randint(1,5,size=15)
#
#norm = plt.Normalize(1,4)
#cmap = plt.cm.RdYlGn
#
#fig,ax = plt.subplots()
#sc = plt.scatter(x,y,c=c, s=100, cmap=cmap, norm=norm)
#
#annot = ax.annotate("", xy=(0,0), xytext=(20,20),textcoords="offset points",
#                    bbox=dict(boxstyle="round", fc="w"),
#                    arrowprops=dict(arrowstyle="->"))
#annot.set_visible(False)
#
#def update_annot(ind):
#
#    pos = sc.get_offsets()[ind["ind"][0]]
#    annot.xy = pos
#    text = "{}, {}".format(" ".join(list(map(str,ind["ind"]))), 
#                           " ".join([names[n] for n in ind["ind"]]))
#    annot.set_text(text)
#    annot.get_bbox_patch().set_facecolor(cmap(norm(c[ind["ind"][0]])))
#    annot.get_bbox_patch().set_alpha(0.4)
#
#
#def hover(event):
#    vis = annot.get_visible()
#    if event.inaxes == ax:
#        cont, ind = sc.contains(event)
#        if cont:
#            update_annot(ind)
#            annot.set_visible(True)
#            fig.canvas.draw_idle()
#        else:
#            if vis:
#                annot.set_visible(False)
#                fig.canvas.draw_idle()
#
#fig.canvas.mpl_connect("motion_notify_event", hover)
#
#plt.show()

import matplotlib.pyplot as plt

fig = plt.figure()
plot = fig.add_subplot(111)

# create some curves
for i in range(4):
    plot.plot(
        [i*1,i*2,i*3,i*4],
        gid=i)

def on_plot_hover(event):
    for curve in plot.get_lines():
        if curve.contains(event)[0]:
            print("over %s" % curve.get_gid())

fig.canvas.mpl_connect('motion_notify_event', on_plot_hover)           
plt.show()