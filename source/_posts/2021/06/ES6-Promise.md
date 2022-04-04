---
title: ES6-Promise
categories: ES6
date: 2021-06-22 18:46:56
tags:
      - ES6 
      - Promise
---
### 什么是promise
定义：Promise是ES6引入的异步编程的新解决方案。语法上 Promise是一个构造函数，用来封装异步操作并可以获取其成功或失败的结果。
```bash
<script>
        const p = new Promise(function (resolve,reject) {
            setTimeout(function () {
                //
                let data = '数据库中用户的数据';
                // 调用resolve,成功
                resolve(data);
                // let err = '数据库读取失败';
                // reject(err)
              },1000);
          });

          //调用promise对象的then方法
          p.then(function (value) { //成功的话调用第一个，失败就调用第二个
            console.log(value);
            },
            function (reason) {
                // console.log(reason);
          })
    </script>
```
### Promise的then()方法
```bash
        <script>
            const p =new Promise((resolve, reject) =>{
                setTimeout(()=>{
                    resolve('用户数据');
                })
            });

        //then（）函数返回的实际也是一个Promise对象
        //1.当回调后，返回的是非Promise类型的属性时，状态为fulfilled，then（）函数的返回值为对象的成功值，如reutnr      123，返回的Promise对象值为123，如果没有返回值，是undefined

        //2.当回调后，返回的是Promise类型的对象时，then（）函数的返回值为这个Promise对象的状态值

        //3.当回调后，如果抛出的异常，则then（）函数的返回值状态也是rejected
            let result = p.then(value => {
                console.log(value)
                // return 123;
                // return new Promise((resolve, reject) => {
                //     resolve('ok')
                // })
                throw 123
            },reason => {
                console.log(reason)
            })
            console.log(result);
        </script>
```
### promise的catch()方法
```bash
<script>
    const p = new Promise((resolve,reject)=>{
        setTimeout(() => {
            reject('失败');
        }, 1000);
    });

    p.then(function (value) {  },function (reason) {
        console.log(reason);
      });
      p.catch(function (reason) { 
          console.warn(reason);
       })
</script>
```

### 使用Promise封装Ajax
```bash
<script>
        //使用原始ajax
        // 1.创建对象
        const xhr = new XMLHttpRequest();
        //2.初始化
        xhr.open("GET","https://api.apiopen.top/getJoke");
        //3.发送
        xhr.send();
        //4.绑定 事件，处理响应结果
        xhr.onreadystatechange = function () {
            if(xhr.readyState === 4){
                //判断响应状态码 200-299
                if(xhr.status >= 200 && xhr.status < 300){
                    //表示成功
                    console.log(xhr.response);
                }else{
                    //如果失败
                    console.error(xhr.status);
                }
            }
          }

        //使用promise封装
        const p = new Promise((resolve,reject)=>{
        // 1.创建对象
        const xhr = new XMLHttpRequest();
        //2.初始化
        xhr.open("GET","https://api.apiopen.top/getJoke");
        //3.发送
        xhr.send();
        //4.绑定 事件，处理响应结果
        xhr.onreadystatechange = function () {
            if(xhr.readyState === 4){
                //判断响应状态码 200-299
                if(xhr.status >= 200 && xhr.status < 300){
                    //表示成功
                    resolve(xhr.response);
                }else{
                    //如果失败
                    reject(xhr.status);
                }
            }
          }
          });
          p.then(function (value) {
              console.log(value);
            },
            function (reason) {
                console.error(reason);
              })
    </script>
```


