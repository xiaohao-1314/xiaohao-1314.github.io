---
title: js实现计算器
categories: JavaScript
date: 2022-04-13 23:16:24
tags:
  - JavaScript
---
```
<!DOCTYPE html>
<html>
 
<head>
  <meta charset="UTF-8">
  <title>简易计算器</title>
  <style>
    .calc {
      width: 300px;
      height: 400px;
      border: 2px solid #149985;
      border-radius: 10px;
      margin: auto;
      background-color: lightgray;
    }
 
    #btn {
      width: 90%;
      height: 320px;
      margin: 10px auto 0 auto;
      background-color: rgb(238, 234, 234);
    }
 
    #btn button {
      width: 80px;
      height: 35px;
      margin: 15px 0 0 3px;
      background-color: white;
      border: 1px solid #999;
      border-radius: 5px;
      font-size: 18px;
      font-weight: bolder;
    }
 
    #btn button:hover {
      background-color: #999;
      color: white;
      cursor: pointer;
    }
  </style>
</head>
 
<body>
  <div class="calc">
    <!-- 显示数字文本域 -->
    <!-- readonly设置文本域为只读 -->
    <textarea readonly name="" id="text"
      style="width: 90%;height: 30px;display: block;margin: 20px auto 0 auto;font-size: 24px;"></textarea>
    <!-- 键盘按钮 -->
    <div id="btn">
      <button>1</button>
      <button>2</button>
      <button>3</button>
      <button>4</button>
      <button>5</button>
      <button>6</button>
      <button>7</button>
      <button>8</button>
      <button>9</button>
      <button>0</button>
      <button>C</button>
      <button>+</button>
      <button>-</button>
      <button>*</button>
      <button>/</button>
      <button style="width: 98%;">=</button>
    </div>
  </div>
</body>
<script>
  //获取按键区域的元素（键盘）
  var btn = document.getElementById('btn');
  //绑定事件处理函数
  btn.onclick = function (e) {
    //判断只有点击到按钮上才会将信息录入“显示屏”
    if (e.target.nodeName === "BUTTON") {
      //获取文本域元素（显示屏）
      var text = document.getElementById('text');
      //switch 判断当前点击的按钮内容
      switch (e.target.innerHTML) {
        //点击C清空屏幕
        case 'C':
          text.value = '';
          break;
        //如果点击=，获得显示屏中的表达式并计算结果
        case "=":
          var str = text.value;
          //尝试计算显示屏中的内容
          try {
            //将显示屏的内容交给eval做计算，将结果再替换回显示屏中
            text.value = eval(str)
          } catch (err) {
            text.value = err;
          }
          break;
        //点击其他的按钮，将按钮内容追加到显示屏上
        default:
          text.value += e.target.innerHTML;
      }
    }
  }
</script>
</html>
```
### eval函数  
eval() 函数用于计算 JavaScript 字符串，并把它作为脚本代码来执行。如果参数是一个表达式，eval() 函数将执行表达式。如果参数是 Javascript 语句，eval() 将执行 Javascript 语句。所以当我们点击按钮，将表达式写入“显示屏“，该函数便会自动执行计算。  
