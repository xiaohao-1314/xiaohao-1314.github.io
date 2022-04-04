---
title: ES6-class
categories: ES6
date: 2021-06-23 10:27:33
tags:  
     - ES6 
     - class
---
### 定义  
ES6提供了更接近传统语言的写法，引入了Class（类）这个概念，作为对象的模板。通过class关键字，可以定义类。基本上，ES6的class可以看作只是一个语法糖，它的绝大部分功能，ES5都可以做到，新的class写法只是让对象原型的写法更加清晰、更像面向对象编程的语法而已。

```bash
<script>
    class shouji {
        constructor(brand,price) {
            this.brand=brand;
            this.price=price
        }

        call(){
            console.log('我可以打电话')
        }
    }

    let A = new shouji('1+',1999);
    console.log(A)
</script>
```
### 静态成员
```bash
<script>
        //class静态成员
        function phone() {  }
        phone.name = 'shouji';
        phone.change = function () {
            console.log('我可以改变世界');
          }//这两个属于函数对象，不属于实例对象
          phone.prototype.name1 = '小豪';
          let huawei = new phone();
          console.log(huawei.name);//undefined
          console.log(huawei.name1);//小豪

          class Car{
              //静态
              static name = 'haha';
              static change(){
                  console.log("我可以改变世界");
              }
          }
          let car = new Car();
          console.log(car.name);//undefined
          console.log(Car.name);//haha
    </script>
```
### 构造函数继承
```bash
<script>
        //构造函数的继承
        function Phone(brand,price) { 
            this.brand = brand;
            this.price = price;
         }
         Phone.prototype.call = function () {
                console.log("我可以打电话");
              }
              function SmartPhone(brand,price,color,size) {
                  Phone.call(this.brand,price);
                  this.color = color;
                  this.size = size;
                }

            //设置子级构造函数的原型
            SmartPhone.prototype = new Phone;
            SmartPhone.prototype.constructor = SmartPhone;

            //声明子类的方法
            SmartPhone.prototype.photo = function () {
                console.log("我可以拍照");
              }
              SmartPhone.prototype.playGame = function () {
                  console.log("我可以玩游戏");
                }
                const chuizi = new SmartPhone('锤子',2499,'黑色','5.5inch')
                console.log(chuizi);
    </script>
```
### class类继承和重写
```bash
    <script>
        //类的继承
        class Phone{
            //构造方法
            constructor(brand,price){
                this.brand = brand;
                this.price = price;
            }
            //父类成员属性
            call(){
                console.log("我可以打电话");
            }
        }

        class SmartPhone extends Phone{
            //构造方法
            constructor(brand,price,color,size){
                super(brand,price);
                this.color = color;
                this.size = size;
            }
            photo(){
                console.log("拍照");
            }
            playGame(){
                console.log("游戏");
            }
            //重写父类方法
            call(){
                console.log("我可以视频通话");
            }
        }
        const xiaomi = new SmartPhone('小米',799,'黑色','4.7inch');
        console.log((xiaomi));
        xiaomi.call();//我乐意视频通话

    </script>
```