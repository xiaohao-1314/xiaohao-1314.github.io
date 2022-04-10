---
title: Vue3中开发技巧
categories: Vue
date: 2022-04-10 21:50:17
tags:
     - Vue
---
分享7个我在 Vue3 中学习到的一些实用功能小技巧,这些函数具有高度的可重用性，对日常开发很有用。

### 1、判断一个字符串是否以on开头
```
const onRE = /^on[^a-z]/;
const isOn = (key: string) => onRE.test(key);
console.log(isOn('onClick')); // true
console.log(isOn('onclick')); // false
```
我们可以看到它使用了正则匹配。它将匹配以 on 开头且下一个字符不是 a 到 z 的字母。

### 2、确定property是否为自己的
```
const hasOwnProperty = Object.prototype.hasOwnProperty;
const hasOwn = (val: object, key: string | symbol): key is keyof typeof val =>
  hasOwnProperty.call(val, key);
const testObj = { name: 1 };
console.log(hasOwn(testObj, 'name')); // true
Object.getPrototypeOf(testObj).age = 2;
console.log(hasOwn(testObj, 'age')); // false
```
此方法使用 Object.prototype.hasOwnProperty 来确定键是否是对象本身的属性。  
当我们使用 Object.getPrototypeOf() 获取 testObj 的原型并在其上设置 age 属性时，hasOwn 将返回 false。  
除此之外，它在这里使用 TypeScript 的 is 关键字，它创建了一个用户定义的类型保护，在运行时检查以确保它是我们在特定范围内期望的类型。

### 3、判断是否为Promise
此方法借用isObject判断当前值对象，借用isFunction判断当前值的then和catch属性是函数。  
他们三个也都使用 is 关键字。此外，isPromise 还使用泛型来传递 Promise 的 Result 类型。  
```
const isObject = (val: unknown): val is Record<any, any> =>
  val !== null && typeof val === 'object';
const isFunction = (val: unknown): val is Function => typeof val === 'function';
const isPromise = <T = any>(val: unknown): val is Promise<T> => {
  return isObject(val) && isFunction(val.then) &&      isFunction(val.catch);
};
console.log(isPromise(new Promise(() => {}))); // true
console.log(isPromise(async function () {})); // false
console.log(isPromise(function* () {})); // false
```

### 4、判断是否为整数字符串
先用isString判断是否为字符串类型，再判断是否为'NaN'且首字符不是-，最后用空字符串将parseInt转换后的十进制数转为字符串，判断是否为等于原始字符串。  
```
const isString = (val: unknown): val is string => typeof val === 'string';
const isIntegerKey = (key: unknown) =>
  isString(key) &&
  key !== 'NaN' &&
  key[0] !== '-' &&
  '' + parseInt(key, 10) === key;
console.log(isIntegerKey('10')); // true
console.log(isIntegerKey('010')); // false
console.log(isIntegerKey('3.0')); // false
console.log(isIntegerKey('Vue')); // false
```

### 5、缓存字符串计算结果
这是一个高阶函数，内部使用闭包来缓存之前的计算结果，如果再次调用时发现已经计算过，则返回之前的结果。  
```
const cacheStringFunction = <T extends (str: string) => string>(fn: T): T => {
  const cache: Record<string, string> = Object.create(null);
  return ((str: string) => {
    const hit = cache[str];
    return hit || (cache[str] = fn(str));
  }) as any;
};
const getUpperCase = cacheStringFunction((str: string): string =>
  str.toUpperCase(),
);
console.log(getUpperCase('a')); // A
console.log(getUpperCase('a')); // A
```

### 6、连字符转驼峰/驼峰转连字符
以上两种方法都使用正则表达式匹配和使用String.prototype.replace()替换字符，并且都被上一节介绍的缓存函数包裹，也就是说一旦需要处理相同的字符串， 会直接返回缓存结果。  
```
const cacheStringFunction = <T extends (str: string) => string>(fn: T): T => {
  const cache: Record<string, string> = Object.create(null);
  return ((str: string) => {
    const hit = cache[str];
    return hit || (cache[str] = fn(str));
  }) as any;
};
const camelizeRE = /-(\w)/g;
const camelize = cacheStringFunction((str: string): string => {
  return str.replace(camelizeRE, (_, c) => (c ? c.toUpperCase() : ''));
});
const hyphenateRE = /\B([A-Z])/g;
const hyphenate = cacheStringFunction((str: string) =>
  str.replace(hyphenateRE, '-$1').toLowerCase(),
);
console.log(camelize('on-click')); // onClick
console.log(camelize('test-a-click')); // testAClick
console.log(hyphenate('onClick')); // on-click
console.log(hyphenate('testAClick')); // test-a-click
```

### 7、获取当前环境的全局对象
```
let _globalThis: any;
const getGlobalThis = (): any => {
  return (
    _globalThis ||
    (_globalThis =
      typeof globalThis !== 'undefined'
        ? globalThis
        : typeof self !== 'undefined'
        ? self
        : typeof window !== 'undefined'
        ? window
        : typeof global !== 'undefined'
        ? global
        : {})
  );
};
console.log(getGlobalThis());
console.log(getGlobalThis());
```
这里也用到了闭包，但是，这次闭包存储的 _globalThis 是在当前加载的模块中，所以，只需要调用一次，判断一次，不需要后续的判断。  
我们看一下函数内部的逻辑，它的优先级是：  
1.使用 globalThis，它提供了一种跨环境访问全局对象的标准方法。  
2.判断self，这是因为在Web Workers中，无法访问window对象，只能通过self访问当前全局对象。  
3.常见的窗口对象。  
4.Node.js 中的全局对象。  