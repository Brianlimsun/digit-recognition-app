#!/usr/bin/env python3
"""
Script to check the deployment status of your Hugging Face Space
"""
import requests
import time
import webbrowser

def check_space_status():
    space_url = "https://huggingface.co/spaces/Brianlimsun/digit-recognition-app"
    
    print("🔍 Checking deployment status...")
    print(f"Space URL: {space_url}")
    
    try:
        response = requests.get(space_url, timeout=10)
        if response.status_code == 200:
            print("✅ Space is accessible!")
            print("🎉 Your digit recognition app is live!")
            print(f"🌐 Visit: {space_url}")
            
            # Open the space in browser
            webbrowser.open(space_url)
            return True
        else:
            print(f"⏳ Space is building... (Status: {response.status_code})")
            return False
    except requests.exceptions.RequestException as e:
        print(f"⏳ Space is still building or not ready yet...")
        return False

def main():
    print("🚀 Digit Recognition App - Deployment Checker")
    print("=" * 50)
    
    max_attempts = 10
    attempt = 0
    
    while attempt < max_attempts:
        attempt += 1
        print(f"\n🔄 Attempt {attempt}/{max_attempts}")
        
        if check_space_status():
            print("\n🎉 Deployment successful!")
            print("Your digit recognition app is now live and ready to use!")
            break
        else:
            if attempt < max_attempts:
                print("⏳ Waiting 30 seconds before next check...")
                time.sleep(30)
            else:
                print("\n⏰ Deployment is taking longer than expected.")
                print("Please check manually: https://huggingface.co/spaces/Brianlimsun/digit-recognition-app")
                print("The deployment usually takes 3-5 minutes.")

if __name__ == "__main__":
    main()
