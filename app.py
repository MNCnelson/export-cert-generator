import streamlit as st
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A4
from reportlab.lib.units import mm
import io

def create_pdf(species, weight, cert_number):
    # 使用 io.BytesIO 在内存中生成 PDF
    buffer = io.BytesIO()
    c = canvas.Canvas(buffer, pagesize=A4)
    
    # --- 绘制静态模板 (基于之前沟通的排版) ---
    c.setFont("Helvetica-Bold", 14)
    c.drawCentredString(105*mm, 280*mm, "REPUBLIQUE FRANCAISE")
    c.setFont("Helvetica", 10)
    c.drawString(15*mm, 220*mm, "I. Identification des viandes et produits / Identification:")
    c.drawString(20*mm, 210*mm, "a) Espèce animale / Species :")
    c.drawString(20*mm, 200*mm, "e) Poids net/Net weight :")
    c.line(70*mm, 210*mm, 195*mm, 210*mm) # 虚线或实线
    
    # --- 填入表单动态数据 ---
    c.setFont("Helvetica-Bold", 11)
    c.drawString(135*mm, 280*mm, f"CERTIFICAT N° : {cert_number}")
    c.drawString(75*mm, 210*mm, species)
    c.drawString(75*mm, 200*mm, weight)
    
    c.save()
    buffer.seek(0)
    return buffer

# ==========================
# Streamlit 网页界面设计
# ==========================
st.set_page_config(page_title="卫生证书生成系统", layout="centered")

st.title("📄 官方卫生证书与装箱单生成器")
st.markdown("填写下方信息，系统将自动生成符合格式的法国出口卫生证书 PDF。")

# 使用表单组件整理输入区
with st.form("cert_form"):
    cert_num_input = st.text_input("证书编号 (Certificate N°)", value="FR-094-26-0349827")
    
    col1, col2 = st.columns(2)
    with col1:
        species_input = st.selectbox("物种 (Species)", ["PIGEONNEAU / PIGEON", "LAMB RACK"])
    with col2:
        weight_input = st.text_input("总净重 (Net Weight)", value="18.00KG")
        
    submitted = st.form_submit_button("生成并预览 PDF")

# 处理表单提交并提供下载
if submitted:
    pdf_file = create_pdf(species_input, weight_input, cert_num_input)
    
    st.success("✅ PDF 渲染成功！请点击下方按钮下载。")
    st.download_button(
        label="⬇️ 下载证书 PDF",
        data=pdf_file,
        file_name=f"Certificate_{cert_num_input}.pdf",
        mime="application/pdf"
    )
