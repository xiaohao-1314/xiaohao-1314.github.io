---
title: ES6 let和const命令
date: 2021-05-16 15:05:04
tags: ES6 let和const命令
---
## let命令
1.变量不能重复声明
``` bash
let star='罗志祥';
let star='小猪'  //error
```
2.let有块级作用域，全局，函数，eval
``` bash
{
    let girl='周扬青'
}
console.log(girl) //error
```
不仅仅针对花括号，例如if（）里面

3.不存在变量提前
``` bash
console.log(song)   //error
let song='时间管理大师'
```
<!-- more -->
4.不影响作用域链
``` bash
let school='abc'
function fn(){
    console.log(school) //abc
}
```
案例
``` bash
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Title</title>
</head>
<body>
    <div>
        <div class="item" style="width: 50px;height: 50px;background-color: red"></div>
        <div class="item" style="width: 50px;height: 50px;background-color: red"></div>
        <div class="item" style="width: 50px;height: 50px;background-color: red"></div>
    </div>
    <script>
        let items=document.getElementsByClassName("item");
        for (var i=0;i<items.length;i++){
            items[i].onclick=function (){
                items[i].style.backgroundColor='pink';
            }
        }
        console.log(windows.i)  //3 
        // 当var=3的时候，点击事件开始向外层作用域找，找不到，就是windows.i，此时是3，如果是let i，具有块级作用域，所以每一次触碰事件的i都是不同的。

        //相当于这样
        {
            let i = 0;
                        items[i].onclick=function (){
                items[i].style.backgroundColor='pink';
            }
        }
                {
            let i = 1;
                        items[i].onclick=function (){
                items[i].style.backgroundColor='pink';
            }
        }
                {
            let i = 2;
                        items[i].onclick=function (){
                items[i].style.backgroundColor='pink';
            }
        }
    </script>
</body>
</html>

```

## const命令
声明常量
``` bash
const AA = 'xiaohao'
```
1.一定要赋初始值
2.一般常量使用大写（潜规则）
3.常量的值不能修改
4.也具有块级作用域
``` bash
{
    const pyaler = 'uzi'
}
console.log(player) //error
```
5.对于数组和对象的元素修改，不算作对常量的修改
``` bash
const team = ['uzi','MXLG','Ming','Letme'];
team.push('Meiko'); //不报错，常量地址没有发生变化,值发生改变就会报错

```