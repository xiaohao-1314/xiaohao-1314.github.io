---
title: ES6-集合
categories: ES6
date: 2021-06-22 20:59:58
tags:  
     - ES6 
     - 集合
---
### 定义
ES6提供了新的数据结构set(集合）。它类似于数组，但成员的值都是唯一的，集合实现了iterator接口，所以可以使用「扩展运算符』和「 for…of…』进行遍历，集合的属性和方法: 

· size返回集合的元素个数  
· add增加一个新元素，返回当前集合  
· delete删除元素，返回boolean值has检测集合中是否包含某个元素，返回boolean值  

```bash
<script>
    let s = new Set();
    let s2 = new Set(['1','2','3','4','5']);
    //元素个数
    console.log(s2.size);//5
    //添加新的元素
    s2.add('6'); //Set(5) {"1", "2", "3", "4", "5","6"}
    //删除元素
    s2.delete('5');
    console.log(s2); //Set(5) {"1", "2", "3", "4","6"}
    //检测
    console.log(s2.has('6')); //true
    //清空
    s2.clear();
    console.log(s2);

    //实现了iterator接口，可以使用for of遍历元素
    for(v of s2){
        console.log(v);
    }
```
### 集合的应用
```bash
    let arr = [1,2,3,4,5,4,3,2,1];
    //1.数组去重
    // let result = [...new Set(arr)];
    //2.交集
    let arr2 = [4,5,6,5,6];
    let result = [...new Set(arr)].filter(item=>{
        let s2 = new Set(arr2);
        if(s2.has(item)){
            return true;
        }else{
            return false;
        }
    });
    //简化
    // let result = [...new Set(arr)].filter(item=>new Set(arr2).has(item));
    console.log(result);

    //3.并集
    let union = [...new Set([...arr,...arr2])];
    console.log(union);

    //4.差集
    let diff = [...new Set(arr)].filter(item=>!(new Set(arr2).has(item)));
    console.log(diff);
</script>
```
