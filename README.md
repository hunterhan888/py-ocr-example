需要先安装tesseract
MacOS
```bash
brew install tesseract
```

# usage

安装依赖项
```bash
pip install -r requirements.txt
```

# 运行

查看帮助运行
```bash
python ocr.py -h 
```

如果需要识别中文，需要安装tesseract-lang
```bash
brew install tesseract-lang 
```

在使用的时候增加`--language`参数，简体中文传入`chi_sim`

例如:
```bash
python ocr.py path/to/your/image.png --language chi_sim
```

如果需要debug可以使用
```python
python ocr.py image_path --language chi_sim --debug
```
开启后会将预处理的图片保存到本地
生成denoised_image.png,gray_image.png,binary_image