#-------------------------------------------------------------------------
#
# Makefile for 4bits
#
# auther:
# 	"张连壮" <lianzhuangzhang@yunify.com>
# 	"颜博" <jerryyan@yunify.com>
#
# Date:
# 	2023.04
#
#-------------------------------------------------------------------------
FILEDESC = "4bits.cn"

all: web-image kubectl-image compose

web-image:
	/bin/rm -rf  ./server/webserver/web
	cp -rf ./web ./server/webserver/web
	cp -rf ./config.json ./server/webserver/config.json
	cd ./server/webserver/; \
		docker build -t `jq -r '.web_image' config.json` .

kubectl-image:
	cp -rf ./config.json ./server/kubectl/1.21/config.json
	cd ./server/kubectl/1.21/; \
		docker build -t `jq -r '.kubectl_image' config.json` .

compose:
	cp config.json ./server/versions.json
	cp jq-template.awk ./server/jq-template.awk
	cd ./server/; \
		awk -f jq-template.awk docker-compose.template.yaml > docker-compose.yaml
	cp config.json ./server/compose-configs/nginx/templates/versions.json
	cp jq-template.awk ./server//compose-configs/nginx/templates/jq-template.awk
	cd ./server/compose-configs/nginx/templates; \
		awk -f jq-template.awk default.conf.template.conf > default.conf.template
