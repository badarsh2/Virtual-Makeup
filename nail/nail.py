import numpy as np
from scipy import interpolate
from scipy.misc import imresize
from pylab import *
from skimage import color
from sys import version_info

Rg, Gg, Bg = (121.,13.,188.)

py3 = version_info[0] > 2 #creates boolean value for test that Python major version > 2

if py3:
  response_texture = input("Please enter \n 1 for texture 1 \n 2 for texture 2 \n 3 for texture 3 \n 4 for texture 4 \n 5 for texture 5 \n 6 for texture 6: ")
else:
  response_texture = raw_input("Please enter \n 1 for texture 1 \n 2 for texture 2 \n 3 for texture 3 \n 4 for texture 4 \n 5 for texture 5 \n 6 for texture 6: ")

if(response_texture == '1'):
	texture_input = 'texture.jpg'
elif(response_texture == '2'):
	texture_input = 'texture1.jpg'
elif(response_texture == '3'):
	texture_input = 'texture2.jpg'
elif(response_texture == '4'):
	texture_input = 'texture3.jpg'
elif(response_texture == '5'):
	texture_input = 'texture4.jpg'
elif(response_texture == '6'):
	texture_input = 'texture5.jpg'
else:
	print 'Invalid. Taking default'
	texture_input = 'texture.jpg'

if py3:
  response_type = input("Please enter \n 1 for round length 1 \n 2 for round length 2 \n 3 for square length 1 \n 4 for square length 2 \n 5 for round & square: ")
else:
  response_type = raw_input("Please enter \n 1 for round length 1 \n 2 for round length 2 \n 3 for square length 1 \n 4 for square length 2 \n 5 for round & square: ")

if(response_type == '1'):
	im = imread('roundLength1.jpg')
	points = np.loadtxt('nailpoint_2')
elif(response_type == '2'):
	im = imread('roundLength2.jpg')
	points = np.loadtxt('nailpoint_3')
elif(response_type == '3'):
	im = imread('squareLength1.jpg')
	points = np.loadtxt('nailpoint_4')
elif(response_type == '4'):
	im = imread('squareLength2.jpg')
	points = np.loadtxt('nailpoint_5')
elif(response_type == '5'):
	im = imread('square&roundLength0.jpg')
	points = np.loadtxt('nailpoint')
else:
	print 'Invalid. Taking default'
	im = imread('square&roundLength0.jpg')
	points = np.loadtxt('nailpoint')


def getBoundaryPoints(x = [], y = []):
	tck,u = interpolate.splprep([x, y], s=0, per=1)
	unew = np.linspace(u.min(), u.max(), 1000)
	xnew,ynew = interpolate.splev(unew, tck, der=0)
	tup = c_[xnew.astype(int),ynew.astype(int)].tolist()
	coord = list(set(tuple(map(tuple, tup))))
	coord = np.array([list(elem) for elem in coord])
	return coord[:,0],coord[:,1]
	
def getInteriorPoints(x = [], y = []):
	nailx = []
	naily = []
	def ext(a, b, i):
		a, b=round(a), round(b)
		nailx.extend(arange(a, b, 1).tolist())
		naily.extend((ones(b-a)*i).tolist())
	x, y = np.array(x), np.array(y)
	xmin, xmax = amin(x), amax(x)
	xrang = np.arange(xmin, xmax + 1, 1)
	for i in xrang:
		ylist = y[where(x==i)]
		ext(amin(ylist), amax(ylist), i)
	return nailx, naily

# im = imread('squareLength2.jpg')

def applyNailPolish(x , y , r = Rg, g = Gg, b = Bg):
	val = color.rgb2lab((im[x, y]/255.).reshape(len(x), 1, 3)).reshape(len(x), 3)
	L, A, B = mean(val[:,0]), mean(val[:,1]), mean(val[:,2])
	L1, A1, B1 = color.rgb2lab(np.array((r/255., g/255., b/255.)).reshape(1, 1, 3)).reshape(3,)
	ll, aa, bb = L1 - L, A1 - A, B1 - B
	val[:, 0] = np.clip(val[:, 0] + ll, 0, 100)
	val[:, 1] = np.clip(val[:, 1] + aa, -127, 128)
	val[:, 2] = np.clip(val[:, 2] + bb, -127, 128)
	im[x, y] = color.lab2rgb(val.reshape(len(x), 1, 3)).reshape(len(x), 3)*255

def applyTexture(x, y, texture = texture_input):
	text = imread(texture_input)
	height,width = text.shape[:2]
	xmin, ymin = amin(x),amin(y)
	xmax, ymax = amax(x),amax(y)
	scale = max(((xmax - xmin + 2)/height),((ymax - ymin + 2)/width))
	text = imresize(text, scale)
	# print text.shape[:2]
	# print xmax - xmin +2, ymax - ymin+2
	X = (x-xmin).astype(int)
	Y = (y-ymin).astype(int)
	val1 = color.rgb2lab((text[X, Y]/255.).reshape(len(X), 1, 3)).reshape(len(X), 3)
	val2 = color.rgb2lab((im[x, y]/255.).reshape(len(x), 1, 3)).reshape(len(x), 3)
	L, A, B = mean(val2[:,0]), mean(val2[:,1]), mean(val2[:,2])
	val2[:, 0] = np.clip(val2[:, 0] - L + val1[:,0], 0, 100)
	val2[:, 1] = np.clip(val2[:, 1] - A + val1[:,1], -127, 128)
	val2[:, 2] = np.clip(val2[:, 2] - B + val1[:,2], -127, 128)
	im[x,y] = color.lab2rgb(val2.reshape(len(x), 1, 3)).reshape(len(x), 3)*255

# points = np.loadtxt('nailpoint_5')

x, y = points[:12, 0],points[:12, 1]
x, y = getBoundaryPoints(x, y)
x, y = getInteriorPoints(x, y)
#applyNailPolish(x, y)
applyTexture(x,y)

x, y = points[12:24, 0],points[12:24, 1]
x, y = getBoundaryPoints(x, y)
x, y = getInteriorPoints(x, y)
#applyNailPolish(x, y)
applyTexture(x,y)

x, y = points[24:36, 0],points[24:36, 1]
x, y = getBoundaryPoints(x, y)
x, y = getInteriorPoints(x, y)
#applyNailPolish(x, y)
applyTexture(x,y)

x, y = points[36:48, 0],points[36:48, 1]
x, y = getBoundaryPoints(x, y)
x, y = getInteriorPoints(x, y)
#applyNailPolish(x, y)
applyTexture(x,y)

x, y = points[48:60, 0],points[48:60, 1]
x, y = getBoundaryPoints(x, y)
x, y = getInteriorPoints(x, y)
#applyNailPolish(x, y)
applyTexture(x,y)

x, y = points[60:72, 0],points[60:72, 1]
x, y = getBoundaryPoints(x, y)
x, y = getInteriorPoints(x, y)
#applyNailPolish(x, y)
applyTexture(x,y)

x, y = points[72:84, 0],points[72:84, 1]
x, y = getBoundaryPoints(x, y)
x, y = getInteriorPoints(x, y)
#applyNailPolish(x, y)
applyTexture(x,y)

x, y = points[84:96, 0],points[84:96, 1]
x, y = getBoundaryPoints(x, y)
x, y = getInteriorPoints(x, y)
#applyNailPolish(x, y)
applyTexture(x,y)

x, y = points[96:108, 0],points[96:108, 1]
x, y = getBoundaryPoints(x, y)
x, y = getInteriorPoints(x, y)
#applyNailPolish(x, y)
applyTexture(x,y)

x, y = points[108:, 0],points[108:, 1]
x, y = getBoundaryPoints(x, y)
x, y = getInteriorPoints(x, y)
#applyNailPolish(x, y)
applyTexture(x,y)

figure()
#plot(points[:, 0],points[:, 1],'ro')
imshow(im)
gca().set_aspect('equal', adjustable='box')
imsave('out1.jpg',im)
show()
