import streamlit as st
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A4
from reportlab.lib.units import mm
import io

def create_pdf(cert_number, species, weight, packages, temp):
    buffer = io.BytesIO()
    c = canvas.Canvas(buffer, pagesize=A4)
    
    # ==========================================
    # 表头部分 (Header)
    # ==========================================
    c.setFont("Helvetica-Bold", 9)
    c.drawString(15*mm, 280*mm, "DUPLICATA")
    c.drawString(15*mm, 276*mm, "ORIGINAL")
    c.setFont("Helvetica", 7)
    c.drawString(15*mm, 272*mm, "Nombre total de duplicatas délivrés/Total number of copies issued")
    
    c.setFont("Helvetica-Bold", 14)
    c.drawCentredString(105*mm, 280*mm, "REPUBLIQUE FRANCAISE")
    c.setFont("Helvetica-Bold", 10)
    c.drawCentredString(105*mm, 275*mm, "DIRECTION GENERALE DE L'ALIMENTATION")
    
    # 动态插入证书号
    c.setFont("Helvetica-Bold", 10)
    c.drawString(130*mm, 280*mm, f"CERTIFICAT N° /CERTIFICATE N° {cert_number}")
    
    c.setFont("Helvetica-Bold", 10)
    c.drawCentredString(105*mm, 265*mm, "CERTIFICAT POUR L'EXPORTATION A DESTINATION DE HONG KONG")
    c.drawCentredString(105*mm, 260*mm, "DE VIANDES FRAICHES DE GIBIER A PLUME, ET DE PRODUITS A BASE DE")
    c.drawCentredString(105*mm, 255*mm, "CES VIANDES EN PROVENANCE DE FRANCE")
    
    c.setFont("Helvetica", 9)
    c.drawCentredString(105*mm, 248*mm, "CERTIFICATE FOR EXPORTATION OF GAME BIRDS,")
    c.drawCentredString(105*mm, 243*mm, "AND THEIR PRODUCTS FROM FRANCE TO HONG KONG")

    # ==========================================
    # 第一部分: 货物标识 (Section I)
    # ==========================================
    c.setFont("Helvetica-Bold", 9)
    c.drawString(15*mm, 230*mm, "I. Identification des viandes et produits à base de viande / Identification of games birds and their products:")
    
    c.setFont("Helvetica", 9)
    # a) 物种
    c.drawString(20*mm, 222*mm, "a) Espèce animale / Species :")
    c.setDash(1, 2)
    c.line(65*mm, 222*mm, 195*mm, 222*mm)
    c.setFont("Helvetica-Bold", 10)
    c.drawString(70*mm, 223*mm, species) # 动态数据
    
    # b) 部位
    c.setFont("Helvetica", 9)
    c.drawString(20*mm, 214*mm, "b) Nature des pièces / Nature of joints :")
    c.line(75*mm, 214*mm, 195*mm, 214*mm)
    c.drawString(80*mm, 215*mm, "SEE ANNEXE")
    
    # c) 包装数量
    c.drawString(20*mm, 206*mm, "c) Nombre de pièces ou d'unités d'emballage / Number of joints or packages :")
    c.line(135*mm, 206*mm, 195*mm, 206*mm)
    c.setFont("Helvetica-Bold", 10)
    c.drawString(140*mm, 207*mm, packages) # 动态数据
    
    # d) 储存温度 与 e) 净重
    c.setFont("Helvetica", 9)
    c.drawString(20*mm, 198*mm, "d) Température d'entreposage / Temperature of storage :")
    c.line(100*mm, 198*mm, 140*mm, 198*mm)
    c.setFont("Helvetica-Bold", 10)
    c.drawString(105*mm, 199*mm, temp) # 动态数据
    
    c.setFont("Helvetica", 9)
    c.drawString(145*mm, 198*mm, "e) Poids net/Net weight :")
    c.line(180*mm, 198*mm, 195*mm, 198*mm)
    c.setFont("Helvetica-Bold", 10)
    c.drawString(182*mm, 199*mm, weight) # 动态数据
    
    # f) 日期
    c.setFont("Helvetica", 9)
    c.drawString(20*mm, 190*mm, "f) Dates d'abattage/ Dates of slaughter:")
    c.line(75*mm, 190*mm, 120*mm, 190*mm)
    c.drawString(80*mm, 191*mm, "SEE ANNEXE")
    c.drawString(125*mm, 190*mm, "Date de production / Date of production:")
    c.line(180*mm, 190*mm, 195*mm, 190*mm)
    c.drawString(180*mm, 191*mm, "SEE ANNEXE")

    # ==========================================
    # 第二部分: 来源地 (Section II)
    # ==========================================
    c.setDash() # 恢复实线
    c.setFont("Helvetica-Bold", 9)
    c.drawString(15*mm, 175*mm, "II. Provenance des viandes et produits à base de viande / Origin of meat and meat products:")
    
    c.setFont("Helvetica", 8)
    c.drawString(20*mm, 168*mm, "Abattoirs/Slaughter plants (adresses, départements et n° d'agrément / addresses, departments and approval numbers):")
    c.drawString(20*mm, 164*mm, "Voir annexe / See appendix")
    
    c.drawString(20*mm, 156*mm, "Ateliers de découpe / Cutting plants (adresses, départements et n° d'agrément / addresses, departments and approval numbers):")
    c.drawString(20*mm, 152*mm, "Voir annexe / See appendix")

    c.drawString(20*mm, 144*mm, "Ateliers de transformation / Processing plants (adresses, départements et n° d'agrément addresses, departments and approval numbers):")
    c.drawString(20*mm, 140*mm, "Voir annexe / See appendix")

    # ==========================================
    # 第三部分: 目的地 (Section III)
    # ==========================================
    c.setFont("Helvetica-Bold", 9)
    c.drawString(15*mm, 130*mm, "III. Destination des viandes et produits à base de viande / Destination of meat and meat products:")
    
    c.setFont("Helvetica", 9)
    c.drawString(20*mm, 123*mm, "Les viandes et produits à base de viande sont expédiés de / The meat and meat products are dispatched from :")
    
    c.drawString(20*mm, 115*mm, "(Lieu d'expédition / Place of Dispatch)..........................................................................")
    c.setFont("Helvetica-Bold", 10)
    c.drawString(80*mm, 116*mm, "94-RUNGIS")
    
    c.setFont("Helvetica", 9)
    c.drawString(20*mm, 107*mm, "À / To (Pays et Lieu de destination / Country and place of destination):")
    c.line(115*mm, 107*mm, 195*mm, 107*mm)
    c.setFont("Helvetica-Bold", 10)
    c.drawString(120*mm, 108*mm, "HONG KONG")

    c.setFont("Helvetica", 9)
    c.drawString(20*mm, 99*mm, "Par les moyens de transport suivant / By the following means of transport:")
    c.line(125*mm, 99*mm, 195*mm, 99*mm)
    c.setFont("Helvetica-Bold", 10)
    c.drawString(130*mm, 100*mm, "BY PLANE")

    c.setFont("Helvetica", 9)
    c.drawString(20*mm, 91*mm, "Nom et adresse de l'expéditeur / Name and address of consignor:")
    c.setFont("Helvetica-Bold", 9)
    c.drawString(20*mm, 86*mm, "SOCIETE HUGUENIN 32 Avenue de la Villette 94637 Rungis Cedex")

    c.setFont("Helvetica", 9)
    c.drawString(20*mm, 78*mm, "Nom et adresse du destinataire / Name and address of consignee :")
    c.setFont("Helvetica-Bold", 9)
    c.drawString(20*mm, 73*mm, "M&C ASIA LIMITED KWONG GA FACTORY BUILDING 17/F UNIT F 64 VICTORIA ROAD")
    c.drawString(20*mm, 68*mm, "KENNEDY TOWN HONG KONG")

    c.save()
    buffer.seek(0)
    return buffer

# ==========================
# Streamlit 网页界面设计
# ==========================
st.set_page_config(page_title="卫生证书生成系统", layout="centered")

st.title("📄 官方卫生证书生成器")

with st.form("cert_form"):
    cert_num_input = st.text_input("证书编号 (Certificate N°)", value="FR-094-26-0349827")
    
    col1, col2 = st.columns(2)
    with col1:
        species_input = st.selectbox("物种 (Species)", ["PIGEONNEAU / PIGEON", "LAMB RACK"])
        packages_input = st.text_input("包装数量 (Packages)", value="3 BOX")
    with col2:
        weight_input = st.text_input("总净重 (Net Weight)", value="18.00KG")
        temp_input = st.text_input("储存温度 (Temperature)", value="+ 0 + 4 °C")
        
    submitted = st.form_submit_button("生成 PDF")

if submitted:
    pdf_file = create_pdf(cert_num_input, species_input, weight_input, packages_input, temp_input)
    st.success("✅ PDF 渲染成功！请点击下方按钮下载。")
    st.download_button(
        label="⬇️ 下载完整排版证书",
        data=pdf_file,
        file_name=f"Certificate_{cert_num_input}.pdf",
        mime="application/pdf"
    )
