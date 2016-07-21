# copyq-action-youdao
有道词典的 copyq 执行动作。

你可以新建命令
```
./copyq-action-youdao/app.py %1
```
这样就可以翻译你选中的条目

也可以设置全局热键，翻译选中的文字：
```
copyq show
copyq selection |xargs ./copyq-action-youdao/app.py
```
