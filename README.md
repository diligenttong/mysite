# mysite
git和github演示项目

## 说明
git是一个开源的分布式版本控制系统，可以有效、高速地处理从很小到非常大的项目版本管理.
1.在github里创建一个仓库
2.在gitbash中敲命令：git clone+加你仓库HTTPS地址
3.把你项目里的文件复制到仓库里去，在gitbash中敲命令：git status 查看仓库状态
4.git add . 把编辑区的文件放到寄存区中  添加代码
5.vim .gitignore    :wq保存并退出vim编译器，用sublime打开忽略文件，添加settings，缓冲文件等敏感的文件，git reset之后可以重复3，4步
6.git commit -m '初始化项目'  提交代码，‘’里面是描述
7.git push 将项目推送到github中去
git pull 将在github中更改的内容更新到本地上去
git log 查看日志
