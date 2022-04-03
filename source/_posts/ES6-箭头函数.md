---
title: ES6-箭头函数
date: 2021-05-16 22:50:11
tags: ES6 箭头函数
---
ES6允许使用箭头（=>）定义函数,俗称箭头函数
``` bash
       //普通写法
       let fn = function(){
           return a + b;
       }
       //箭头函数写法
        let fn = (a,b) => {
            return a + b;
        }
        let result = fn(1,2);
        console.log(result);
```
### 1.this是静态的，this始终指向函数声明所在作用域下的this的值
``` bash
        function getName() {
            console.log(this.name);
          }
          let getName2 = () =>{
              console.log(this.name);
          }
          //设置window对象的name属性
          window.name = 'xiaohao';
          const shcool = {
              name:'小豪'
          }
          //直接调用
          getName();//xiaohao
          getName2();//xiaohao

          //call方法调用
          getName.call(shcool);//小豪
          getName2.call(shcool);//xiaohao
```
<!-- more -->
### 2.不能作为构造函数
``` bash
           let Person = (name,age) => {
               this.name = name;
               this.age = age;
            }
           let me = new Person('xiaohao',30);
           console.log(me);//报错
```

### 3.不能使用arguments变量
``` bash
           let fn = () => {console.log(arguments);}
           fn(1,2,3);
```

### 4.箭头函数的简写
1)省略小括号，当形参有且只有一个的时候
``` bash
          let add = n => { //let add = (n) => {}
              return n + n;
          }
          console.log(add(9));//18
```
2)省略花括号，当代码体只有一条语句的时候，此时return必须省略
``` bash
          let pow = n => n * n;//let pow = (n) => {return n * n;}
          console.log(pow(9));//81
```

## 箭头函数实践
1)点击div，两秒后背景颜色变为粉色
``` bash
    <style>
        #ad{
            width: 100px;
            height: 100px;
            background: blue;
        }
    </style>

    <div id="ad"></div>

     let ad = document.getElementById('ad');
          ad.addEventListener("click",function () {
              //以前的做法
                //保存this的值
               let _this = this;
               setTimeout(function () {
                   console.log(_this);
                   _this.style.background = 'pink';
                 },2000);

            //使用箭头函数
            //箭头函数指向声明时所在作用域下,this是事件源ad
                setTimeout(()  => {
                  console.log(this);
                  this.style.background = 'pink';
                },2000);
            });
```

2)筛选数组中属于偶数的数
``` bash
 const arr = [1,6,4,23,26,47];
                //以前的做法
            const result = arr.filter(function (item) {
                if(item % 2 === 0){
                    return true;
                    // console.log(result);
                }else{
                    return false;
                }
              });

              //使用箭头函数
              const result = arr.filter(item => item % 2 === 0);
              console.log(result);
```

·箭头函数适合于this无关的回调：定时器，数组的方法回调
·箭头函数不适合与this有关的问题：事件回调，对象的方法
如：
``` bash
             let aq = {
                  name :'nihao',
                  getName: ()=>{
                      this.name;//此时的this指向外层作用域
                      console.log(this.name);
                  }
              }
            aq.getName()
```