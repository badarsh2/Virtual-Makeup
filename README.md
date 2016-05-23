# Virtual-Makeup
A sequel to the existing Virtual Makeup repository https://github.com/srivatsan-ramesh/Virtual-Makeup

Contains Python scripts that provide tweaks to facial features using LAB Color Space.

1. Eyeshadow
------------------
Available face contour points: Eyelid and eyebrow<br>
Approximated points (using the available points): Eye shadow region<br>
Blur & Dilation: Applied using OpenCV

<strong>INPUT</strong><br><br>
<img src="https://raw.githubusercontent.com/badarsh2/Virtual-Makeup/master/eyeshadow/Input.jpg" width="40%"/>
<br><br>
<strong>OUTPUT</strong><br><br>
<img src="https://raw.githubusercontent.com/badarsh2/Virtual-Makeup/master/eyeshadow/out1.jpg" width="40%"/>
<br><br>
2. Foundation
------------------
Available face contour points: Lower face<br>
Approximated points (using the available points with Elliptical Approximation): Upper face<br>
Used Skin Detection Mask to avoid interference with hair
Blur & Dilation: Applied using OpenCV

<strong>INPUT</strong><br><br>
<img src="https://raw.githubusercontent.com/badarsh2/Virtual-Makeup/master/foundation/Input.jpg" width="40%"/>
<br><br>
<strong>OUTPUT</strong><br><br>
<img src="https://raw.githubusercontent.com/badarsh2/Virtual-Makeup/master/foundation/output_1_a.jpg" width="40%"/>
<br><br>
3. Nail Polish
------------------
Available: Nail points & Textures

<strong>INPUT</strong><br><br>
<img src="https://raw.githubusercontent.com/badarsh2/Virtual-Makeup/master/nail/square%26roundLength0.jpg" width="40%"/>
<br><br>
<strong>OUTPUT ( Square Nails )</strong><br><br>
<img src="https://raw.githubusercontent.com/badarsh2/Virtual-Makeup/master/nail/square_1_2.jpg" width="40%"/>
<br><br>
<strong>OUTPUT ( Round Nails )</strong><br><br>
<img src="https://raw.githubusercontent.com/badarsh2/Virtual-Makeup/master/nail/round_2_2.jpg" width="40%"/>
<br><br>
