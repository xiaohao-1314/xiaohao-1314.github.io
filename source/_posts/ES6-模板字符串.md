---
title: ES6-模板字符串
date: 2021-05-16 22:34:24
tags: ES6 模板字符串
---
### 1.声明
``` bash
        let str = `这么巧，我也是一个字符串！`;
        console.log(str,typeof str);
```
    
### 2.内容中可以直接出现换行符
在使用append时，就知道有多算爽了
注意：使用的是``,TAB键上面那个符号
``` bash
        let ul = `<ul>
			        <li>xiaohao</li>
			        <li>小豪</li>
                    <li>小豪豪</li>
                    <li>宝贝</li>
		          </ul>`
        console.log(ul);
```

### 3.拼接字符串
``` bash
        let name = '小豪';
        let out = `${name}是最帅的`;
        console.log(out);
```
<!-- more -->