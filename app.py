import streamlit as st

def calculate_combinations(target_gpa):
    total_credits = 120
    subject_credits = 3
    total_subjects = total_credits // subject_credits
    
    results = []
    found = False
    for a_grades in range(total_subjects + 1):
        for b_grades in range(total_subjects - a_grades + 1):
            current_calc = (a_grades * 4.0 * subject_credits + b_grades * 3.0 * subject_credits) / total_credits
            if abs(current_calc - target_gpa) < 0.02:
                results.append(f"{a_grades} môn loại A (4.0), {b_grades} môn loại B (3.0)")
                found = True
                break
        if len(results) >= 5: break
    return results

st.set_page_config(page_title="GPA Calculator", page_icon="🎓")

st.title("🎓 Máy tính tổ hợp điểm GPA")
st.write("Tối đa 120 tín chỉ - Giả định mỗi môn 3 tín chỉ")

target = st.slider("GPA mục tiêu", 0.0, 4.0, 3.5, 0.1)

if st.button("Tìm tổ hợp môn cần thiết"):
    combinations = calculate_combinations(target)
    if combinations:
        st.success("Các tổ hợp môn A và B có thể đạt được mục tiêu:")
        for combo in combinations:
            st.write(f"- {combo}")
    else:
        st.error("Không tìm thấy tổ hợp A/B phù hợp cho mục tiêu này.")

st.info("Ghi chú: Đây là mô hình tính toán dựa trên tổng số 120 tín chỉ.")
