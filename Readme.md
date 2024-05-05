## Dependencies:

* Python 3.7
* Tensorflow 1.15.2
* Keras 2.0.8

## It is highly recommended to create a python virtual environment to install all the dependencies. Here is how you can do it:

* After installing python 3.7.9, install the Virtualenv library and create a virtual encironment.

    * ```pip install virtualenv```
    * ```python3 -m venv myenv```
    * ```myenv\Scripts\activate```

## How to use

* IPython Notebook:

``` Download the notebook and upload Jupyter Notebooks. The rest of the instructions are in the notebook. ```

## To run code on a local machine

* Create a Python virtual environment and install the dependencies using the following command:

``` pip install -r requirements.txt ```

* Use set_regions.py to set the parking regions:

``` python set_regions.py PATH_OF_VIDEO_FILE NAME_OF_OUTPUT_FILE(optional)```

* Use detector.py to get the output:

``` python detector.py PATH_OF_VIDEO_FILE PATH_OF_PARKING_REGIONS_FILE ```


