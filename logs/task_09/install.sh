# sudo apt update
# sudo apt install nginx
# nano /etc/nginx/sites-enabled/default full log paths
# curl -L https://toolbelt.treasuredata.com/sh/install-ubuntu-focal-td-agent4.sh | sh

# kafka config: listener: PLAINTEXT..ip:9092

listeners=PLAINTEXT://10.114.0.4:9092

advertised.listeners=PLAINTEXT://10.114.0.4:9092

раскомментировать listener.security.protocol.map=


#curl -XDELETE localhost:9200/logstash-2021.07.19
#bin/kafka-console-consumer.sh --bootstrap-server 10.114.0.4:9092 --topic topic --from-beginning
