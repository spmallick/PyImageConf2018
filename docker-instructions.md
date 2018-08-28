# Docker Image Instructions

To use the docker image, use the following instructions:

For **OpenCV-3.4.1** and **Flask application for face recognition**:
`docker pull vishwesh5/cv-docker:withFlask`

`docker run -it -p 8888:8888 -p 5000:5000 vishwesh5/cv-docker:withFlask`

To run **Flask application for face recognition**:
`source activate OpenCV-3.4.1-py3`
`cd /home/jovyan/work/face-recognition-web-app`
`flask run --host=0.0.0.0`

Open your web browser, browse to `http://0.0.0.0:5000/demo.html` and follow the given instructions.
To enable webcam on Chrome (**change the path as required**):
`/Applications/Google\ Chrome.app/Contents/MacOS/Google\ Chrome --user-data-dir=/tmp/foo --unsafely-treat-insecure-origin-as-secure=http://0.0.0.0:5000`

To run **jupyter-notebook**:
`jupyter-notebook`

Open your web browser, browse to `http://0.0.0.0:8888` and use the token present in the log.

To use Python environments:

`source activate OpenCV-3.4.1-py2`
`ipython`
`import cv2`
`cv2.__version__`
`exit()`
`source deactivate`

Similarly for Python 3.6,

`source activate OpenCV-3.4.1-py3`
`ipython`
`import cv2`
`cv2.__version__`
`exit()`
`source deactivate`

The image also has **dlib** installed for both Python environments. 

`source activate OpenCV-3.4.1-py2`
`ipython`
`import dlib`
`dlib.__version__`
`exit()`
`source deactivate`
