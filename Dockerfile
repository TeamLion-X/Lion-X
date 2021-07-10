FROM MdNoor786/Lion:latest

#clonning repo 
RUN git clone https://github.com/MdNoor786/Lion_X.git /root/Lion

#working directory 
WORKDIR /root/Lion

# Install requirements
RUN pip3 install -U -r requirements.txt

ENV PATH="/home/userbot/bin:$PATH"

CMD ["python3","-m","Lion"]
