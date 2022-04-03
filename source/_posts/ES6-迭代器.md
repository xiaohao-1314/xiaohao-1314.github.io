---
title: ES6-迭代器
date: 2021-06-09 17:03:06
tags: ES6 迭代器
---
![alt](one.png)
<!-- more -->
![alt](two.png)
```bash
   <script>
        //声明一个数组
        const xiyou = ['唐僧','孙悟空','猪八戒','沙僧'];
        for(let v in xiyou){ //保存键名
            console.log(v);
        }
        for(let v of xiyou){ //保存键值
            console.log(v);
        }

        let iterator = xiyou[Symbol.iterator]();
        //调用对象的next方法，每次返回value的值，和done的状态
        console.log(iterator.next());//{value: "唐僧", done: false}
        console.log(iterator.next());//{value: "孙悟空", done: false}
        console.log(iterator.next());//{value: "猪八戒", done: false}
        console.log(iterator.next());//{value: "沙僧", done: false}
        console.log(iterator.next());//{value: undefined, done: true}

        //应用
        const banji = {
    name : "终极一班",
    stus: [
        'aa',
        'bb',
        'cc',
        'dd'
    ],
    [Symbol.iterator](){
        let index = 0;
        let _this = this;
        return {
            next: () => {
                if(index < this.stus.length){
                    const result = {value: _this.stus[index],done: false};
                    //下标自增
                    index++;
                    //返回结果
                    return result;
                }else {
                    return {value: underfined,done:true};
                }
            }
        }
    }
}
for(let v of banji){
    console.log(v);  // aa bb cc dd
}
        
    </script>
```