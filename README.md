### quiet主题的文档
    https://gitee.com/liershuang/hexo-theme-quiet-ext
### hexo运行命令
    1.hexo clean
    2.hexo d 或 hexo deploy
    3.hexo g
    4.hexo server
ps:记得先安装hexo-deployer-git  
     npm install --save hexo-deployer-git
### 可能遇到的问题
#### github超时
     $ git config --global http.proxy http://127.0.0.1:1080  
     $ git config --global https.proxy http://127.0.0.1:1080  
     $ git config --global --unset http.proxy  
     $ git config --global --unset https.proxy  
    
#### Git :fatal: refusing to merge unrelated histories解决
     git pull origin master --allow-unrelated-histories

#### nodejs版本 安装n模块报错 npm ERR! code EBADPLATFORM
     先将生成的node_modules文件夹删除，再运行npm install --force即可
 