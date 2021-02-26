FROM python:3
ADD pybar.py /
RUN pip install pyStrich
RUN pip install RandomWords
CMD ["python","./pybar.py"]