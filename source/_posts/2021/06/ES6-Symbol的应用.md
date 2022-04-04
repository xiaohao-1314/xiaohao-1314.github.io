---
title: ES6-Symbol的应用
categories: ES6
date: 2021-06-03 14:42:43
tags: 
    - ES6 
    - Symbol
---
除了定义自己使用的Symbol值以外，ES6还提供了11个内置的Symbol值，指向语言内部使用的方法
![](./ES6-Symbol%E7%9A%84%E5%BA%94%E7%94%A8/%E5%BE%AE%E4%BF%A1%E5%9B%BE%E7%89%87_20210605110724.png)
![](./ES6-Symbol%E7%9A%84%E5%BA%94%E7%94%A8/%E5%BE%AE%E4%BF%A1%E5%9B%BE%E7%89%87_20210605110750.png)

```bash
class Person {
    static [Symbol.hasInstance](param){
        console.log(param);
        console.log("我被用来检测了")；
        return false;
    }
}
let o = {};
console.log(o instanceof Person); //我被用来检测了，false
```

### 给对象添加方法方式一：
```bash
let game = {
    name : 'ran'
}
let methods = {
    up:Symbol()
    down:Symbol()
}
game[methods.up]=function(){
    console.log('aaa');
}
game[methods.down]=function(){
    console.log('bbb');
}
console.log(game)    // name: 'ran',Symbol(),Symbol()
```

### 给对象添加方法方式二:
```bash
let youxi = {
    name: '狼人杀'，
    [Symbol('say')]:function(){
        console.log('阿萨德')
    }
}
console.log(youxi)    // name:'狼人杀',Symbol(say)
```
