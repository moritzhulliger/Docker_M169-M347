sudo yum update -y

sudo yum install docker -y
sudo systemctl enable docker
sudo systemctl start docker
sudo docker version

sudo yum install curl
sudo curl -L "https://github.com/docker/compose/releases/latest/download/docker-compose-$(uname -s)-$(uname -m)" -o /usr/local/bin/docker-compose
sudo chmod +x /usr/local/bin/docker-compose
docker-compose --version

    docker swarm join --token SWMTKN-1-0p3tnr4ycekftgg6bcv9su8k3c25fkw8tq1iop7i3wx24vetl6-2bpqxm0mrivf11r790z9iok7q 172.31.84.210:2377