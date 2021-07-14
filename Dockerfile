FROM python:3

ADD . .

RUN pip install --upgrade pip
RUN pip install -r requirements.txt

# Run in python, module(-m) unittest and option for discover, and set the folder file(-s) to find the Unit Test
CMD ["python", "-m", "unittest", "discover", "-s", "./src/UnitTests"]