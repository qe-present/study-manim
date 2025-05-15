# 运行
```shell
./build.cmd
```
## Main
```python
        rendered_code = Code(
            code_string=code,
            language="python",
            background="window",
            background_config={"stroke_color": "maroon"},
        )
```
- 这段代码创建了一个代码对象，指定了代码字符串、语言和背景配置
- `background_config` 是一个字典，用于设置背景的配置选项
- `stroke_color` 是背景的边框颜色
- `background` 是背景的类型，可以是 "window" 或 "solid"
- `language` 是代码的语言类型，这里是 Python
- `code_string` 是要渲染的代码字符串
