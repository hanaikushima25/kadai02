# ロボットシステム学課題2

## 概要
2つのノードを動かし、二倍した結果を表示する

## 動作環境
- Raspberry Pi 4 Computer Model B
- OS:ubuntu 20.04 LTS
- ROS Noetic

## 実行手順
1.ディレクトリに入る
```
 cd ~/catkin_ws/src
```
2.リポジトリをクローンする
```
 git clone git@github.com:hanaikushima25/kadai02.git
```
3.一つ前のリポジトリに戻る
```
 cd ..
```
4.コンパイルする
```
 catkin_make
```
5.ROSを立ち上げる
```
 roscore &
```
6.count.pyを実行する
```
 chmod +x count.py   
 roscore mypkg count.py
```
7.twice.pyを別の端末で実行する
```
 chmod +x twice.py 
 rosrun mypkg twice.py
```
8.また別の端末で実行する
```
 rostopic echo /twice.py
```
停止する場合はctrl + c
## 実行結果
 Youtube https://www.youtube.com/watch?v=xc0hnqJGaRw
## 文責
 - Hana Ikushima
 - s20C1006NU@s.chibakoudai.jp
## ライセンス
　"mypkg" is under BSD 3-Clause "NEW" or "Revised"License.
 
## 参考
　https://ryuichiueda.github.io/robosys2020/lesson10_ros.html#/20
 
 Thank you!
　
# kadai02
