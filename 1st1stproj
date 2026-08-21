def calculate_combinations(current_gpa, target_gpa):
    total_credits = 120
    subject_credits = 3
    total_subjects = total_credits // subject_credits
    
    # Logic to find combinations of A (4.0) and B (3.0) subjects
    # that would result in the target GPA for the total 120 credits
    results = []
    found = False
    for a_grades in range(total_subjects + 1):
        for b_grades in range(total_subjects - a_grades + 1):
            # Calculate GPA based on current distribution of A and B grades
            current_calc = (a_grades * 4.0 * subject_credits + b_grades * 3.0 * subject_credits) / total_credits
            if abs(current_calc - target_gpa) < 0.02: # Tighter tolerance for accuracy
                results.append(f"{a_grades} môn loại A (4.0), {b_grades} môn loại B (3.0)")
                found = True
                break
        if len(results) >= 5: break

    if not found:
        return "Không tìm thấy tổ hợp A/B phù hợp cho mục tiêu này."
    
    return "\n".join(results)

with gr.Blocks(theme=gr.themes.Soft()) as demo:
    gr.Markdown("# 🎓 Máy tính tổ hợp điểm GPA (Tối đa 120 tín chỉ)")
    gr.Markdown("Giả định mỗi môn học là 3 tín chỉ.")
    
    with gr.Row():
        curr = gr.Slider(0, 4, value=2.0, label="GPA hiện tại")
        target = gr.Slider(0, 4, value=3.5, label="GPA mục tiêu")
    
    btn = gr.Button("Tìm tổ hợp môn cần thiết", variant="primary")
    out = gr.Textbox(label="Tổ hợp môn A và B có thể đạt được mục tiêu")
    
    btn.click(calculate_combinations, inputs=[curr, target], outputs=out)

# launch với share=True để tạo link công khai
demo.launch(share=True)
