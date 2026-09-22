import streamlit as st
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A4
from reportlab.lib.units import mm
import io
import os

def draw_blue_chop(c, x, y, vet_name, chop_date):
    """精準還原圖片中印章日期的字形、大小、格式與傾斜度"""
    c.saveState()
    
    # 根據獸醫姓名匹配底圖
    if "Amal" in vet_name:
        stamp_img = "stamp_amal.png"
    elif "Mahmoud" in vet_name:
        stamp_img = "stamp_mahmoud.png"
    else:
        stamp_img = "stamp_djamal.png"
        
    c.translate(x, y)
    
    # 印章整體傾斜角度
    angle = 6.5
    c.rotate(angle)

    if os.path.exists(stamp_img):
        # 1. 正片疊底模式（Multiply），避免白底遮擋後方表格文字
        c.setBlendMode("Multiply")
        c.drawImage(stamp_img, 0, 0, width=75*mm, height=43*mm, preserveAspectRatio=True, mask='auto')
        
        # 2. 繪製動態日期（還原圖片字體大小與深藍色印泥質感）
        c.setBlendMode("Normal")
        c.setFillColorRGB(0.10, 0.22, 0.52) # 深藍墨色
        
        # 使用 15pt 粗體字型還原橡皮章打印感
        c.setFont("Helvetica-Bold", 15)
        
        # 在擦除日期的區域精準列印傾斜日期
        c.drawCentredString(35*mm, 15*mm, chop_date)
    else:
        c.setFillColorRGB(1, 0, 0)
        c.setFont("Helvetica", 10)
        c.drawString(0, 20*mm, f"[請在 GitHub 上傳 {stamp_img}]")
        
    c.restoreState()

def create_pdf(cert_number, species, weight, packages, temp, date_slaughter, date_production, vet_name, chop_date):
    buffer = io.BytesIO()
    c = canvas.Canvas(buffer, pagesize=A4)
    
    # ==========================================
    # PAGE 1: 貨物標識與來源
    # ==========================================
    c.setFont("Helvetica-Bold", 9)
    c.drawString(15*mm, 280*mm, "ORIGINAL")
    c.circle(32*mm, 281*mm, 1.5*mm)         
    c.circle(32*mm, 281*mm, 0.7*mm, fill=1) 
    
    c.drawString(42*mm, 280*mm, "DUPLICATA")
    c.circle(62*mm, 281*mm, 1.5*mm)         
    
    c.drawString(135*mm, 280*mm, f"CERTIFICAT N° / CERTIFICATE N° {cert_number}")
    c.setFont("Helvetica", 7)
    c.drawString(15*mm, 275*mm, "Nombre total de duplicatas délivrés / Total number of copies issued : 0")

    if os.path.exists("logo.png"):
        c.drawImage("logo.png", 95*mm, 255*mm, width=20*mm, height=20*mm, preserveAspectRatio=True, mask='auto')

    c.setFont("Helvetica-Bold", 12)
    c.drawString(65*mm, 265*mm, "REPUBLIQUE")
    c.drawString(120*mm, 265*mm, "FRANCAISE")
    
    c.setFont("Helvetica-Bold", 10)
    c.drawCentredString(105*mm, 250*mm, "DIRECTION GENERALE DE L'ALIMENTATION")
    c.drawCentredString(105*mm, 240*mm, "CERTIFICAT POUR L'EXPORTATION A DESTINATION DE HONG KONG")
    c.drawCentredString(105*mm, 235*mm, "DE VIANDES FRAICHES DE GIBIER A PLUME, ET DE PRODUITS A BASE DE")
    c.drawCentredString(105*mm, 230*mm, "CES VIANDES EN PROVENANCE DE FRANCE")
    
    c.setFont("Helvetica-Oblique", 9)
    c.drawCentredString(105*mm, 225*mm, "CERTIFICATE FOR EXPORTATION OF GAME BIRDS,")
    c.drawCentredString(105*mm, 220*mm, "AND THEIR PRODUCTS FROM FRANCE TO HONG KONG")

    # Section I
    c.setFont("Helvetica-Bold", 9)
    c.drawString(15*mm, 210*mm, "I. Identification des viandes et produits à base de viande / Identification of games birds and their products:")
    
    c.setFont("Helvetica", 9)
    c.drawString(20*mm, 202*mm, "a) Espèce animale / Species:")
    c.setDash(1, 2)
    c.line(65*mm, 202*mm, 195*mm, 202*mm)
    c.setFont("Helvetica-Bold", 10)
    c.drawString(70*mm, 203*mm, species) 
    
    c.setFont("Helvetica", 9)
    c.drawString(20*mm, 194*mm, "b) Nature des pièces / Nature of joints:")
    c.line(75*mm, 194*mm, 195*mm, 194*mm)
    c.drawString(80*mm, 195*mm, "SEE ANNEXE")
    
    c.drawString(20*mm, 186*mm, "c) Nombre de pièces ou d'unités d'emballage / Number of joints or packages:")
    c.line(135*mm, 186*mm, 195*mm, 186*mm)
    c.setFont("Helvetica-Bold", 10)
    c.drawString(140*mm, 187*mm, packages) 
    
    c.setFont("Helvetica", 9)
    c.drawString(20*mm, 178*mm, "d) Température d'entreposage / Temperature of storage:")
    c.line(100*mm, 178*mm, 140*mm, 178*mm)
    c.setFont("Helvetica-Bold", 10)
    c.drawString(105*mm, 179*mm, temp) 
    
    c.setFont("Helvetica", 9)
    c.drawString(145*mm, 178*mm, "e) Poids net/Net weight:")
    c.line(180*mm, 178*mm, 195*mm, 178*mm)
    c.setFont("Helvetica-Bold", 10)
    c.drawString(182*mm, 179*mm, weight) 
    
    c.setFont("Helvetica", 9)
    c.drawString(20*mm, 170*mm, "f) Dates d'abattage/ Dates of slaughter:")
    c.line(75*mm, 170*mm, 120*mm, 170*mm)
    c.drawString(80*mm, 171*mm, date_slaughter)
    c.drawString(125*mm, 170*mm, "Date de production:")
    c.line(160*mm, 170*mm, 195*mm, 170*mm)
    c.drawString(162*mm, 171*mm, date_production)

    # Section II
    c.setDash()
    c.setFont("Helvetica-Bold", 9)
    c.drawString(15*mm, 155*mm, "II. Provenance des viandes et produits à base de viande / Origin of meat and meat products:")
    c.setFont("Helvetica", 8)
    c.drawString(20*mm, 148*mm, "Abattoirs/Slaughter plants (adresses, départements et n° d'agrément / addresses, departments and approval numbers):")
    c.drawString(20*mm, 144*mm, "Voir annexe / See appendix")
    c.drawString(20*mm, 136*mm, "Ateliers de découpe / Cutting plants (adresses, départements et n° d'agrément / addresses, departments and approval numbers):")
    c.drawString(20*mm, 132*mm, "Voir annexe / See appendix")
    c.drawString(20*mm, 124*mm, "Ateliers de transformation / Processing plants (adresses, départements et n° d'agrément / addresses, departments and approval numbers):")
    c.drawString(20*mm, 120*mm, "Voir annexe / See appendix")

    # Section III
    c.setFont("Helvetica-Bold", 9)
    c.drawString(15*mm, 110*mm, "III. Destination des viandes et produits à base de viande / Destination of meat and meat products:")
    c.setFont("Helvetica", 9)
    c.drawString(20*mm, 103*mm, "Les viandes et produits à base de viande sont expédiés de / The meat and meat products are dispatched from:")
    c.drawString(20*mm, 95*mm, "(Lieu d'expédition / Place of Dispatch)..........................................................................")
    c.setFont("Helvetica-Bold", 10)
    c.drawString(80*mm, 96*mm, "94-RUNGIS")
    
    c.setFont("Helvetica", 9)
    c.drawString(20*mm, 87*mm, "À / To (Pays et Lieu de destination / Country and place of destination):")
    c.line(115*mm, 87*mm, 195*mm, 87*mm)
    c.setFont("Helvetica-Bold", 10)
    c.drawString(120*mm, 88*mm, "HONG KONG")

    c.setFont("Helvetica", 9)
    c.drawString(20*mm, 79*mm, "Par les moyens de transport suivant / By the following means of transport:")
    c.line(125*mm, 79*mm, 195*mm, 79*mm)
    c.setFont("Helvetica-Bold", 10)
    c.drawString(130*mm, 80*mm, "BY PLANE")

    c.setFont("Helvetica", 9)
    c.drawString(20*mm, 71*mm, "Nom et adresse de l'expéditeur / Name and address of consignor:")
    c.setFont("Helvetica-Bold", 9)
    c.drawString(20*mm, 66*mm, "SOCIETE HUGUENIN 32 Avenue de la Villette 94637 Rungis Cedex")

    c.setFont("Helvetica", 9)
    c.drawString(20*mm, 58*mm, "Nom et adresse du destinataire / Name and address of consignee:")
    c.setFont("Helvetica-Bold", 9)
    c.drawString(20*mm, 53*mm, "M&C ASIA LIMITED KWONG GA FACTORY BUILDING 17/F UNIT F 64 VICTORIA ROAD")
    c.drawString(20*mm, 48*mm, "KENNEDY TOWN HONG KONG")
    
    # Page 1 印章
    draw_blue_chop(c, x=120*mm, y=50*mm, vet_name=vet_name, chop_date=chop_date)

    c.setFont("Helvetica", 8)
    c.drawString(15*mm, 15*mm, "HK VPG AVR 14.doc")
    c.drawString(190*mm, 15*mm, "1/2")

    # ==========================================
    # PAGE 2: 衛生認證條款 
    # ==========================================
    c.showPage()
    
    c.setFont("Helvetica-Bold", 10)
    c.drawString(160*mm, 280*mm, f"CERTIFICAT N° {cert_number}")
    c.drawString(15*mm, 260*mm, "IV. ATTESTATION SANITAIRE / HEALTH CERTIFICATION:")
    
    c.setFont("Helvetica", 9)
    c.drawString(15*mm, 250*mm, "Je soussigné, vétérinaire officiel, certifie que / I, official veterinarian, hereby certify that:")
    
    text_y = 240
    line_height = 4
    
    lines = [
        "1- L'ensemble des viandes et produits est issu d'oiseaux qui ont été gardés dans un pays, une zone ou un compartiment",
        "indemne de maladie de Newcastle et d'Influenza aviaire à déclaration obligatoire (IADO) depuis leur éclosion ou depuis",
        "les 21 derniers jours:",
        "The entire consignment of meat/products derived from birds which had been kept in a Newcastle disease and notifiable",
        "avian influenza (NAI) free country, zone or compartment since they were hatched or for the past 21 days;",
        "Et/And",
        "2- Les oiseaux dont sont issus les viandes / produits ont été abattus dans des abattoirs agréés dans lesquels il n'y a pas eu",
        "de signes caractéristiques de l'IADO depuis 21 jours. Ils ont été soumis à une inspection ante et post mortem avec",
        "résultat favorable concernant l'IADO et d'autres maladies contagieuses. Les volailles ont été abattues dans un abattoir",
        "qui n'est pas situé dans une zone (circonscription administrative) infectée par la MNC ou l'IADO.",
        "The entire consignment of meat / products derived from birds which had been slaughtered in an approved abattoir in",
        "which there had been no evidence of NAI in the past 21 days. The birds had been subject to ante-mortem and post-",
        "mortem inspections for NAI and other contagious diseases with favourable results. The poultry were slaughtered in an",
        "abattoir not situated in a ND or NAI infected zone (administrative constituency).",
        "3- Les viandes / produits faisant l'objet du présent envoi sont propres à la consommation humaine, même à l'état cru.",
        "The meat/products of the current shipment are fit for human consumption, even in a raw state.",
        "4- L'établissement de provenance des viandes ou produits à base de viande est agréé pour l'exportation par les autorités",
        "françaises compétentes et inspecté par les vétérinaires inspecteurs officiels. Les viandes / produits ont été soumis à des",
        "tests de recherche de résidus de médicaments ou chimiques et organismes et substances pouvant être pathogenes pour",
        "l'être humain. Les résultats de ces tests sont en conformité avec les standards européens en vigueur.",
        "The processing plants from which meat / products originate have been authorised by the Government of France for",
        "exports and is inspected by official veterinary inspectors. The poultry meat / products have been subject to testing",
        "programmes for drug / chemical residues and harmful organisms and substances which may be harmful to human",
        "health. The results of the testing programmes meet the EU performance standards.",
        "5- Les viandes / produits ont été manipulés de façon à éviter tout risque de contamination jusqu'à l'embarquement. Le",
        "conditionnement et l'emballage des viandes/produits ont été réalisés à l'aide de matériaux agréés et propres.",
        "The exported meat / products have been handled in such ways as to keep it from being contaminated with any causative",
        "agents of animal infectious diseases until the shipment. Clean and sanitary wrapping and/or containers such as card",
        "board boxes shall be used to pack the exported meat/products.",
        "6- Les emballages portent une marque de salubrité prouvant que les viandes / produits proviennent d'établissements agréés.",
        "The cases carry a mark to prove that the meat/products come from approved plants."
    ]
    
    for line in lines:
        if line.startswith(str(tuple(range(1, 10)))): 
            text_y -= 2
        c.drawString(15*mm, text_y*mm, line)
        text_y -= line_height

    text_y -= 15
    c.drawString(15*mm, text_y*mm, "Fait à / Done at ..............................................................   Le / On the ..............................................................")
    c.setFont("Helvetica-Bold", 10)
    c.drawString(50*mm, (text_y+1)*mm, "RUNGIS")
    text_y -= 10
    c.setFont("Helvetica", 9)
    c.drawString(15*mm, text_y*mm, "Titre du signataire / Qualification")
    c.drawString(85*mm, text_y*mm, "Signature du vétérinaire officiel / Signature of the official veterinarian")
    text_y -= 5
    c.drawString(15*mm, text_y*mm, "Cachet officiel / Official stamp")

    # Page 2 印章
    draw_blue_chop(c, x=118*mm, y=28*mm, vet_name=vet_name, chop_date=chop_date)

    c.setFont("Helvetica", 8)
    c.drawString(15*mm, 15*mm, "HK VPG AVR 14.DOC")
    c.drawString(190*mm, 15*mm, "2/2")

    c.save()
    buffer.seek(0)
    return buffer

# ==========================
# Streamlit 界面
# ==========================
st.set_page_config(page_title="衛生證書生成系統", layout="centered")
st.title("📄 官方雙頁衛生證書生成器")

with st.form("cert_form"):
    st.subheader("基礎資訊 / Basic Information")
    cert_num_input = st.text_input("證書編號 (Certificate N°)", value="FR-094-26-0349818")
    
    col1, col2 = st.columns(2)
    with col1:
        species_input = st.selectbox("物種 (Species)", ["CAILLE", "PIGEONNEAU / PIGEON", "LAMB RACK"])
        packages_input = st.text_input("包裝數量 (Packages)", value="10 box")
        date_slaughter = st.text_input("屠宰日期 (Date of slaughter)", value="SEE ANNEXE")
    with col2:
        weight_input = st.text_input("總淨重 (Net Weight)", value="30KG")
        temp_input = st.text_input("儲存溫度 (Temperature)", value="+0 +4 °C")
        date_production = st.text_input("生產日期 (Date of production)", value="SEE ANNEXE")
        
    st.subheader("獸醫蓋章資訊 / Veterinarian Stamp")
    col3, col4 = st.columns(2)
    with col3:
        vet_name_input = st.selectbox("官方獸醫 (Official Veterinarian)", ["Dr Djamal OULDAROUS", "Dr Amal BELACEL", "Dr Mahmoud BENHARRATS"])
    with col4:
        chop_date_input = st.text_input("蓋章日期 (Chop Date)", value="01 Aug 2026")
        
    submitted = st.form_submit_button("生成帶蓋章 PDF (Generate PDF)")

if submitted:
    pdf_file = create_pdf(
        cert_num_input, species_input, weight_input, packages_input, 
        temp_input, date_slaughter, date_production, 
        vet_name_input, chop_date_input
    )
    st.success("✅ 渲染成功！程式錯誤已修復。")
    st.download_button(
        label="⬇️ 下載完整證書 (Download)",
        data=pdf_file,
        file_name=f"Certificate_{cert_num_input}.pdf",
        mime="application/pdf"
    )
