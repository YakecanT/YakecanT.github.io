# -*- coding: utf-8 -*-
"""
Created on Sun Mar 1 21:49:42 2020
 实现将本地adoc自动渲染、自动拼接模板的功能
 采用面向对象方法
 0302备注：已完成基本的自动渲染，待解决：无法调用IDE获取shell权限；
 todo：
    1、自动化生成概要（概要如何提取，字数控制？选取什么部分？）
    2、自动化统计字数、图片、阅读时间，放置在自身的html中
    3、自动化复制修改时间、题目、概要、头图到index.html的对应位置

@author: Tarin.chen
"""
import os
import re

class adoc:
    
    # 构造器
    def __init__(self, basePath, baseCSS, cssPath):
        self.basePath = basePath
        self.baseCSS = baseCSS
        self.cssPath = cssPath
        self.name = basePath.split(sep="\\")[-1]
        self.cmd = 'asciidoctor -a linkcss -a stylesheet=' + self.baseCSS\
            + ' -a stylesdir=' + self.cssPath\
            + ' ' + self.basePath + '/main.adoc'
    
    def getMainHtml(self):
        with open(self.basePath + "/main.html", mode="r", encoding="utf-8") as mainFile:
            main = mainFile.read()
            mainText = main.split(sep="toc-left\">")
            mainText = mainText[1].strip("</body>\n</html>")
        
        self.mainText = mainText
        return self.mainText
    
    # def findSelf(self, fromFile):
    #     fileText = fromFile.read()
    #     if re.find(self.name, fileText, re.S): 
    #         return True
    #     else return False
    
    # def createSelf(self, fromFile):
    #     fileText = fromFile.read()
    #     re.
        


if __name__ == '__main__':
    
    # 定义全局变量
    adoc_path = "D:/github/YakecanT.github.io/adoc"
    adoc_list = os.listdir(adoc_path) 
    adoc_list.remove('template')

    baseCSS = "a-main.css"
    cssPath = "D:/github/YakecanT.github.io/assets/css"

    templateFile = open(adoc_path+'/template/adoc.html', mode="r", encoding="utf-8")
    template = templateFile.read()
    templateList = template.split(sep="toc-left\">\n<")

    for f in adoc_list:
        # 渲染为html
        this_path_input=os.path.join(adoc_path,f)
        adocFile = adoc(this_path_input, baseCSS, cssPath)
        os.system(adocFile.cmd)

        # 写入模板
        with open(this_path_input + "/adoc.html", mode="w", encoding="utf-8", errors="ignore") as htmlFile:
            mainText = adocFile.getMainHtml()  # 提取其中内容
            htmlText = (templateList[0] +   # 并入模板
                    "toc-left\">\n<d" + mainText +
                     "<" + templateList[1])
            htmlFile.write(htmlText)
        
        # # 写入index.html导航
        # indexFile = open(adoc_path.replace("adoc", "index.html"), mode="r", encoding="utf-8")
        # indexText = indexFile.read()







    

