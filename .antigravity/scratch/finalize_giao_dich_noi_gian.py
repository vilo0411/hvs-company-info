import os

draft_path = r"e:\project\hvs-company-info\content\blog\2-user-review\Draft-giao-dich-noi-gian-la-gi.md"
final_path = r"e:\project\hvs-company-info\content\blog\3-finalized\Final-giao-dich-noi-gian-la-gi.md"
outline_path = r"e:\project\hvs-company-info\content\blog\1-outlines\Outline-giao-dich-noi-gian-la-gi.md"

with open(draft_path, "r", encoding="utf-8") as f:
    content = f.read()

# Update YAML Status: Finalized
final_content = content.replace("Status: Draft", "Status: Finalized")

os.makedirs(os.path.dirname(final_path), exist_ok=True)
with open(final_path, "w", encoding="utf-8") as f:
    f.write(final_content)

print(f"Created {final_path}")

# Remove draft and outline if exists
if os.path.exists(draft_path):
    os.remove(draft_path)
    print(f"Removed {draft_path}")

if os.path.exists(outline_path):
    os.remove(outline_path)
    print(f"Removed {outline_path}")
