FROM python:3.10

RUN apt-get update
RUN yes | apt-get install texlive-fonts-recommended
RUN yes | apt-get install dvipng
RUN apt-get install nano

RUN pip install pdflatex
RUN pip install PyLaTeX

RUN pip install latex_python2025_task

COPY mug.png /data/mug.png
COPY main.py /data/main.py
WORKDIR /data
RUN python main.py

CMD ["/bin/sh", "-c", "bash"]

