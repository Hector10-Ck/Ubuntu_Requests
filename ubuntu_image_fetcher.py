import os
import requests
from urllib.parse import urlparse

def fetch_image():
    print("🌍 The Wisdom of Ubuntu: 'I am because we are'")
    print("This program connects to the global web community to fetch and store shared images.\n")

    # Prompt user for image URL
    image_url = input("🔗 Enter the URL of the image you want to fetch: ").strip()

    # Directory to store fetched images
    folder_name = "Fetched_Images"
    os.makedirs(folder_name, exist_ok=True)  # Create if it doesn’t exist

    # Extract filename from URL or generate one
    parsed_url = urlparse(image_url)
    filename = os.path.basename(parsed_url.path)
    if not filename:  # In case URL doesn’t have a filename
        filename = "image_from_ubuntu_community.jpg"

    filepath = os.path.join(folder_name, filename)

    try:
        # Fetch image
        print("\n📡 Connecting to the web community...")
        response = requests.get(image_url, timeout=10)
        response.raise_for_status()  # Raise error for bad responses

        # Save image in binary mode
        with open(filepath, "wb") as f:
            f.write(response.content)

        print(f"✅ Image successfully fetched and saved as: {filepath}")

    except requests.exceptions.HTTPError as e:
        print(f"⚠️ HTTP Error: {e}")
    except requests.exceptions.ConnectionError:
        print("⚠️ Connection Error: Could not connect to the internet.")
    except requests.exceptions.Timeout:
        print("⏳ Timeout Error: The request took too long.")
    except Exception as e:
        print(f"⚠️ An unexpected error occurred: {e}")

    finally:
        print("\n🙏 Thank you for connecting with the community. All shared images are stored in the 'Fetched_Images' folder.")

# Run the function
if __name__ == "__main__":
    fetch_image()
