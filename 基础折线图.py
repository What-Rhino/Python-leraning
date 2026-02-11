from pyecharts.charts import Line
from pyecharts.options import TitleOpts,LegendOpts,ToolboxOpts,VisualMapOpts
# 构建基础折线图
line = Line()
line.add_xaxis(["中国","美国","英国"])
line.add_yaxis("GDP",[30,20,10])

# 设置全局配置项
line.set_global_opts(
    title_opts=TitleOpts(title="GDP展示",pos_left="center",pos_bottom="1%"),#标题
    legend_opts=LegendOpts(is_show=True),#图例
    toolbox_opts=ToolboxOpts(is_show=True),#工具箱
    visualmap_opts=VisualMapOpts(is_show=True)#视觉映射
)






line.render("基础折线图.html")