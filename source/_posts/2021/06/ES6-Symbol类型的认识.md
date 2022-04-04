---
title: ES6-Symbol类型的认识
categories: ES6
date: 2021-06-03 14:42:43
tags: 
    - ES6 
    - Symbol
---
### 什么是Symbol
ES6引入了一种新的原始数据类型Symbol，表示独一无二的值，它是javascript语言的第七种数据类型，是一种类似于字符串的数据类型。  
Symbol特点
1）Symbol值是唯一的，用来解决命名冲突的问题  
2) Symbol值不能与其他数据进行运算  
3) Symbol定义的对象属性不能使用for..in循坏遍历，但是可以使用Reflect.ownKeys来获取对象的所有键名
```
 //创建Symbol
        let s = Symbol();
        console.log(s,typeof s);

        //第一种方式
        let s2 = Symbol('小豪');
        let s3 = Symbol('小豪');
        console.log(s2 == s3);//false

        //第二种方式 对象
        let s4 = Symbol.for('小豪');
        let s5 = Symbol.for('小豪');
        console.log(s4 == s5);//true

        //不能与其他数据进行运算
        let result = s + 100;//报错

        //js七种数据类型
        // u  undefined
        // s  Symbol String
        // o  object
        // n  null number
        // b  boolean
```
Symbol 值作为属性名时，该属性是公有属性不是私有属性，可以在类的外部访问。但是不会出现在 for...in 、 for...of 的循环中，也不会被 Object.keys() 、 Object.getOwnPropertyNames() 返回。如果要读取到一个对象的 Symbol 属性，可以通过 Object.getOwnPropertySymbols() 和 Reflect.ownKeys() 取到。
```
        let sy = Symbol("key1");
                let syObject = {};
        syObject[sy] = "kk";
        console.log(syObject);
        
        for (let i in syObject) {
          console.log(i);
        }    // 无输出
        
        Object.keys(syObject);                     // []
        Object.getOwnPropertySymbols(syObject);    // [Symbol(key1)]
        Reflect.ownKeys(syObject);                 // [Symbol(key1)]
```
Symbol.for()
Symbol.for() 类似单例模式，首先会在全局搜索被登记的 Symbol 中是否有该字符串参数作为名称的 Symbol 值，如果有即返回该 Symbol 值，若没有则新建并返回一个以该字符串参数为名称的 Symbol 值，并登记在全局环境中供搜索。
```bash
        let yellow = Symbol("Yellow");
        let yellow1 = Symbol.for("Yellow");
        yellow === yellow1;      // false
        
        let yellow2 = Symbol.for("Yellow");
        yellow1 === yellow2;     // true
```

Symbol.keyFor() 返回一个已登记的 Symbol 类型值的 key ，用来检测该字符串参数作为名称的 Symbol 值是否已被登记。
```bash
        let yellow1 = Symbol.for("Yellow");
        Symbol.keyFor(yellow1);    // "Yellow"
```