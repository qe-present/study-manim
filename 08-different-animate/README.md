# 运行
```shell
./build.cmd
```
## 代码1
```python
 self.play(DrawBorderThenFill(rt))
```
- self.play - 播放动画的函数
- DrawBorderThenFill(rt) - 绘制边框然后填充颜色的动画
## 代码2
```python
        self.play(FadeIn(rt))
        self.wait(2)
        self.play(FadeOut(rt))
```
- FadeIn(rt) - 渐显动画
- FadeOut(rt) - 渐隐动画
- self.wait(2) - 等待2秒
## 代码3
```python
        rt=RoundedRectangle(corner_radius=0.5,fill_opacity=0.2,color=BLUE,fill_color=BLUE)
        t=Triangle(fill_color=RED,fill_opacity=0.5)
        self.add(rt)
        self.wait(2)
        self.play(Transform(rt,t))
        self.wait(2)
```
- Transform(rt,t) - 变换动画，将 rt 变换为 t
- Triangle - 创建一个三角形对象