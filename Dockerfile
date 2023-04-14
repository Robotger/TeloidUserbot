
FROM erdembey/epicuserbot:latest
RUN git clone https://github.com/RobotgerDev/TeloidUserBot /root/TeloidUserBot
WORKDIR /root/TeloidUserBot/
RUN pip3 install -r requirements.txt
CMD ["python3", "teloid.py"]  
