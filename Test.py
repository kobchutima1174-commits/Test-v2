import streamlit as st
import pandas as pd
import os
from PIL import Image

# ตั้งค่าหน้าเว็บ
st.set_page_config(page_title="แบบสอบถามชุดครุย KPRU", layout="centered")

# ฟังก์ชันสำหรับบันทึกข้อมูล
def save_data(data):
    file_path = 'survey_results.csv'
    df = pd.DataFrame([data])
    if not os.path.isfile(file_path):
        df.to_csv(file_path, index=False, encoding='utf-8-sig')
    else:
        df.to_csv(file_path, mode='a', header=False, index=False, encoding='utf-8-sig')

st.title("แบบสอบถามการปรับแบบชุดครุย KPRU")
st.write("วัตถุประสงค์: เพื่อรวบรวมความเห็นเกี่ยวกับการพัฒนาชุดครุยให้ทันสมัย")

st.header("ส่วนที่ 1: ข้อมูลทั่วไป")
status = st.selectbox("สถานะ", ["อาจารย์", "นักศึกษา", "นักเรียน", "บัณฑิต"])
department = st.text_input("คณะ/สาขา")
gender = st.radio("เพศ", ["ชาย", "หญิง", "อื่น ๆ"], horizontal=True)

st.header("ส่วนที่ 2: ความคิดเห็นต่อรูปแบบชุดครุย")
score_map = {"ชอบมาก": 3, "ชอบ": 2, "ปานกลาง": 1, "ไม่ชอบ": 0}

col1, col2, col3, col4, col5, col6 = st.columns(6)
with col1:
    st.subheader("1. พิบูลสงคราม")
    st.image("Image/Pibulsongkram.png", use_container_width=True)
    choice1 = st.radio("ระดับความชอบ (1)", ["ชอบมาก", "ชอบ", "ปานกลาง"], key="c1")

with col2:
    st.subheader("2. กำแพงเพชร")
    st.image("Image/KamphaengPhet.jpeg", use_container_width=True)
    choice2 = st.radio("ระดับความชอบ (2)", ["ชอบมาก", "ชอบ", "ปานกลาง"], key="c2")

with col3:
    st.subheader("3. เชียงใหม่")
    st.image("Image/ChiangMai.jpeg", use_container_width=True)
    choice3 = st.radio("ระดับความชอบ (3)", ["ชอบมาก", "ชอบ", "ไม่ชอบ"], key="c3")

with col4:
    st.subheader("4. เกษตรศาสตร์")
    st.image("Image/Kasetsart.jpeg", use_container_width=True)
    choice4 = st.radio("ระดับความชอบ (4)", ["ชอบมาก", "ชอบ", "ไม่ชอบ"], key="c4")

with col5:
    st.subheader("5. จุฬา")
    st.image("Image/Chula.png", use_container_width=True)
    choice5 = st.radio("ระดับความชอบ (5)", ["ชอบมาก", "ชอบ", "ไม่ชอบ"], key="c5")

with col6:
    st.subheader("6. แม่ฟ้าหลวง")
    st.image("Image/MFU.jpeg", use_container_width=True)
    choice6 = st.radio("ระดับความชอบ (6)", ["ชอบมาก", "ชอบ", "ไม่ชอบ"], key="c6")

if st.button("ส่งข้อมูล"):
    respondent_data = {
        "status": status,
        "department": department,
        "gender": gender,
        "Pibul_score": score_map[choice1],
        "Kamphaeng_score": score_map[choice2],
        "ChiangMai_score": score_map[choice3],
        "Kasetsart_score": score_map[choice4],
        "Chula_score": score_map[choice5],
        "MFU_score": score_map[choice6]
    }
    save_data(respondent_data)
    st.success("บันทึกข้อมูลเรียบร้อยแล้ว!")

st.divider()
st.header("📊 สรุปลำดับความชอบในขณะนี้")

if os.path.exists('survey_results.csv'):
    results = pd.read_csv('survey_results.csv')
    avg_scores = {
        "พิบูลสงคราม": results['Pibul_score'].mean(),
        "กำแพงเพชร": results['Kamphaeng_score'].mean(),
        "เชียงใหม่": results['ChiangMai_score'].mean(),
        "เกษตรศาสตร์": results['Kasetsart_score'].mean(),
        "จุฬา": results['Chula_score'].mean(),
        "แม่ฟ้าหลวง": results['MFU_score'].mean()
    }
    sorted_ranking = sorted(avg_scores.items(), key=lambda x: x[1], reverse=True)
    for i, (name, score) in enumerate(sorted_ranking, 1):
        st.write(f"ลำดับที่ {i}: **{name}** (คะแนนเฉลี่ย: {score:.2f})")
else:
    st.info("ยังไม่มีข้อมูลการตอบกลับ")