# 基于Arcpy脚本的空间规划工具箱

## 背景 
从事规划一线多年，大量的工作其实用于制图。然而每个设计单位都有自己的一套工作体系，市场上也有规划软件\工具\平台，大多水土不服。为了偷懒，我打算通过实践，基于arcpy对部分工作流进行自动化的尝试 


## 目前实现的功能  

### 1.三调基数转换
基于《国土空间调查、规划、用途管制用地用海分类指南（试行）》中已三调用地的衔接，输入三调矢量文件，识别DLBM字段，
三调用地编码转用地用海用地编码、用地用海编码转用地用海名称。  
部分一对多的转换需要细化的话还是要自己写  
<img src="https://github.com/Milentsz/Spatial-Planning-Arcpy/blob/main/sample/%E5%9F%BA%E6%95%B0%E8%BD%AC%E6%8D%A2-sample.jpg" alt="图片alt" title="基数转换" width=400px>
### 2.用地统计表的生成
从三调基数转换生成的要素，通过字段读取，统计用地表格并导出excel。  
<img src="https://github.com/Milentsz/Spatial-Planning-Arcpy/blob/main/sample/%E7%94%A8%E5%9C%B0%E7%BB%9F%E8%AE%A1-sample.jpg" alt="图片alt" title="用地统计" width=400px>

### 3.批量出图
结合规划日常工作，优化出图流程。以迭代图层组作为出图内容，同时保留底图图层组，同步更新图纸名和图号，另外部分图层可根据专题图纸需求灵活开关。  
<img src="https://github.com/Milentsz/Spatial-Planning-Arcpy/blob/main/sample/%E6%89%B9%E9%87%8F%E5%87%BA%E5%9B%BE-sample.jpg" alt="图片alt" title="批量出图" width=400px>
## pyt工具箱
写入了pyt工具箱，也因自己兴趣使然，要保持初心，先暂命名为**初心规划助理**。工具可在arcgis pro 3.0下运行，具有UI界面，并丰富了部分功能，方便使用，其他环境没有测试。

不支持arcmap，有机会对python2.7兼容吧。
## 
想了想决定项目开源，也欢迎有兴趣的同行交流，集众智、采众长，也许哪一天就能解放生产力了。

**联系我**
微信：milent    邮箱：milent@qq.com
