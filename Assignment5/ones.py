#all of the work herein is solely mine

def lr(xlst):
    currentLargest = 0
    current = 0
    for i in xlst:
        if i == 1:
            current += 1
        else:
            current = 0
        if current > currentLargest:
            currentLargest = current
    return currentLargest

if __name__ == "__main__":
    x = [0,1,1,1,1,1,0,1,1,0,1,0,1,0,1,1,0,1,1,0]
    y = [0,1,1,1,1,1,1,1,1,1,1,1,0,0,0,1,1,0,1,1,1,1,1]
    z = [0,1,1,1,0,1,1,1,1,0,1,1,0,1]
    xx = []
    xy = [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1]
    xz = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
    aList = [x,y,z,xx,xy,xz]
    for i in aList:
        print(lr(i))
