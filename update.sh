echo "正在拉取服务器仓库数据"
git fetch origin master
git merge origin/master
read -p "按任意键退出" va