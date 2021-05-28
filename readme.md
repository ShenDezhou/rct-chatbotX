# 安装mysql并导出bin目录
`
修改~/.bash_profile，增加
export PATH=$PATH:/usr/local/mysql/bin/
export LIBRARY_PATH=$LIBRARY_PATH:/usr/local/mysql/lib
`

#1. 安装git+https://github.com/morteza31/ChatterBot.git库
一同安装的有ChatterBot-1.1.0 blis-0.2.4 preshed-2.0.1 pyyaml-5.3.1 spacy-2.1.9 srsly-1.0.5 thinc-7.0.8

#2.下载spacy语言模型

```
python -m spacy download en
```
或者
```
pip install https://github.com/explosion/spacy-models/releases/download/en_core_web_sm-3.0.0/en_core_web_sm-3.0.0.tar.gz
```
则会安装spacy3.0.0

#3 训练并推理
`
python main.py
python main_cn.py
`