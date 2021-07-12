FROM python:3

ADD src /src

RUN pip install --upgrade pip

# Run in python, module(-m) unittest and option for discover, and set the folder file(-s) to find the Unit Test
CMD ["python", "-m", "unittest", "discover", "-s", "./src/UnitTests"]