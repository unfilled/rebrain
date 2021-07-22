#https://www.nginx.com/resources/wiki/start/topics/tutorials/install/
sudo apt update
sudo apt install nginx


sudo apt-get update && sudo apt-get upgrade
sudo apt-get install -y apt-transport-https openjdk-8-jre-headless uuid-runtime pwgen

sudo apt-key adv --keyserver hkp://keyserver.ubuntu.com:80 --recv     9DA31620334BD75D9DCB49F368818C72E52529D4
echo "deb [ arch=amd64 ] https://repo.mongodb.org/apt/ubuntu bionic/mongodb-org/4.0 multiverse" |  sudo tee /etc/apt/sources.list.d/mongodb-org-4.0.list
sudo apt-get update
sudo apt-get install -y mongodb-org

sudo systemctl daemon-reload
sudo systemctl enable --now mongod.service
sudo systemctl status mongod.service
sudo systemctl --type=service --state=active | grep mongod

wget -q https://artifacts.elastic.co/GPG-KEY-elasticsearch -O myKey
sudo apt-key add myKey
echo "deb https://artifacts.elastic.co/packages/oss-6.x/apt stable main" | sudo tee -a /etc/apt/sources.list.d/elastic-6.x.list
sudo apt-get update && sudo apt-get install elasticsearch-oss

sudo nano /etc/elasticsearch/elasticsearch.yml
# Вносим следующие значения:
cluster.name: graylog
action.auto_create_index: false

sudo systemctl daemon-reload
sudo systemctl enable --now elasticsearch.service
sudo systemctl status elasticsearch.service
sudo systemctl --type=service --state=active | grep elasticsearch

wget https://packages.graylog2.org/repo/packages/graylog-3.3-repository_latest.deb
sudo dpkg -i graylog-3.3-repository_latest.deb
sudo apt-get update && sudo apt-get install graylog-server


# Генерируем пароль из 16 символов
pwgen -N 1 -s 16
# Результат записываем 
4U7MawTsmPBCfk66
# Далее сгенерируйте хеш для пароля пользователя admin, указав значение пароля:
echo -n 4U7MawTsmPBCfk66 | sha256sum

72d775c0b6721d6d8311624152970aa2c80efc538da77e4eadb3ca259c16f4c1

sudo nano /etc/graylog/server/server.conf

root_password_sha2 {хэш}
http_bind_address = 192.168.100.2:9000

sudo systemctl daemon-reload
sudo systemctl enable --now graylog-server.service
sudo systemctl status graylog-server.service

sudo less /var/log/graylog-server/server.log