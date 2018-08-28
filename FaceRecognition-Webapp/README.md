1) Create a virtual env. It is ok to create in your checkout. The directory "venv" is listed in ".gitignore" file.

`python3 -m venv venv`

2) Activate the virtual environment

`source venv/bin/activate`

3) Install packages

`pip3 install flask flask_restful numpy dlib`

4) Setup opencv into the new virtual environment. Do equivalent of the following for your setup:
`cd venv/lib/python3.6/site-packages/`
`ln -s /usr/local/lib/python3.6/dist-packages/cv2.cpython-36m-x86_64-linux-gnu.so`
`cd -`

5) Start Flask

`flask  run --host=0.0.0.0`

6) To enable webcam on Chrome
`/Applications/Google\ Chrome.app/Contents/MacOS/Google\ Chrome --user-data-dir=/tmp/foo --unsafely-treat-insecure-origin-as-secure=http://0.0.0.0:5000`

7) Browse the html file From you browser browse to `http://<hostname or ip address or localhost>:5000/demo.html`. Do NOT use file system based click on the file. The HTML and JS files etc are also conifgured to be stread from the server as files.

8) Enter data into the demo.

