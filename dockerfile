FROM python:3

RUN git clone https://github.com/santidotpy/palindromos.git

WORKDIR /palindromos

RUN pip install -r requirements.txt

CMD ["python3", "test_palindromos.py"]