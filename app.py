def draw_blue_chop(c, x, y, vet_name, chop_date):
    """使用真实的印章图片底图，并在上方叠加动态日期"""
    c.saveState()
    
    # 根据下拉菜单选择，匹配对应的印章图片文件名
    if "Amal" in vet_name:
        stamp_img = "stamp_amal.png"
    elif "Mahmoud" in vet_name:
        stamp_img = "stamp_mahmoud.png"
    else:
        stamp_img = "stamp_djamal.png"
        
    # 定位到页面上该盖章的坐标
    c.translate(x, y)
    
    # 稍微倾斜，让印章看起来像是手工盖上去的
    c.rotate(3) 

    # 检查 GitHub 仓库里有没有上传对应的印章底图
    if os.path.exists(stamp_img):
        # 1. 贴上真实的印章照片底图 (宽约78mm，高约45mm，可根据您的实际裁切比例微调)
        c.drawImage(stamp_img, 0, 0, width=78*mm, height=45*mm, preserveAspectRatio=True, mask='auto')
        
        # 2. 在印章图片的特定坐标上，印上动态生成的日期
        # 设置字体颜色为与印章相近的深蓝色
        c.setFillColorRGB(0.12, 0.28, 0.60) 
        c.setFont("Helvetica-Bold", 14)
        
        # 调整下方坐标 (39*mm 是水平居中，16*mm 是距离底部的垂直高度)
        # 如果您发现生成的日期偏高或偏低，请修改 16*mm 这个数字
        c.drawCentredString(39*mm, 16*mm, chop_date)
        
    else:
        # 如果忘记上传图片，在 PDF 上显示红字提示
        c.setFillColorRGB(1, 0, 0)
        c.setFont("Helvetica", 10)
        c.drawString(0, 20*mm, f"[请在 GitHub 上传 {stamp_img} 图片文件]")
        
    c.restoreState()
