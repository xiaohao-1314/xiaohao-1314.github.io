---
title: ES6-数值扩展
date: 2021-06-23 12:10:35
tags:  ES6 数值扩展
---
```bash
<script>
   // Number.EPSILON是 JavaScript的最小精度，属性的值接近于 2.22044...E-16
   function equal(a,b){
       if(Math.abs(a-b) < Number.EPSILON){
           return true;
       }else {
           return false;
       }
   }

   console.log(equal(0.1 + 0.2 === 0.3))  //false
   console.log(equal(0.1+0.2,0.3))  //true
```
<!-- more -->
```bash
   //二进制和八进制
   let b = 0b1010; //2进制
   let o = 0o777;  //8进制
   let d = 100;    //10进制
   let x = 0xff;   //16进制
   console.log(x)   //255

   //检测一个数是否为有限数
   console.log(Number.isFinite(100));  //true
   console.log(Number.isFinite(100/0));  //false
   console.log(Number.isFinite(Infinity));  //false

   //检测一个数值是否为NaN
   console.log(Number.isNaN(123))  //false

   //字符串转整数
   console.log(Number.parseInt('5213123love')); //5213123
   console.log(Number.parseFloat('5.123123神器')); //5.123123

   //判断是否为整数
   console.log(Number.isInteger(5));  //true
   console.log(Number.isInteger(2.5)); //false
   
   //将小数部分抹除
   console.log(Math.trunc(3.45345345345)) //3

   //检测一个数到底是正数、负数、还是0
   console.log(Math.sign(100)) //1
   console.log(Math.sign(0))  //0
   console.log(Math.sign(-123)) //-1
</script>
```
