# Box_Detection_OpenCV

You are working on a long-range microwave-based communication system. The communication device you are building use mirrors to deflect the microwave in certain directions. You are given an abandoned area to test your device. The area is divided into a grid of m_row,n_col and each cell can house only 1 mirror. The microwave starts from the cell (0,0), reflect from mirrors in different directions and has to exit from the cell (m-1,n-1).  Your task is to develop a small script that keeps tracks of all the visited cell the microwave beam goes to and return the path it took to reach (m-1,n-1 ) cell. If the beam can't reach (m-1,n-1) cell, print -1. An image is given as input which contains a grid of dimension  (m_row*n_col). Further, the grid can only have 2 possible values in them  (/,\). 

"/" denoting a double-sided mirror tilting 45 degrees to the right 

"\" denoting a double-sided mirror tilting 45 degrees to the left

m_row,n_col<100


# Working with the tool
Use the main program by calling the "process" function which returns a list of coordinates traversed by the microwaves. The function takes the image path as a raw string argument. The image must be an excel sheet grid, since template matching is used to detect various objects from the same. In order to use a random grid the use of proper constants and templates must be done in the image_to_matrix file to achieve correct results. 
For the purposes of the given testcases, use the templates as follows:
1. Path of "blank_template" in the templates folder for centre
2. Path of "left_temp" in the templates folder for left
3. Path of "template2" in the templates folder for right

# Future prospect and extension
Since code uses template matching, scaling and random grids often cause a problem, currently working on OCR and box detection using ML models to achieve the same results more efficiently.
