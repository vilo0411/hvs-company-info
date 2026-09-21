import re
import sys
sys.stdout.reconfigure(encoding='utf-8')

forbidden_words = [
    "Trong thế giới không ngừng",
    "Mở khóa tiềm năng",
    "Hành trình",
    "Giải pháp toàn diện",
    "Đóng vai trò là",
    "Tóm lại,",
    "Kết luận là,",
    "Hãy cùng tìm hiểu",
    "Hiểu một cách đơn giản,",
    "Chúng tôi thấu hiểu rằng",
    "Đọc vị",
    "Nâng tầm",
    "Hơn cả một",
    "Đáng chú ý là,",
    "Tôi hy vọng thông tin này",
    "Bạn đã bao giờ tự hỏi",
    "HVS Có Thể Giúp Gì",
    "HVS Đồng Hành Cùng Bạn",
    "Định hình phương pháp",
    "Trang bị phương pháp",
    "Đánh dấu một bước ngoặt",
    "Thay đổi cuộc chơi",
    "Các chuyên gia tin rằng",
    "Nhiều người cho rằng",
    "Tương lai vẫn còn ở phía trước",
    "Chỉ có thời gian mới trả lời",
    "Để mà",
    "Do thực tế là",
    "Trong nỗ lực nhằm",
    "Nghệ thuật săn tìm",
    "Chữ cái vàng",
    "Giải mã",
    "tận dụng",
    "mạnh mẽ",
    "liền mạch",
    "đột phá",
    "cốt lõi",
    "hệ sinh thái",
    "nhịp đập thị trường",
    "nên",
    "cần",
    "có lẽ",
]

with open("content/blog/3-finalized/Final-cung-tien-la-gi.md", "r", encoding="utf-8") as f:
    lines = f.readlines()

for i, line in enumerate(lines):
    line_num = i + 1
    # Check for forbidden strings case-insensitively
    for fw in forbidden_words:
        if re.search(r'\b' + re.escape(fw) + r'\b', line, re.IGNORECASE):
            print(f"Line {line_num}: Found '{fw}' in: {line.strip()}")

    # Check for passive voice patterns like "được ... là", "được ... xem", "được ... cho", "được ... thực hiện"
    passive_patterns = [
        r'\bđược\b.*?\blà\b',
        r'\bđược\b.*?\bxem\b',
        r'\bđược\b.*?\bcho\b',
        r'\bđược\b.*?\bthực hiện\b'
    ]
    for pattern in passive_patterns:
        if re.search(pattern, line, re.IGNORECASE):
            print(f"Line {line_num}: Passive pattern matched in: {line.strip()}")

    # Check for English nominalization "việc [động từ]", "sự [tính từ]"
    nominalizations = [
        r'\bviệc\b\s+\w+',
        r'\bsự\b\s+\w+'
    ]
    for pattern in nominalizations:
        matches = re.findall(pattern, line, re.IGNORECASE)
        if matches:
            print(f"Line {line_num}: Nominalization candidate {matches} in: {line.strip()}")
