FROM python:3.8

RUN mkdir /laismo-bot
COPY . /laismo-bot
WORKDIR /laismo-bot
RUN pip install --upgrade pip &&\
    pip install --user -r requirements.txt
RUN touch stats.json &&\
    echo "{}" > stats.json
CMD [ "python", "main.py" ]
