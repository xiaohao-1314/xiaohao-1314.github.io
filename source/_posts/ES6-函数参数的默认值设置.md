---
title: ES6-函数参数的默认值设置
categories: ES6
date: 2021-06-01 23:16:37
tags: 
     - ES6 
     - 函数参数的默认值设置
---
### ES6 允许给函数参数赋值初始值
### 1.形参初始值  具有默认值的参数，一般位置要靠后(潜规则)
```bash
            function add(a,b,c = 10) {
                return a + b + c;
              }
              let result = add(1,2);
              console.log(result);//13
            //如果把c放在a和b中间，b就会没有赋值，打印的是NAN
```

### 2.与解构赋值结合
```bash
            function connect({host,username,password,port}) {
                // console.log(option.username);//xiaohao
                // console.log(option.password);//123456
                //如果这样写，每次都要调用option，麻烦，可以直接使用解构赋值
                console.log(host);//127.0.0.1
                console.log(username);//xiaohao
                console.log(password);//123456
                console.log(port);//3306

                //形参可以写成host="127.1.1.1"默认值,如果实参没有host
                //那console.log(host)就会打印默认值，否则就打印实参
              }
              connect({
                  host:'127.0.0.1',
                  username:'xiaohao',
                  password:'123456',
                  port:3306
              })
```