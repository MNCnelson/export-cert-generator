import streamlit as st
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A4
from reportlab.lib.units import mm
import io
import os

def create_pdf(cert_number, species, weight, packages, temp, date_slaughter, date_production):
    buffer = io.BytesIO()
    c = canvas.Canvas(buffer, pagesize=A4)
    
    # ==========================================
    # PAGE 1: 货物标识与来源 (Section I, II, III)
    # ==========================================
    c.setFont("Helvetica-Bold", 9)
    # 绘制复选框和文字[cite: 7]
    c.rect(15*mm, 280*mm, 3*mm, 3*mm)
    c.drawString(20*mm, 280*mm, "DUPLICATA")
    c.rect(15*mm, 275*mm, 3*mm, 3*mm)
    c.drawString(20*mm, 275*mm, "ORIGINAL")
    
    c.setFont("Helvetica", 7)
    c.drawString(15*mm, 270*mm, "Nombre total de duplicatas délivrés / Total number of copies issued")
    
    # 加载官方 Logo (如果 GitHub 仓库里有 logo.png，就会自动画出来)
    if os.path.exists("logo.png"):
        c.drawImage("logo.png", 15*mm, 245*mm, width=25*mm, height=25*mm, preserveAspectRatio=True, mask='auto')

    c.setFont("Helvetica-Bold", 14)
    c.drawCentredString(105*mm, 280*mm, "REPUBLIQUE FRANCAISE")
    c.setFont("Helvetica-Bold", 10)
    c.drawCentredString(105*mm, 275*mm, "DIRECTION GENERALE DE L'ALIMENTATION")
    
    c.drawString(130*mm, 280*mm, f"CERTIFICAT N° /CERTIFICATE N° {cert_number}")
    
    c.setFont("Helvetica-Bold", 10)
    c.drawCentredString(105*mm, 260*mm, "CERTIFICAT POUR L'EXPORTATION A DESTINATION DE HONG KONG")
    c.drawCentredString(105*mm, 255*mm, "DE VIANDES FRAICHES DE GIBIER A PLUME, ET DE PRODUITS A BASE DE")
    c.drawCentredString(105*mm, 250*mm, "CES VIANDES EN PROVENANCE DE FRANCE")
    
    c.setFont("Helvetica", 9)
    c.drawCentredString(105*mm, 243*mm, "CERTIFICATE FOR EXPORTATION OF GAME BIRDS,")
    c.drawCentredString(105*mm, 238*mm, "AND THEIR PRODUCTS FROM FRANCE TO HONG KONG")

    # [Section I]
    c.setFont("Helvetica-Bold", 9)
    c.drawString(15*mm, 225*mm, "I. Identification des viandes et produits à base de viande / Identification of games birds and their products:")
    
    c.setFont("Helvetica", 9)
    c.drawString(20*mm, 217*mm, "a) Espèce animale / Species:")
    c.setDash(1, 2)
    c.line(65*mm, 217*mm, 195*mm, 217*mm)
    c.setFont("Helvetica-Bold", 10)
    c.drawString(70*mm, 218*mm, species) 
    
    c.setFont("Helvetica", 9)
    c.drawString(20*mm, 209*mm, "b) Nature des pièces / Nature of joints:")
    c.line(75*mm, 209*mm, 195*mm, 209*mm)
    c.drawString(80*mm, 210*mm, "SEE ANNEXE")
    
    c.drawString(20*mm, 201*mm, "c) Nombre de pièces ou d'unités d'emballage / Number of joints or packages:")
    c.line(135*mm, 201*mm, 195*mm, 201*mm)
    c.setFont("Helvetica-Bold", 10)
    c.drawString(140*mm, 202*mm, packages) 
    
    c.setFont("Helvetica", 9)
    c.drawString(20*mm, 193*mm, "d) Température d'entreposage / Temperature of storage:")
    c.line(100*mm, 193*mm, 140*mm, 193*mm)
    c.setFont("Helvetica-Bold", 10)
    c.drawString(105*mm, 194*mm, temp) 
    
    c.setFont("Helvetica", 9)
    c.drawString(145*mm, 193*mm, "e) Poids net/Net weight:")
    c.line(180*mm, 193*mm, 195*mm, 193*mm)
    c.setFont("Helvetica-Bold", 10)
    c.drawString(182*mm, 194*mm, weight) 
    
    c.setFont("Helvetica", 9)
    c.drawString(20*mm, 185*mm, "f) Dates d'abattage/ Dates of slaughter:")
    c.line(75*mm, 185*mm, 120*mm, 185*mm)
    c.drawString(80*mm, 186*mm, date_slaughter)
    c.drawString(125*mm, 185*mm, "Date de production:")
    c.line(160*mm, 185*mm, 195*mm, 185*mm)
    c.drawString(162*mm, 186*mm, date_production)

    # [Section II]
    c.setDash()
    c.setFont("Helvetica-Bold", 9)
    c.drawString(15*mm, 170*mm, "II. Provenance des viandes et produits à base de viande / Origin of meat and meat products:")
    c.setFont("Helvetica", 8)
    c.drawString(20*mm, 163*mm, "Abattoirs/Slaughter plants (adresses, départements et n° d'agrément / addresses, departments and approval numbers):")
    c.drawString(20*mm, 159*mm, "Voir annexe / See appendix")
    c.drawString(20*mm, 151*mm, "Ateliers de découpe / Cutting plants (adresses, départements et n° d'agrément / addresses, departments and approval numbers):")
    c.drawString(20*mm, 147*mm, "Voir annexe / See appendix")
    c.drawString(20*mm, 139*mm, "Ateliers de transformation / Processing plants (adresses, départements et n° d'agrément / addresses, departments and approval numbers):")
    c.drawString(20*mm, 135*mm, "Voir annexe / See appendix")

    # [Section III]
    c.setFont("Helvetica-Bold", 9)
    c.drawString(15*mm, 120*mm, "III. Destination des viandes et produits à base de viande / Destination of meat and meat products:")
    c.setFont("Helvetica", 9)
    c.drawString(20*mm, 113*mm, "Les viandes et produits à base de viande sont expédiés de / The meat and meat products are dispatched from:")
    c.drawString(20*mm, 105*mm, "(Lieu d'expédition / Place of Dispatch)..........................................................................")
    c.setFont("Helvetica-Bold", 10)
    c.drawString(80*mm, 106*mm, "94-RUNGIS")
    
    c.setFont("Helvetica", 9)
    c.drawString(20*mm, 97*mm, "À / To (Pays et Lieu de destination / Country and place of destination):")
    c.line(115*mm, 97*mm, 195*mm, 97*mm)
    c.setFont("Helvetica-Bold", 10)
    c.drawString(120*mm, 98*mm, "HONG KONG")

    c.setFont("Helvetica", 9)
    c.drawString(20*mm, 89*mm, "Par les moyens de transport suivant / By the following means of transport:")
    c.line(125*mm, 89*mm, 195*mm, 89*mm)
    c.setFont("Helvetica-Bold", 10)
    c.drawString(130*mm, 90*mm, "BY PLANE")

    c.setFont("Helvetica", 9)
    c.drawString(20*mm, 81*mm, "Nom et adresse de l'expéditeur / Name and address of consignor:")
    c.setFont("Helvetica-Bold", 9)
    c.drawString(20*mm, 76*mm, "SOCIETE HUGUENIN 32 Avenue de la Villette 94637 Rungis Cedex")

    c.setFont("Helvetica", 9)
    c.drawString(20*mm, 68*mm, "Nom et adresse du destinataire / Name and address of consignee:")
    c.setFont("Helvetica-Bold", 9)
    c.drawString(20*mm, 63*mm, "M&C ASIA LIMITED KWONG GA FACTORY BUILDING 17/F UNIT F 64 VICTORIA ROAD")
    c.drawString(20*mm, 58*mm, "KENNEDY TOWN HONG KONG")

    # 页脚[cite: 7]
    c.setFont("Helvetica", 8)
    c.drawString(15*mm, 15*mm, "HK VPG AVR 14.doc")
    c.drawString(190*mm, 15*mm, "1/2")

    # ==========================================
    # PAGE 2: 卫生认证条款 (Section IV)
    # ==========================================
    c.showPage() # 自动新建第二页
    
    c.setFont("Helvetica-Bold", 10)
    c.drawString(160*mm, 280*mm, f"CERTIFICAT N° {cert_number}")
    c.drawString(15*mm, 260*mm, "IV. ATTESTATION SANITAIRE / HEALTH CERTIFICATION:")
    
    c.setFont("Helvetica", 9)
    c.drawString(15*mm, 250*mm, "Je soussigné, vétérinaire officiel, certifie que / I, official veterinarian, hereby certify that:")
    
    text_y = 240
    line_height = 4
    
    # 逐条写入条款全文[cite: 7]
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
            text_y -= 2 # 段落间距
        c.drawString(15*mm, text_y*mm, line)
        text_y -= line_height

    # 签名区[cite: 7]
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

    # 页脚[cite: 7]
    c.setFont("Helvetica", 8)
    c.drawString(15*mm, 15*mm, "HK VPG AVR 14.DOC")
    c.drawString(190*mm, 15*mm, "2/2")

    c.save()
    buffer.seek(0)
    return buffer

# ==========================
# Streamlit 网页界面设计
# ==========================
st.set_page_config(page_title="卫生证书生成系统", layout="centered")

st.title("📄 官方双页卫生证书生成器")

with st.form("cert_form"):
    cert_num_input = st.text_input("证书编号 (Certificate N°)", value="FR-094-26-0349818")
    
    col1, col2 = st.columns(2)
    with col1:
        species_input = st.selectbox("物种 (Species)", ["CAILLE", "PIGEONNEAU / PIGEON", "LAMB RACK"])
        packages_input = st.text_input("包装数量 (Packages)", value="10 box")
        date_slaughter = st.text_input("屠宰日期 (Date of slaughter)", value="SEE ANNEXE")
    with col2:
        weight_input = st.text_input("总净重 (Net Weight)", value="30KG")
        temp_input = st.text_input("储存温度 (Temperature)", value="+0 +4 °C")
        date_production = st.text_input("生产日期 (Date of production)", value="SEE ANNEXE")
        
    submitted = st.form_submit_button("生成 PDF")

if submitted:
    pdf_file = create_pdf(cert_num_input, species_input, weight_input, packages_input, temp_input, date_slaughter, date_production)
    st.success("✅ 包含完整健康条款和 Logo 的双页 PDF 渲染成功！")
    st.download_button(
        label="⬇️ 下载完整双页证书",
        data=pdf_file,
        file_name=f"Certificate_{cert_num_input}.pdf",
        mime="application/pdf"
    )
