import os
import re

directory = "./servers/nextjs/app/(presentation-generator)/custom-template/components"

replacements = {
    # Light backgrounds
    r"bg-\[#FEFEFF\]": "bg-[#000000]",
    r"bg-\[#FAFAFF\]": "bg-[#1d1d1d]",
    r"bg-\[#F6F6F9\]": "bg-[#1d1d1d]",
    r"bg-\[#FAFAFA\]": "bg-[#1d1d1d]",
    r"bg-white": "bg-[#000000]",
    
    # Gradients / Purples
    r"bg-\[#EBE9FE\]": "bg-[#383838]",
    r"bg-\[#7A5AF8\]": "bg-[#ffffff]",
    r"text-\[#7A5AF8\]": "text-[#ffffff]",
    r"text-\[#5B49A1\]": "text-[#ffffff]",
    r"text-\[#20165C\]": "text-[#ffffff]",
    r"text-\[#5246C3\]": "text-[#ffffff]",
    r"bg-gradient-to-br from-\[#EBE9FE\] to-\[#DDD6FE\]": "bg-[#383838]",
    r"bg-gradient-to-r from-\[#FAFAFA\] to-card": "bg-[#1d1d1d]",
    r"from-violet-500 to-purple-600": "from-[#383838] to-[#1d1d1d]",
    r"hover:from-violet-600 hover:to-purple-700": "hover:from-[#1d1d1d] hover:to-[#000000]",
    r"hover:text-violet-600": "hover:text-[#ffffff]",
    r"hover:text-emerald-600": "hover:text-[#ffffff]",
    r"hover:text-blue-600": "hover:text-[#ffffff]",
    r"hover:text-indigo-600": "hover:text-[#ffffff]",
    r"hover:text-amber-600": "hover:text-[#ffffff]",
    r"hover:bg-red-50 hover:border-red-200 hover:text-red-500": "hover:bg-[#383838] hover:border-[#ffffff] hover:text-[#ffffff]",
    r"border-\[#FECACA\] text-\[#DC2626\]": "border-[#383838] text-[#ffffff]",
    r"hover:bg-\[#FEE2E2\]": "hover:bg-[#383838]",
    
    # Borders
    r"border-\[#EDEEEF\]": "border-[#383838]",
    r"border-\[#EBE9FE\]": "border-[#383838]",
    r"border-\[#B8B8C1\]": "border-[#383838]",
    r"border-\[#E5E7EB\]": "border-[#383838]",
    r"border-\[#D1FAE5\]": "border-[#383838]",
    r"border-\[#FDE68A\]": "border-[#383838]",
    r"border-\[#F3F4F6\]": "border-[#383838]",
    r"border-slate-\w+": "border-[#383838]",
    
    # Texts
    r"text-\[#4C4C4C\]": "text-[#ffffff]",
    r"text-\[#808080\]": "text-[#888888]",
    r"text-\[#3A3A3A\]": "text-[#888888]",
    r"text-\[#9A9AA6\]": "text-[#888888]",
    r"text-\[#166534\]": "text-[#ffffff]",
    r"text-\[#374151\]": "text-[#ffffff]",
    
    # Complex inline styles (Regex with single quotes)
    r"background: 'radial-gradient[^']+'": "background: '#000000'",
    r"boxShadow: '0 0 16px 0 rgba\(80, 71, 230, 0.12\)'": "border: '1px solid #383838'",
    r"boxShadow: '0 0 4px 0 rgba\(0, 0, 0, 0.06\)'": "border: '1px solid #383838'",
    r"background: 'linear-gradient\(270deg, #D5CAFC[^']+'": "background: '#ffffff', color: '#000000'",
    r"background: 'linear-gradient\(90deg, #7A5AF8[^']+'": "background: '#ffffff'",
    r"background: 'linear-gradient\(135deg, #D5CAFC[^']+'": "background: '#ffffff'",
    r"backgroundImage: 'linear-gradient\(45deg[^']+'": "backgroundImage: 'none'",
}

for root, _, files in os.walk(directory):
    for file in files:
        if file.endswith((".tsx", ".ts")):
            filepath = os.path.join(root, file)
            with open(filepath, "r") as f:
                content = f.read()
            
            original = content
            for pattern, replacement in replacements.items():
                content = re.sub(pattern, replacement, content)
                
            if original != content:
                with open(filepath, "w") as f:
                    f.write(content)
                print(f"Updated {filepath}")
