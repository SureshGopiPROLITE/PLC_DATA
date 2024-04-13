# Read the content of the file
with open("Icons_reso_rc.py", "rb") as f:
    content = f.read()

# Remove null bytes
content_without_null_bytes = content.replace(b"\x00", b"")

# Write the modified content back to the file
with open("Icons_reso_rc.py", "wb") as f:
    f.write(content_without_null_bytes)
