# install fluentd
curl -L https://calyptia-fluentd.s3.us-east-2.amazonaws.com/calyptia-fluentd-1-ubuntu-focal.sh | sh

# install loggly-gem
sudo /opt/td-agent/bin/fluent-gem install fluent-plugin-loggly