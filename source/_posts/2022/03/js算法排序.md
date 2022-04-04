---
title: js算法排序
categories: JavaScript
date: 2022-03-28 14:56:38
tags:
     - JavaScript
---
js算法排序可视化网站：链接: [https://visualgo.net](https://www.csdn.net/)
# 冒泡排序
```
function BubbleSort(array) {
  var length = array.length;
  for (var i = length - 1; i > 0; i--) { //用于缩小范围
    for (var j = 0; j < i; j++) { //在范围内进行冒泡，在此范围内最大的一个将冒到最后面
      if (array[j] > array[j+1]) { 
        var temp = array[j];
        array[j] = array[j+1];
        array[j+1] = temp;
      }
    }
    console.log(array);
    console.log("-----------------------------");
  }
  return array;
}
var arr = [10,9,8,7,7,6,5,11,3];
var result = BubbleSort(arr);
console.log(result); 
/*
[ 9, 8, 7, 7, 6, 5, 10, 3, 11 ]
-----------------------------
[ 8, 7, 7, 6, 5, 9, 3, 10, 11 ]
-----------------------------
[ 7, 7, 6, 5, 8, 3, 9, 10, 11 ]
-----------------------------
[ 7, 6, 5, 7, 3, 8, 9, 10, 11 ]
-----------------------------
[ 6, 5, 7, 3, 7, 8, 9, 10, 11 ]
-----------------------------
[ 5, 6, 3, 7, 7, 8, 9, 10, 11 ]
-----------------------------
[ 5, 3, 6, 7, 7, 8, 9, 10, 11 ]
-----------------------------
[ 3, 5, 6, 7, 7, 8, 9, 10, 11 ]
-----------------------------
[ 3, 5, 6, 7, 7, 8, 9, 10, 11 ]
*/
```

# 选择排序
```
function SelectionSort(array) {
  var length = array.length;
  for (var i = 0; i < length; i++) { //缩小选择的范围
    var min = array[i]; //假定范围内第一个为最小值
    var index = i; //记录最小值的下标
    for (var j = i + 1; j < length; j++) { //在范围内选取最小值
      if (array[j] < min) {
        min = array[j];
        index = j;
      }
    }
    if (index != i) { //把范围内最小值交换到范围内第一个
      var temp = array[i];
      array[i] = array[index];
      array[index] = temp;
    }
    console.log(array);
    console.log("---------------------");
  }
  return array;
}

var arr = [ 1, 10, 100, 90, 65, 5, 4, 10, 2, 4 ];
var result = SelectionSort(arr);
console.log(result);
/*
[ 1, 10, 100, 90, 65, 5, 4, 10, 2, 4 ]
---------------------
[ 1, 2, 100, 90, 65, 5, 4, 10, 10, 4 ]
---------------------
[ 1, 2, 4, 90, 65, 5, 100, 10, 10, 4 ]
---------------------
[ 1, 2, 4, 4, 65, 5, 100, 10, 10, 90 ]
---------------------
[ 1, 2, 4, 4, 5, 65, 100, 10, 10, 90 ]
---------------------
[ 1, 2, 4, 4, 5, 10, 100, 65, 10, 90 ]
---------------------
[ 1, 2, 4, 4, 5, 10, 10, 65, 100, 90 ]
---------------------
[ 1, 2, 4, 4, 5, 10, 10, 65, 100, 90 ]
---------------------
[ 1, 2, 4, 4, 5, 10, 10, 65, 90, 100 ]
---------------------
[ 1, 2, 4, 4, 5, 10, 10, 65, 90, 100 ]
---------------------
[ 1, 2, 4, 4, 5, 10, 10, 65, 90, 100 ]
*/
```

# 插入排序
```
function InsertionSort(array) {
  var length = array.length;
  for (var i = 0; i < length - 1; i++) {
    //i代表已经排序好的序列最后一项下标
    var insert = array[i+1];
    var index = i + 1;//记录要被插入的下标
    for (var j = i; j >= 0; j--) {
      if (insert < array[j]) {
        //要插入的项比它小，往后移动
        array[j+1] = array[j];
        index = j;
      }
    }
    array[index] = insert;
    console.log(array);
    console.log("-----------------------");
  }
  return array;
}

var arr = [100,90,80,62,80,8,1,2,39];
var result = InsertionSort(arr);
console.log(result);
/*
[ 90, 100, 80, 62, 80, 8, 1, 2, 39 ]
-----------------------
[ 80, 90, 100, 62, 80, 8, 1, 2, 39 ]
-----------------------
[ 62, 80, 90, 100, 80, 8, 1, 2, 39 ]
-----------------------
[ 62, 80, 80, 90, 100, 8, 1, 2, 39 ]
-----------------------
[ 8, 62, 80, 80, 90, 100, 1, 2, 39 ]
-----------------------
[ 1, 8, 62, 80, 80, 90, 100, 2, 39 ]
-----------------------
[ 1, 2, 8, 62, 80, 80, 90, 100, 39 ]
-----------------------
[ 1, 2, 8, 39, 62, 80, 80, 90, 100 ]
-----------------------
[ 1, 2, 8, 39, 62, 80, 80, 90, 100 ]
*/
```

# 希尔排序
```
function ShellSort(array) {
  var length = array.length;
  var gap = Math.round(length / 2);
  while (gap > 0) {
    for (var i = gap; i < length; i++) {
      var insert = array[i];
      var index = i;
      for (var j = i; j >= 0; j-=gap) {
        if (insert < array[j]) {
          array[j+gap] = array[j];
          index = j;
        }
      }
      array[index] = insert;
    }
    console.log(array);
    console.log("-----------------------");
    gap = Math.round(gap/2 - 0.1);
  }
  return array;
}

var arr = [ 13, 14, 94, 33, 82, 25, 59, 94, 65, 23, 45, 27, 73, 25, 39, 10 ];
var result = ShellSort(arr);
console.log(result); 
/*
[ 13, 14, 45, 27, 73, 25, 39, 10, 65, 23, 94, 33, 82, 25, 59, 94 ]
-----------------------
[ 13, 14, 39, 10, 65, 23, 45, 27, 73, 25, 59, 33, 82, 25, 94, 94 ]
-----------------------
[ 13, 10, 39, 14, 45, 23, 59, 25, 65, 25, 73, 27, 82, 33, 94, 94 ]
-----------------------
[ 10, 13, 14, 23, 25, 25, 27, 33, 39, 45, 59, 65, 73, 82, 94, 94 ]
-----------------------
[ 10, 13, 14, 23, 25, 25, 27, 33, 39, 45, 59, 65, 73, 82, 94, 94 ]
*/
```

# 归并排序
```
function MergeSort(array) {
  var length = array.length;
  if (length <= 1) {
    return array;
  } else {
    var num = Math.ceil(length/2);
    var left = MergeSort(array.slice(0, num));
    var right = MergeSort(array.slice(num, length));
    return merge(left, right);
  }
}

function merge(left, right) {
  console.log(left);
  console.log(right);
  var a = new Array();
  while (left.length > 0 && right.length > 0) {
    if (left[0] <= right[0]) {
      var temp = left.shift();
      a.push(temp);
    } else {
      var temp = right.shift();
      a.push(temp);
    }
  }
  if (left.length > 0) {
    a = a.concat(left);
  }
  if (right.length > 0) {
    a = a.concat(right);
  }
  console.log(a);
  console.log("-----------------------------");
  return a;
}

var arr = [ 13, 14, 94, 33, 82, 25, 59, 94, 65, 23, 45, 27, 73, 25, 39, 10 ];
var result = MergeSort(arr);
console.log(result);
/*
[ 13 ]
[ 14 ]
[ 13, 14 ]
-----------------------------
[ 94 ]
[ 33 ]
[ 33, 94 ]
-----------------------------
[ 13, 14 ]
[ 33, 94 ]
[ 13, 14, 33, 94 ]
-----------------------------
[ 82 ]
[ 25 ]
[ 25, 82 ]
-----------------------------
[ 59 ]
[ 94 ]
[ 59, 94 ]
-----------------------------
[ 25, 82 ]
[ 59, 94 ]
[ 25, 59, 82, 94 ]
-----------------------------
[ 13, 14, 33, 94 ]
[ 25, 59, 82, 94 ]
[ 13, 14, 25, 33, 59, 82, 94, 94 ]
-----------------------------
[ 65 ]
[ 23 ]
[ 23, 65 ]
-----------------------------
[ 45 ]
[ 27 ]
[ 27, 45 ]
-----------------------------
[ 23, 65 ]
[ 27, 45 ]
[ 23, 27, 45, 65 ]
-----------------------------
[ 73 ]
[ 25 ]
[ 25, 73 ]
-----------------------------
[ 39 ]
[ 10 ]
[ 10, 39 ]
-----------------------------
[ 25, 73 ]
[ 10, 39 ]
[ 10, 25, 39, 73 ]
-----------------------------
[ 23, 27, 45, 65 ]
[ 10, 25, 39, 73 ]
[ 10, 23, 25, 27, 39, 45, 65, 73 ]
-----------------------------
[ 13, 14, 25, 33, 59, 82, 94, 94 ]
[ 10, 23, 25, 27, 39, 45, 65, 73 ]
[ 10, 13, 14, 23, 25, 25, 27, 33, 39, 45, 59, 65, 73, 82, 94, 94 ]
-----------------------------
[ 10, 13, 14, 23, 25, 25, 27, 33, 39, 45, 59, 65, 73, 82, 94, 94 ]
*/
```

# 快速排序
```
function QuickSort(array) {
  var length = array.length;
  if (length <= 1) {
    return array;
  } else {
    var smaller = [];
    var bigger = [];
    var base = [array[0]];
    for (var i = 1; i < length; i++) {
      if (array[i] <= base[0]) {
        smaller.push(array[i]);
      } else {
        bigger.push(array[i]);
      }
    }
    console.log(smaller.concat(base.concat(bigger)));
    console.log("-----------------------");
    return QuickSort(smaller).concat(base.concat(QuickSort(bigger)));
  }
}


var arr = [ 8, 10, 100, 90, 65, 5, 4, 10, 2, 4 ];
var result = QuickSort(arr);
console.log(result);
/*
[ 5, 4, 2, 4, 8, 10, 100, 90, 65, 10 ]
-----------------------
[ 4, 2, 4, 5 ]
-----------------------
[ 2, 4, 4 ]
-----------------------
[ 2, 4 ]
-----------------------
[ 10, 10, 100, 90, 65 ]
-----------------------
[ 90, 65, 100 ]
-----------------------
[ 65, 90 ]
-----------------------
[ 2, 4, 4, 5, 8, 10, 10, 65, 90, 100 ]
*/
```
# 计数排序
```
 function countingSort(nums) {
            let arr = [];  // 定义一个空数组
            let max = Math.max(...nums); // 找到这个数组的 最大 最小值
            let min = Math.min(...nums);

            // 装桶
            for(let i=0, len=nums.length; i<len; i++) { // 把传入数组的值作为下标  装入一个长度为数组最大值长度的临时数组
                // 比如 第一位是5  传入arr后 arr为[,,,,,1]   =>   [empty × 5, 1]
                let temp = nums[i];
                arr[temp] = arr[temp] + 1 || 1;  
            }
            let index = 0;  // 定义一个索引 这个索引是 后面用来改变原数组的 

            // 还原原数组
            for(let i=min; i<=max; i++) { // 写一个for循环 i=原数组最小值  i>原数组最大值的时候跳出循环  i每次++
                while(arr[i] > 0) { // 从arr[i]开始 如果他>0 
                    nums[index++] = i; // 就把原数组的第index位赋值为 i
                    arr[i]--; // 每赋值完一次后 临时数组当前位的值就--   如果=0 就说明这位上没有值了
                }
            }
        }
```

