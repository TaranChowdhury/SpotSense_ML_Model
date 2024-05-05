# Dependencies:

* Python 3.7
* Tensorflow 1.15.2
* Keras 2.0.8

# How to use

* IPython Notebook:

``` Download the notebook and open it using Jupyter Notebooks Extension on VS code. The rest of the instructions are in the notebook. ```

# To run code on a local machine

* It is highly recommended to create a Python virtual environment to install all the dependencies. Here is how you can do it:

## Create a Python virtual environment using the following command:
* ```pip install virtualenv```
* ```python3 -m venv myenv```
* ```myenv\Scripts\activate```

* Note: make sure to install Python3.7.9 before creating the virtual environment.

## Install the dependencies using the following command:

``` pip install -r requirements.txt ```

* Note: make sure that your virtual environment is selected as the kernel currently running on Jupyter Notebook in VS Code.

* Use ParkingMaskCreator.py to set the parking regions:
    * You can update the following Paths before running the script to experiment with other videos:
        * ```videoPath: path to the video whose mask you want to create.```
        * ```savePath: saves the region mask to the specified location```

* Use detector.py to get the output:
``` python detector.py PATH_OF_VIDEO_FILE PATH_OF_PARKING_MASK_FILE ```

# The Training and output videos and the parking region masks are in the ```Drive link Training_&_output Video.txt``` file.
