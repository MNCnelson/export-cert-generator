# ==========================================
    # PAGE 1: 货物标识与来源 (Section I, II, III)
    # ==========================================
    
    # 1. 顶部第一行: 复选框、份数 和 证书号
    c.setFont("Helvetica-Bold", 9)
    # ORIGINAL 复选框
    c.circle(18*mm, 281*mm, 1.5*mm) # 画圆圈代替方框
    c.drawString(22*mm, 280*mm, "ORIGINAL")
    # DUPLICATA 复选框
    c.circle(42*mm, 281*mm, 1.5*mm)
    c.drawString(46*mm, 280*mm, "DUPLICATA")
    
    # 右侧的证书号
    c.drawString(135*mm, 280*mm, f"CERTIFICAT N° / CERTIFICATE N° {cert_number}")
    
    # 底部说明
    c.setFont("Helvetica", 7)
    c.drawString(18*mm, 275*mm, "Nombre total de duplicatas délivrés / Total number of copies issued : 0")

    # 2. 居中机构信息与 Logo
    # 加载官方 Logo 居中显示
    if os.path.exists("logo.png"):
        c.drawImage("logo.png", 95*mm, 255*mm, width=20*mm, height=20*mm, preserveAspectRatio=True, mask='auto')

    c.setFont("Helvetica-Bold", 12)
    c.drawString(65*mm, 265*mm, "REPUBLIQUE")
    c.drawString(120*mm, 265*mm, "FRANCAISE")
    
    c.setFont("Helvetica-Bold", 10)
    c.drawCentredString(105*mm, 250*mm, "DIRECTION GENERALE DE L'ALIMENTATION")
    
    c.setFont("Helvetica-Bold", 10)
    c.drawCentredString(105*mm, 240*mm, "CERTIFICAT POUR L'EXPORTATION A DESTINATION DE HONG KONG")
    c.drawCentredString(105*mm, 235*mm, "DE VIANDES FRAICHES DE GIBIER A PLUME, ET DE PRODUITS A BASE DE")
    c.drawCentredString(105*mm, 230*mm, "CES VIANDES EN PROVENANCE DE FRANCE")
    
    c.setFont("Helvetica-Oblique", 9) # 使用斜体
    c.drawCentredString(105*mm, 225*mm, "CERTIFICATE FOR EXPORTATION OF GAME BIRDS,")
    c.drawCentredString(105*mm, 220*mm, "AND THEIR PRODUCTS FROM FRANCE TO HONG KONG")

    # [Section I] ... (下面的代码保持不变)
