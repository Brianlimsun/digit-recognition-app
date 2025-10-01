#!/usr/bin/env python3
"""
Script to help deploy the digit recognition app to Hugging Face Spaces
"""
import os
import subprocess
import webbrowser
from pathlib import Path

def main():
    print("🚀 Hugging Face Spaces Deployment Helper")
    print("=" * 50)
    
    # Check if we're in the right directory
    if not os.path.exists("app.py") or not os.path.exists("mnist_model.h5"):
        print("❌ Error: Please run this script from the DigitRecognition directory")
        return
    
    print("✅ Project files found!")
    print("\n📋 Deployment Steps:")
    print("1. Go to https://huggingface.co/spaces")
    print("2. Click 'Create new Space'")
    print("3. Fill in the details:")
    print("   - Space name: digit-recognition-app")
    print("   - License: MIT")
    print("   - SDK: Docker")
    print("   - Hardware: CPU Basic")
    print("   - Visibility: Public")
    print("4. After creating, go to Settings > Repository")
    print("5. Connect to GitHub repository: Brianlimsun/digit-recognition-app")
    print("6. Your app will automatically deploy!")
    
    print(f"\n🌐 Your GitHub repository: https://github.com/Brianlimsun/digit-recognition-app")
    print(f"🎯 Your Hugging Face Space will be: https://huggingface.co/spaces/Brianlimsun/digit-recognition-app")
    
    # Open the Hugging Face Spaces page
    try:
        webbrowser.open("https://huggingface.co/spaces")
        print("\n🌐 Opening Hugging Face Spaces in your browser...")
    except:
        print("\n🌐 Please manually go to: https://huggingface.co/spaces")
    
    print("\n✨ Your app is ready for deployment!")
    print("The deployment will take 3-5 minutes to complete.")

if __name__ == "__main__":
    main()
