---
title: ES6-变量的解构赋值
date: 2021-05-16 22:26:17
tags:  ES6 变量的解构赋值
---
定义：ES6 允许按照一定模式从数组和对象中提取值，对变量进行赋值，这被称为解构赋值.

### 数组的解构
``` bash
        const happy = ['aa','bb','cc','dd'];
        let [a,b,c,d] = happy;
        console.log(a); //aa
        console.log(b); //bb
        console.log(c); //cc
        console.log(d); //dd
```

### 对象的解构
<!-- more -->
``` bash
        const zhao = {
            name:'赵本山',
            age:'不详',
            xiaoping: function(){
                console.log('我可以演很多的小品');
            }
        }
        let {name,age,xiaoping} = zhao;
        console.log(xiaoping); //ƒ (){console.log('我可以演很多的小品');}
        console.log(name); //赵本山
        console.log(age); //不详
        xiaoping(); //我可以演很多小品
```