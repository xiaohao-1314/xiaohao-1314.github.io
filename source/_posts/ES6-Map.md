---
title: ES6-Map
date: 2021-06-23 10:17:04
tags:  ES6 Map
---
### 定义
ES6提供了Map数据结构。它类似于对象，也是键值对的集合。但是“键”的范围不限于字符串，各种类型的值（包括对象）都可以当作键。Map也实现了iterator接口，所以可以使用『扩展运算符』和「for…of…』进行遍历。Map的属性和方法。

```bash
    <script>
        let m = new Map();
        m.set("name","xiaohao");
        m.set("change",function () {
            console.log("nihao");
          });
        let key = {
            shcool:'huaguang'
        };
        m.set(key,['北京','上海','广州']); //可以把对象当作一个键s
          console.log(m);

          //size
          console.log(m.size);

          //delete
          m.delete('name');//根据键名删除

          //获取
          console.log(m.get('change'));
          console.log(m.get(key));

          //清空
        //   m.clear();

          //遍历
          for(let v of m){
              console.log(v);
          }
    </script>
```