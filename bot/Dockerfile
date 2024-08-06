FROM nickgryg/alpine-pandas

WORKDIR /usr/src/bot

COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

EXPOSE 8080:5432

CMD [ "python", "./bot.py" ]