[![Build Status](https://travis-ci.com/Milan-36/PythonCalculator-UsingTravis.svg?branch=master)](https://travis-ci.com/Milan-36/PythonCalculator-UsingTravis)


# PythonCalculator

This is **Project 2** of **IS 601**. A Python program using principles of automated testing.

## Description:
* The calculator is one application that we all use in our day to day lives. This **PythonCalculator** is a Python program using principles of automated testing.
* It performs basic arithmetic operations. I Learned to use static methods, object methods, object attributes/properties.
* And also used the CSV files to load data for unit tests. There's each file to test the associated operation.
* Also used Travis CI in this project. IT is a hosted continuous integration service used to build and test software projects hosted on GitHub.

## Arithmetic Operations:
* [Addition](https://github.com/Milan-36/PythonCalculator-UsingTravis/blob/master/src/Calculator/Addition.py),
* [Subtraction](https://github.com/Milan-36/PythonCalculator-UsingTravis/blob/master/src/Calculator/Subtraction.py),
* [Multiplication](https://github.com/Milan-36/PythonCalculator-UsingTravis/blob/master/src/Calculator/Multiplication.py),
* [Division](https://github.com/Milan-36/PythonCalculator-UsingTravis/blob/master/src/Calculator/Division.py),
* [Square](https://github.com/Milan-36/PythonCalculator-UsingTravis/blob/master/src/Calculator/Square.py),
* [Square root](https://github.com/Milan-36/PythonCalculator-UsingTravis/blob/master/src/Calculator/Square_Root.py)

## Statistics Operations:
* Mean
* Median
* Mode
* Variance
* Standard Deviation 

## Resources required  to run the Unit tests are,

* [Calculator.py](https://github.com/Milan-36/PythonCalculator-UsingTravis/blob/master/src/Calculator/Calculator.py) (It contians all python function to perform arithmetic operations).
* [test_Calculator.py](https://github.com/Milan-36/PythonCalculator-UsingTravis/blob/master/src/UnitTests/test_Calculator.py) (Unit Test file to perfom individual tests of Arithmetic Operations on source code).
* [Statistics.py](https://github.com/Milan-36/PythonCalculator-UsingTravis/blob/master/src/Statistics/Statistics.py) (It contians all python function to perform Statistics operations).
* [test_statistics.py](https://github.com/Milan-36/PythonCalculator-UsingTravis/blob/master/src/UnitTests/test_statistics.py) (Unit Test file to perfom individual tests of Statistics Operations on source code).
* [CSVReader.py](https://github.com/Milan-36/PythonCalculator-UsingTravis/blob/master/src/CsvReader/CSVReader.py) (To read the csv file and convert the data into list, and dictionary to store in memory.).
* [StaticVariables.py](https://github.com/Milan-36/PythonCalculator-UsingTravis/blob/master/src/StaticProperties/Static_Variables.py) (To refer to the common property of all objects).
* [CSV Data File](https://github.com/Milan-36/PythonCalculator-UsingTravis/tree/master/src/UnitTests/data) (comma-separated values files are used to read and test data in Unit Tests).



## Example #1:
### Unit Test for the addition:
![Addition_code](https://github.com/Milan-36/PythonCalculator-UsingTravis/blob/master/src/Screenshot/Add_method.png)

### Output of Unit Test for addition (Run in Docker):
![Addition_run](https://github.com/Milan-36/PythonCalculator-UsingTravis/blob/master/src/Screenshot/Add_output.png)


## Example #2:
### Unit Test for the squart root:
![Addition_code](https://github.com/Milan-36/PythonCalculator-UsingTravis/blob/master/src/Screenshot/sqrt_method.png)

### Output of Unit Test for squart root (Run in Docker):
![Addition_run](https://github.com/Milan-36/PythonCalculator-UsingTravis/blob/master/src/Screenshot/sqrt_output.png)
