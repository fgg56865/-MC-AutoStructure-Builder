import os
import zipfile
import time

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def get_code_from_user(menu_title):
    clear_screen()
    print("=" * 50)
    print(f"  {menu_title}")
    print("=" * 50)
    
    proj_name = input("প্রজেক্টের নাম দিন (যেমন: MyProject): ").strip()
    if not proj_name:
        proj_name = "Minecraft_Project"
        
    print("\n[!] আপনার কোড বা রিকোয়ারমেন্ট এখানে পেস্ট করুন।")
    print("[!] লেখা শেষ হলে নতুন লাইনে একটি ডট (.) দিয়ে এন্টার প্রেস করুন:\n")
    
    lines = []
    while True:
        try:
            line = input()
            if line.strip() == ".":
                break
            lines.append(line)
        except EOFError:
            break
            
    raw_code = "\n".join(lines)
    
    print("\n[!] কোড গ্রহণ করা হয়েছে। এন্টার প্রেস করে জিপ ফাইল তৈরি শুরু করুন...")
    input()
    print("Wait please, zip file is creating...")
    time.sleep(1.5)
    
    return proj_name, raw_code

def build_mod_files():
    proj_name, code = get_code_from_user("MOD FILE CREATE MENU")
    try:
        base_dir = "temp_workspace"
        proj_root = os.path.join(base_dir, proj_name)
        download_dir = "/storage/emulated/0/Download"
        
        # মাইনক্রাফট মোড বানানোর অফিশিয়াল ফোল্ডার স্ট্রাকচার
        os.makedirs(os.path.join(proj_root, "src/main/java/com/custom/mod/proxy"), exist_ok=True)
        os.makedirs(os.path.join(proj_root, "src/main/resources/assets/custommod/lang"), exist_ok=True)
        os.makedirs(os.path.join(proj_root, "src/main/resources/assets/custommod/textures/items"), exist_ok=True)
        os.makedirs(os.path.join(proj_root, "src/main/resources/assets/custommod/textures/blocks"), exist_ok=True)
        
        # ফাইলে কোড বা মেইন লজিক রাইট করা
        with open(os.path.join(proj_root, "src/main/resources/mcmod.info"), "w", encoding="utf-8") as f:
            f.write(code if code else '{\n  "modid": "custommod",\n  "name": "Custom Mod"\n}')
            
        with open(os.path.join(proj_root, "src/main/java/com/custom/mod/Main.java"), "w", encoding="utf-8") as f:
            f.write("// Your Mod Main Logic Code\n" + code)

        os.makedirs(download_dir, exist_ok=True)
        zip_filename = os.path.join(download_dir, f"{proj_name}.zip")
        
        with zipfile.ZipFile(zip_filename, 'w', zipfile.ZIP_DEFLATED) as zipf:
            for root, dirs, files in os.walk(proj_root):
                for file in files:
                    fp = os.path.join(root, file)
                    zipf.write(fp, os.path.relpath(fp, proj_root))
                    
        print(f"\nSuccessfully download folder save in! Please checking the file.")
        print(f"Path: {zip_filename}\n")
    except Exception as e:
        print(f"\nFAILED! Error: {e}\n")
    input("মেনুতে ফিরে যেতে এন্টার প্রেস করুন...")

def build_texture_files():
    proj_name, code = get_code_from_user("TEXTURE PACK CREATE MENU")
    try:
        base_dir = "temp_workspace"
        proj_root = os.path.join(base_dir, proj_name)
        download_dir = "/storage/emulated/0/Download"
        
        # টেক্সচার প্যাক বানানোর সমস্ত দরকারি ফোল্ডার স্ট্রাকচার
        os.makedirs(os.path.join(proj_root, "assets/minecraft/textures/block"), exist_ok=True)
        os.makedirs(os.path.join(proj_root, "assets/minecraft/textures/item"), exist_ok=True)
        os.makedirs(os.path.join(proj_root, "assets/minecraft/textures/entity/player/wide"), exist_ok=True)
        os.makedirs(os.path.join(proj_root, "assets/minecraft/textures/entity/player/slim"), exist_ok=True)
        os.makedirs(os.path.join(proj_root, "assets/minecraft/textures/gui"), exist_ok=True)
        os.makedirs(os.path.join(proj_root, "assets/minecraft/optifine/cit"), exist_ok=True)
        
        # প্যাক ফাইল ও কোড রাইট করা
        with open(os.path.join(proj_root, "pack.mcmeta"), "w", encoding="utf-8") as f:
            f.write('{\n  "pack": {\n    "pack_format": 3,\n    "description": "Custom Texture Pack"\n  }\n}')
            
        with open(os.path.join(proj_root, "texture_code_notes.txt"), "w", encoding="utf-8") as f:
            f.write(code if code else "No custom code provided.")

        os.makedirs(download_dir, exist_ok=True)
        zip_filename = os.path.join(download_dir, f"{proj_name}.zip")
        
        with zipfile.ZipFile(zip_filename, 'w', zipfile.ZIP_DEFLATED) as zipf:
            for root, dirs, files in os.walk(proj_root):
                for file in files:
                    fp = os.path.join(root, file)
                    zipf.write(fp, os.path.relpath(fp, proj_root))
                    
        print(f"\nSuccessfully download folder save in! Please checking the file.")
        print(f"Path: {zip_filename}\n")
    except Exception as e:
        print(f"\nFAILED! Error: {e}\n")
    input("মেনুতে ফিরে যেতে এন্টার প্রেস করুন...")

def build_shader_files():
    proj_name, code = get_code_from_user("SHADER PACK CREATE MENU")
    try:
        base_dir = "temp_workspace"
        proj_root = os.path.join(base_dir, proj_name)
        download_dir = "/storage/emulated/0/Download"
        
        # সেডার প্যাক বানানোর সমস্ত ফোল্ডার স্ট্রাকচার
        os.makedirs(os.path.join(proj_root, "shaders/world0"), exist_ok=True)
        os.makedirs(os.path.join(proj_root, "shaders/world1"), exist_ok=True)
        os.makedirs(os.path.join(proj_root, "shaders/world-1"), exist_ok=True)
        
        with open(os.path.join(proj_root, "shaders/shaders.properties"), "w", encoding="utf-8") as f:
            f.write("version=1\nprofile=custom_shader")
            
        with open(os.path.join(proj_root, "shaders/composite.fsh"), "w", encoding="utf-8") as f:
            f.write("// Shader Code\n" + (code if code else ""))

        os.makedirs(download_dir, exist_ok=True)
        zip_filename = os.path.join(download_dir, f"{proj_name}.zip")
        
        with zipfile.ZipFile(zip_filename, 'w', zipfile.ZIP_DEFLATED) as zipf:
            for root, dirs, files in os.walk(proj_root):
                for file in files:
                    fp = os.path.join(root, file)
                    zipf.write(fp, os.path.relpath(fp, proj_root))
                    
        print(f"\nSuccessfully download folder save in! Please checking the file.")
        print(f"Path: {zip_filename}\n")
    except Exception as e:
        print(f"\nFAILED! Error: {e}\n")
    input("মেনুতে ফিরে যেতে এন্টার প্রেস করুন...")

def chatbot_menu():
    proj_name, code = get_code_from_user("CHATBOT SMART BUILDER MENU")
    try:
        base_dir = "temp_workspace"
        proj_root = os.path.join(base_dir, proj_name)
        download_dir = "/storage/emulated/0/Download"
        
        # চ্যাটবট মোডের জন্য অল-ইন-ওয়ান কম্বিনেশন ফোল্ডার
        os.makedirs(os.path.join(proj_root, "src/main/java"), exist_ok=True)
        os.makedirs(os.path.join(proj_root, "assets/minecraft/textures/items"), exist_ok=True)
        os.makedirs(os.path.join(proj_root, "shaders"), exist_ok=True)
        
        with open(os.path.join(proj_root, "chatbot_instructions.txt"), "w", encoding="utf-8") as f:
            f.write(code if code else "Chatbot requirement notes.")

        os.makedirs(download_dir, exist_ok=True)
        zip_filename = os.path.join(download_dir, f"{proj_name}.zip")
        
        with zipfile.ZipFile(zip_filename, 'w', zipfile.ZIP_DEFLATED) as zipf:
            for root, dirs, files in os.walk(proj_root):
                for file in files:
                    fp = os.path.join(root, file)
                    zipf.write(fp, os.path.relpath(fp, proj_root))
                    
        print(f"\nSuccessfully download folder save in! Please checking the file.")
        print(f"Path: {zip_filename}\n")
    except Exception as e:
        print(f"\nFAILED! Error: {e}\n")
    input("মেনুতে ফিরে যেতে এন্টার প্রেস করুন...")

def main_menu():
    while True:
        clear_screen()
        print("=" * 50)
        print("     MINECRAFT AUTO BUILDER (TERMUX EDITION)")
        print("=" * 50)
        print(" 1. Mod File Create")
        print(" 2. Texture Pack Create")
        print(" 3. Shader Pack Create")
        print(" 4. Chatbot Smart Builder")
        print(" 5. Exit")
        print("=" * 50)
        
        choice = input("Select an option (1-5): ").strip()
        
        if choice == '1':
            build_mod_files()
        elif choice == '2':
            build_texture_files()
        elif choice == '3':
            build_shader_files()
        elif choice == '4':
            chatbot_menu()
        elif choice == '5':
            print("\nটার্মাক্স টুল থেকে বের হয়ে আসা হলো।")
            break
        else:
            input("\n[❌] ভুল অপশন! এন্টার প্রেস করে আবার চেষ্টা করুন...")

if __name__ == "__main__":
    main_menu()
      