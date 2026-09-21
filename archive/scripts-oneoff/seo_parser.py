import sys
import json
import re

# Force UTF-8 encoding for standard output to avoid UnicodeEncodeErrors on Windows
if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8')
if hasattr(sys.stderr, 'reconfigure'):
    sys.stderr.reconfigure(encoding='utf-8')

def extract_seo_data(html_content):
    """
    Script đơn giản để bóc tách H-tags và Meta Description từ nội dung HTML.
    Trong thực tế, AI có thể gọi script này sau khi dùng read_url_content.
    """
    data = {
        "title": "",
        "meta_description": "",
        "headings": {
            "h1": [],
            "h2": [],
            "h3": []
        }
    }
    
    # Tìm Title
    title_match = re.search(r'<title>(.*?)</title>', html_content, re.IGNORECASE)
    if title_match:
        data["title"] = title_match.group(1)
        
    # Tìm Meta Description
    meta_match = re.search(r'<meta name="description" content="(.*?)"', html_content, re.IGNORECASE)
    if meta_match:
        data["meta_description"] = meta_match.group(1)
        
    # Tìm Headings
    for level in ["h1", "h2", "h3"]:
        tags = re.findall(f'<{level}.*?>(.*?)</{level}>', html_content, re.IGNORECASE | re.DOTALL)
        data["headings"][level] = [re.sub(r'<.*?>', '', tag).strip() for tag in tags]
        
    return data

if __name__ == "__main__":
    # Script này sẽ được Agent gọi và truyền nội dung qua stdin hoặc file
    # Đây là bản demo logic xử lý thô
    pass
