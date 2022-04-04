---
title: vue-cli3创建项目
categories: Vue
date: 2022-03-31 14:59:11
tags:
     - vue
---
### 简介
Vue CLI 是一个基于 Vue.js 进行快速开发的完整系统，提供： 
通过 @vue/cli 实现的交互式的项目脚手架。  
通过 @vue/cli + @vue/cli-service-global 实现的零配置原型开发。  
一个运行时依赖 (@vue/cli-service)，该依赖： 
可升级； 
基于 webpack 构建，并带有合理的默认配置；  
可以通过项目内的配置文件进行配置；  
可以通过插件进行扩展。  
一个丰富的官方插件集合，集成了前端生态中最好的工具。  
一套完全图形化的创建和管理 Vue.js 项目的用户界面。 
Vue CLI 致力于将 Vue 生态中的工具基础标准化。它确保了各种构建工具能够基于智能的默认配置即可平稳衔接，这样你可以专注在撰写应用上，而不必花好几天去纠结配置的问题。与此同时，它也为每个工具提供了调整配置的灵活性，无需 eject。  
![在这里插入图片描述](https://img-blog.csdnimg.cn/3bf082800cdc4173b30fcd27033aadf7.png?x-oss-process=image/watermark,type_d3F5LXplbmhlaQ,shadow_50,text_Q1NETiBA5pif6L6w5LiN5Y-K6Zaj5LiL,size_20,color_FFFFFF,t_70,g_se,x_16)
废话不多说，直接操作。


### 步骤
先检查电脑是否安装vue-cli
```
vue --version
```
若无
```
npm i -g @vue/cli
```
创建vue项目
```
vue create project
```
![在这里插入图片描述](https://img-blog.csdnimg.cn/85ed9e9907804e95bcc10fc6383f47cd.png)
按键盘上下键可以选择默认（default）还是手动（Manually），如果选择default，一路回车执行下去就行了。
![在这里插入图片描述](https://img-blog.csdnimg.cn/8a2eaa1444d846b6b4a0a1158aeec47d.png?x-oss-process=image/watermark,type_d3F5LXplbmhlaQ,shadow_50,text_Q1NETiBA5pif6L6w5LiN5Y-K6Zaj5LiL,size_20,color_FFFFFF,t_70,g_se,x_16)
```
--选择配置--
//提示，空格键是选中与取消
TypeScript 支持使用 TypeScript 书写源码
Progressive Web App (PWA) Support PWA 支持。
Router 支持 vue-router 。
Vuex 支持 vuex 。
CSS Pre-processors 支持 CSS 预处理器。
Linter / Formatter 支持代码风格检查和格式化。
Unit Testing 支持单元测试。
E2E Testing 支持 E2E 测试。
```
![在这里插入图片描述](https://img-blog.csdnimg.cn/6cf4c348c2e5491dad21b59f2bfbb645.png)
选择3.x
然后一路回车，css处理去我选择的是Saaa/SCSS
![在这里插入图片描述](https://img-blog.csdnimg.cn/6960065aea69496491130506c741a86c.png?x-oss-process=image/watermark,type_d3F5LXplbmhlaQ,shadow_50,text_Q1NETiBA5pif6L6w5LiN5Y-K6Zaj5LiL,size_20,color_FFFFFF,t_70,g_se,x_16)
选择ESLint + Prettier
![在这里插入图片描述](https://img-blog.csdnimg.cn/dd7937881d9343668e88acb8dbc388a1.png?x-oss-process=image/watermark,type_d3F5LXplbmhlaQ,shadow_50,text_Q1NETiBA5pif6L6w5LiN5Y-K6Zaj5LiL,size_20,color_FFFFFF,t_70,g_se,x_16)
选择保存就检查（Lint on save）
![在这里插入图片描述](https://img-blog.csdnimg.cn/92f7560db23a48819e769dd7cd261939.png?x-oss-process=image/watermark,type_d3F5LXplbmhlaQ,shadow_50,text_Q1NETiBA5pif6L6w5LiN5Y-K6Zaj5LiL,size_20,color_FFFFFF,t_70,g_se,x_16)
配置文件存放地方
第一个是独立文件夹位置，第二个是在package.json文件里,这我选择独立文件夹
![在这里插入图片描述](https://img-blog.csdnimg.cn/4958cb5afe6841a19a34406e8be7dd82.png?x-oss-process=image/watermark,type_d3F5LXplbmhlaQ,shadow_50,text_Q1NETiBA5pif6L6w5LiN5Y-K6Zaj5LiL,size_20,color_FFFFFF,t_70,g_se,x_16)
然后继续默认回车，最后等待安装完成......
![在这里插入图片描述](https://img-blog.csdnimg.cn/12498ece55ff4b2ba5e7754cbc12e285.png)
启动
```
cd project
npm run serve
```

接下来配置一下vue.config.js文件，如果没有这个文件，就在src同一目录下创建，其实真正需要修改添加的也不多，简单的项目，大部分配置都默认好了。
```
module.exports = {
  // 部署应用时的基本 URL
  publicPath: process.env.NODE_ENV === 'production' ? '/' : '/',
  // build时构建文件的目录 构建时传入 --no-clean 可关闭该行为
  outputDir: 'dist',
  // build时放置生成的静态资源 (js、css、img、fonts) 的 (相对于 outputDir 的) 目录
  assetsDir: '',
  // 指定生成的 index.html 的输出路径 (相对于 outputDir)。也可以是一个绝对路径。
  indexPath: 'index.html',
  // 默认在生成的静态资源文件名中包含hash以控制缓存
  filenameHashing: true,
  // 构建多页面应用，页面的配置
  pages: {
    index: {
      // page 的入口
      entry: 'src/main.ts',
      // 模板来源
      template: 'public/index.html',
      // 在 dist/index.html 的输出
      filename: 'index.html',
      // 当使用 title 选项时，
      // template 中的 title 标签需要是 <title><%= htmlWebpackPlugin.options.title %></title>
      title: 'Index Page',
      // 在这个页面中包含的块，默认情况下会包含
      // 提取出来的通用 chunk 和 vendor chunk。
      chunks: ['chunk-vendors', 'chunk-common', 'index']
    },
    // 当使用只有入口的字符串格式时，
    // 模板会被推导为 `public/subpage.html`
    // 并且如果找不到的话，就回退到 `public/index.html`。
    // 输出文件名会被推导为 `subpage.html`。
    // subpage: 'src/subpage/main.js'
  },
  // 是否在开发环境下通过 eslint-loader 在每次保存时 lint 代码 (在生产构建时禁用 eslint-loader)
  lintOnSave: process.env.NODE_ENV !== 'production',
  // 是否使用包含运行时编译器的 Vue 构建版本
  runtimeCompiler: false,
  // Babel 显式转译列表
  transpileDependencies: [],
  // 如果你不需要生产环境的 source map，可以将其设置为 false 以加速生产环境构建
  productionSourceMap: true,
  // 设置生成的 HTML 中 <link rel="stylesheet"> 和 <script> 标签的 crossorigin 属性（注：仅影响构建时注入的标签）
  crossorigin: '',
  // 在生成的 HTML 中的 <link rel="stylesheet"> 和 <script> 标签上启用 Subresource Integrity (SRI)
  integrity: false,
  // 如果这个值是一个对象，则会通过 webpack-merge 合并到最终的配置中
  // 如果你需要基于环境有条件地配置行为，或者想要直接修改配置，那就换成一个函数 (该函数会在环境变量被设置之后懒执行)。该方法的第一个参数会收到已经解析好的配置。在函数内，你可以直接修改配置，或者返回一个将会被合并的对象
  configureWebpack: {},
  // 对内部的 webpack 配置（比如修改、增加Loader选项）(链式操作)
  chainWebpack: () => {},
  // css的处理
  css: {
    // // 当为true时，css文件名可省略 module 默认为 false
    // modules: false,
    // 是否将组件中的 CSS 提取至一个独立的 CSS 文件中,当作为一个库构建时，你也可以将其设置为 false 免得用户自己导入 CSS
    // 默认生产环境下是 true，开发环境下是 false
    extract: false,
    // 是否为 CSS 开启 source map。设置为 true 之后可能会影响构建的性能
    sourceMap: false,
    //向 CSS 相关的 loader 传递选项(支持 css-loader postcss-loader sass-loader less-loader stylus-loader)
    loaderOptions: {
      css: {},
      less: {}
    }
  },
  // 所有 webpack-dev-server 的选项都支持
  devServer: {
    open: false,
    // host: 'localhost', //默认是 localhost。如果你希望服务器外部可访问，指定如下 host: '0.0.0.0'，设置之后之后可以访问ip地址
    port: 8080,
    hot: true,
    // proxy: {
    //   '/': {
    //     target: 'http://localhost:8080', //目标接口域名
    //     secure: false, //false为http访问，true为https访问
    //     changeOrigin: true, //是否跨域
    //     pathRewrite: {
    //       '^/': '/' //重写接口
    //     }
    //   }
    // }, // 设置代理
  },
  // 是否为 Babel 或 TypeScript 使用 thread-loader
  parallel: require('os').cpus().length > 1,
  // 向 PWA 插件传递选项
  pwa: {},
  // 可以用来传递任何第三方插件选项
  pluginOptions: {}
}
```







