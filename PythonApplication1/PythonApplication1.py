
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from matplotlib import style
import pyrealsense2 as rs
import cv2
import numpy as np

style.use('seaborn-poster')

fig = plt.figure()
ax1 = fig.add_subplot(2,3,1)    # will add x,y,z vs. time then velocoty vs. time
ax2 = fig.add_subplot(2,3,2)
ax3 = fig.add_subplot(2,3,3)

def eachGraph (xlocal,ylocal,whichGraph,ymeaning, GraphTitle):
    whichGraph.clear()
    whichGraph.plot(xlocal, ylocal)
    whichGraph.set_xlabel('Time (s)', fontsize=12)   # for now the x axis is time
    whichGraph.set_ylabel(ymeaning, fontsize=12)
    whichGraph.set_title(GraphTitle, fontsize=16)


#realtime graph
def animate(i):
    graph_data = open('3DPosition.txt','r').read()
    lines = graph_data.split('\n')

    # array of data for time, x,y,z (width, height, depth)
    ts = []
    xs = []
    ys = []
    zs = []

    # continue adding to array as collect more data realtime
    for line in lines:
            if len(line) > 1:
                    t, x, y, z = line.split(',')
                    
                    #I am trying to remove data that has a zero reading, but it is not seeing it as a 0
                    xnum = float (x)
                    ynum = float (y)
                    znum = float(z)

                    if xnum>0.001 and ynum>0.001 and znum>0.001:
                        #print (t,x,y,z,'\n')
                        ts.append(float(t))
                        xs.append(xnum)
                        ys.append(ynum)
                        zs.append(znum)
                        print(ts,xs,ys,zs)
                        

    # erase old graph and redraw so you can see the new data as it comes up realtime
    
    eachGraph(ts,xs,ax1,'Width (m)', 'Width of Object')
    eachGraph(ts,ys,ax2,'Height (m)', 'Height of Object')
    eachGraph(ts,zs,ax3,'Depth (m)', 'Depth of Object')

    ## Using IntelRealSense library 
# open("testing123.txt","w+")

# pipe = rs.pipeline()
# profile = pipe.start()

# append file
# open("testing123","a")


#try: 
#  for i in range(0, 100):
#    frames = pipe.wait_for_frames()
#    for f in frames:
#      print(f.profile)
#finally:
#    pipe.stop()
##



#try:
    #enable the stream from the camera
    #rs_config = rs.config()
    #rs_config.enable_stream(rs.sream.depth, resolution_width, resolution_hieght, rs.format.z16, fram_rate)





#draw graph
ani =  animation.FuncAnimation(fig, animate, interval=1000)    #graph again every 1 second=1000ms

# Add space between plots
plt.subplots_adjust(top=0.92,bottom=0.08,left=0.10,right=0.95, wspace=0.55)
plt.show()