---
title: ES6-rest参数
categories: ES6
date: 2021-06-03 13:52:14
tags: 
     - ES6 
     - rest参数
---
ES6引入rest参数，用于获取函数的实参，用来代替arguments
### 1.首先来看一下ES5获取参数的方式
```bash
            function data(){
            console.log(arguments);
            //获取的是一个对象
        }
        data("xiaohao","ahao","hexo");
```

### 2.ES6使用rest参数
```bash
            function date(...args){
            console.log(args);
        }
        date("xiaohao","ahao","hexo");
        //获取的是一个数组
```
rest参数必须放到参数最后,否则就会报错
```bash
            function fn(a,b,...args) {
            console.log(a);
            console.log(b);
            console.log(args);
          }
          fn(1,2,3,4,5,6,7,8,9);
          //1
          //2
          //[3,4,5,6,7,8,9]
```
rest参数放在a和b中，获取最前面，都会报错。

