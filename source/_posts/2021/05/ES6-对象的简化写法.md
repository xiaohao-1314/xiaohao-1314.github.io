---
title: ES6-对象的简化写法
categories: ES6
date: 2021-05-16 22:41:04
tags: 
     - ES6 
     - 对象的简化写法
---
### ES6允许在大括号里面，直接写入变量和函数，作为对象的属性和方法  
``` bash
        let name = 'aaa';
        let change = function(){
            console.log('aaa');
}
        const school = {
            name,
            change,
            improve(){
                consolg.log('bbb');
            }
                //相当于
                //improve:function(){
                // console.log('bbb');
                // }
}
console.log(school.improve);
```