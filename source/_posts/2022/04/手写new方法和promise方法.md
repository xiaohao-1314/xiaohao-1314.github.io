---
title: 手写new方法和promise方法
date: 2022-04-05 17:05:57
categories: JavaScript
tags:
     - JavaScript 
---
### 手写new方法
```
function parent() {
    this.name = "xiaohao"
}
parent.prototype = {
    walk: function () {
        console.log("walk")
    }
}
function newfn(fn) {
    if (typeof fn != 'function') {
        return;
    }
    let son = {}
    fn.call(son)
    fn.prototype.constructor = fn;
    son.__proto__ = fn.prototype;
    return son;
}
let son1 = newfn(parent);
son1.walk();
```

### 手写promise方法
```
class promise {
    construtctor(executor) {
        this.state = "pedding"
        this.value = null;
        this.reason = null;
        this.onFulfilledCallBack = []
        this.onRejectedCallBack = []

        function resolve(value) {
            if (this.state == "pedding") {
                this.state = "fulfilled"
                this.value = value
                this.onFulfilledCallBack.foreach(item => item(this.value))
            }
        }
        function reject(reason) {
            if (this.state == "pedding") {
                this.state = "rejected"
                this.reason = reason;
                this.onRejectedCallBack.foreach(item => item(this.reason))
            }
        }
        try {
            executor(resolve, reject)
        } catch (error) {
            reject(error)
        }
    }
    then(onFulfilled, onRejected) {
        if (this.state == "fulfilled") {
            return new promise((resolve, reject) => {
                onFulfilled(this.value)
            })
        }
        if (this.state == "rejected") {
            return new promise((resolve, reject) => {
                onRejected(this.reason)
            })
        }
        if (this.state == "pedding") {
            return new promise((resolve, reject) => {
                this.onFulfilledCallBack.push(onFulfilled)
                this.onRejectedCallBack.push(onRejected)
            })
        }
    }
}
```