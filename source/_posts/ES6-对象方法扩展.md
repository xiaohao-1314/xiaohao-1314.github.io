---
title: ES6-对象方法扩展
date: 2021-06-23 12:25:09
tags:  ES6 对象方法扩展
---
```bash
<script>
        // 1.Object.is 判断两个值是否完全相等
        console.log(Object.is(120,120));//true  和===差不多
        console.log(Object.is(NaN,NaN));//true
        console.log(NaN === NaN);//false

        //2.Object.assign对象的合并
        const config1 = {
            host: 'localhost',
            port: 3306,
            name: 'root',
            pass: 'root',
            test1: 'test'
        };
        const config2 = {
            host: 'http://xiaohao.com',
            port: 33060,
            name: 'xiaohao',
            pass: 'i love you',
            test2: 'test2'
        };
        console.log(Object.assign(config1,config2));//如果同名的话，后面的对象会覆盖前面的对象
        //3.Object.setPrototypeOf 设置原型对象 Object.getPrototypeof
        const school = {
        name:'小豪'
    }
    const cities = {
        xiaoqu:['北京','上海','广州']
    }
    Object.setPrototypeOf(school,cities)
    console.log(Object.getPrototypeOf(school))  //{xiaoqu: Array(2)}
    console.log(school)  //{name: "小豪"}
    </script>
```