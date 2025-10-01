#!/usr/bin/env python3
"""
Guide for uploading files to Hugging Face Spaces manually
"""
import os
import webbrowser

def main():
    print("🚀 Manual Upload Guide for Hugging Face Spaces")
    print("=" * 50)
    
    print("\n📋 Step-by-Step Manual Upload:")
    print("1. Go to your Hugging Face Space: https://huggingface.co/spaces/Brianlimsun/digit-recognition-app")
    print("2. Click on the 'Files' tab")
    print("3. Click 'Add file' > 'Upload files'")
    print("4. Upload these files in this order:")
    
    files_to_upload = [
        "app.py",
        "requirements.txt", 
        "Dockerfile",
        "README.md",
        "index.html",
        "mnist_model.h5",
        "static/script.js",
        "static/style.css"
    ]
    
    for i, file in enumerate(files_to_upload, 1):
        if os.path.exists(file):
            print(f"   {i}. ✅ {file}")
        else:
            print(f"   {i}. ❌ {file} (not found)")
    
    print("\n5. After uploading all files, click 'Commit changes'")
    print("6. Your app will automatically build and deploy!")
    
    print(f"\n🌐 Your Space URL: https://huggingface.co/spaces/Brianlimsun/digit-recognition-app")
    
    # Open the space in browser
    try:
        webbrowser.open("https://huggingface.co/spaces/Brianlimsun/digit-recognition-app")
        print("\n🌐 Opening your Hugging Face Space in browser...")
    except:
        print("\n🌐 Please manually go to: https://huggingface.co/spaces/Brianlimsun/digit-recognition-app")
    
    print("\n✨ After uploading, your app will be live in 3-5 minutes!")

if __name__ == "__main__":
    main()
