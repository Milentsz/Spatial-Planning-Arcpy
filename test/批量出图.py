'''
这是一个批量出图的脚本，根据图层组循环出图，同时保留一个底图图层组显示，
还可以根据图层关键字（比如#，@开头）实现特定图纸的图层开关（如中小学专题图，可以打开底图里的居住用地图层）
对于图纸元素，可以根据图层组名作为图纸标题输出，图号按顺序递增
'''

import arcpy
aprx = arcpy.mp.ArcGISProject(r"..\工程文件.aprx")
lyt = aprx.listLayouts("出图")[0]
mf = lyt.listElements("MapFrame_Element")[0]
mp = mf.map
tm = '图名'
th = '图号'
elm1 = lyt.listElements("TEXT_ELEMENT",tm)[0]
elm2 = lyt.listElements("TEXT_ELEMENT",th)[0]
elm3 = lyt.listElements("TEXT_ELEMENT",'项目名称')[0]
legend = lyt.listElements("LEGEND_ELEMENT", "图例")[0]

layers = mp.listLayers()
juzhulayer = mp.listLayers('现状居住用地')[0]     #注意重名图层
fwlayer1 = mp.listLayers('建成区范围')[-1] 
fwlayer2 = mp.listLayers('现状建设用地')[-1] 

ln_key = ['小学','中学','绿地','公园','绿道','农贸市场','街区']
oldlayers = []                 #建立空list

if '居住' in juzhulayer.name :
    for layer in layers:
        v=layer.visible
        oldlayers.append(v)     #定义原始图层可见状态，写入空list

    # 为出图前初始化图层可见状态
        if layer.isBasemapLayer==0:
            layer.visible = True      #打开非底图所有图层
        if layer.name == layer.longName and layer.isBasemapLayer==0:  
            layer.visible = False     #关掉所有图层组，以及单独图层(name 值等于 longName 值，则该图层不在图层组中)

    #遍历图层组批量出图     
    firstnum = 2              #起始图号
    for layer in layers:
        if layer.isGroupLayer==1 and layer.isBasemapLayer==0 and '@' not in layer.name: 
            layer.visible = True
            # 居住用地开关条件in_key     
            if any(key in layer.name for key in ln_key) and '人均公园绿地' not in layer.name:
                juzhulayer.visible = True
            else:
                juzhulayer.visible = False
            if any(v in layer.name for v in ['建成区','用地现状','人口密度']):
                fwlayer2.visible = fwlayer1.visible = False
            else:
                fwlayer2.visible = fwlayer1.visible = True
            elm1.text = layer.name           #图层名写入图名
            elm2.text = str(firstnum).rjust(2,'0')         #写入图号
            legend.mapFrame = mf   #重新关联图例，如果不这么做的话在arcgis外运行，会不更新图例
            lyt.exportToPNG(r'D:\出图\'+ '\\' + elm3.text + lyt.name + elm2.text + '-' + layer.name ,200)
            print('完成\t===> ' + elm2.text +'.'+ str(layer))
            layer.visible = False
            firstnum += 1


    # 复原图层可见状态
    elm1.text,elm2.text ='图名','00'
    for x,y in zip(layers,oldlayers):
        x.visible = y
    print("==========全部完成==========")
    

else :
     print ('没有名为“现状居住用地”图层,请检查')

del aprx
