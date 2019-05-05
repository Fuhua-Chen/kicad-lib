echo "正在拉取服务器仓库数据"
git fetch --all && git reset --hard origin/master && git pull
read -p "按任意键退出" var