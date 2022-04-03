---
title: ES6-扩展运算符
date: 2021-06-03 14:05:39
tags: ES6 扩展运算符
---
### [..]扩展运算符能将[数组]转换为逗号分隔的[参数序列]
```bash
        //声明一个数组...
        const tfboys = ['易烊千玺','王源','王俊凯'];
        
        //声明一个函数
        function wang() {
            console.log(arguments);
          }
          wang(tfboys);//0: (3) ["易烊千玺", "王源", "王俊凯"] 只有一个
          wang(...tfboys);
        //   0: "易烊千玺"
        //   1: "王源"
        //   2: "王俊凯"
```
### 扩展运算符的应用
1)数组的合并
<!-- more -->
```bash
        const kuaizi = ['王太利','肖央'];
        const fenghuang = ['曾毅','玲花'];
        //以前的做法就是concat()
        // const zuixuanxiaopingguo = kuaizi.concat(fenghuang);

        //但现在可以使用扩展运算符
        const  zuixuanxiaopingguo = [...kuaizi,...fenghuang];
        console.log(zuixuanxiaopingguo);//['王太利','肖央','曾毅','玲花']
```

2)数组克隆
```bash
        const sanzhihua = ['E','G','M'];
        const sanyecao = [...sanzhihua];
        console.log(sanyecao);//['E','G','M']
```

3)将伪数组转为真正的数组
```bash 
<body>
    <div></div>
    <div></div>
    <div></div>
    <script>
        const divs = document.querySelectorAll('div');
        const divArr = [...divs];
        console.log(divArr);//[div,div,div] 变成真正的数组    
    </script>
</body>
```


