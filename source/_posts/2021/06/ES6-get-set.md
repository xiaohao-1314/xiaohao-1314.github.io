---
title: ES6-get/set
categories: ES6
date: 2021-06-23 10:48:25
tags:  
      - ES6 
      - get/set
---
```bash
<script>
        //get和set
        class Phone{
            get price(){
                console.log("价格属性被读取");
                return 'xiaohao';
            }
            set price(newval){
                console.log("价格属性被修改");
            }
        }
        //实例化对象
        let s = new Phone();
        console.log(s.price);
        s.price = 'free';
    </script>
```