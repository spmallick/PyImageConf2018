pip3 install --upgrade pip
pip3 install jupyter

These 2 should work. In case if the user wants to use jupyterhub too, they can do:

pip3 install jupyterhub

To install any kernel for a particular environment:
Activate the environment:
pip3 install ipykernel
python -m ipykernel install --name <kernel name> --user

To check the kernel list to verify the kernel has been installed:

jupyter-kernelspec list
