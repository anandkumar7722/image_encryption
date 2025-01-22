🔐 Image Encryption & Decryption CLI Tool




📌 About
This CLI-based Image Encryption Tool allows users to securely encrypt and decrypt images using AES-256 encryption. It ensures privacy and protection for sensitive image files by preventing unauthorized access.

🚀 Features
✅ AES-256 Encryption for strong security 🔒
✅ Encrypt & Decrypt Any Image via CLI
✅ Automatic Key Generation & Logging
✅ Logs Encrypted Files for easy tracking
✅ Cross-Platform Support (Linux & Windows)

📥 Installation
🔧 Prerequisites
Ensure you have Python 3.8+ installed. If using Kali Linux or other managed environments, set up a virtual environment.

💻 Setup
bash
Copy
Edit
# Clone the repository
git clone https://github.com/YOUR_GITHUB_USERNAME/YOUR_REPO_NAME.git
cd YOUR_REPO_NAME

# Create a virtual environment (Recommended)
python3 -m venv venv
source venv/bin/activate  # On Windows use: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt
🔐 Usage
1️⃣ Encrypt an Image
bash
Copy
Edit
python image_tool.py
Select 1 for encryption, then enter the path to the image file.

2️⃣ Decrypt an Image
bash
Copy
Edit
python image_tool.py
Select 2 for decryption, then enter the encrypted file path.

🛠 Tech Stack
Python 🐍
PyCryptodome for AES encryption
OS & JSON for key storage
⚡ Future Enhancements
📌 Add Steganography Features for hidden data encryption
📌 Implement GUI Version for user-friendly interaction
📌 Enable Multi-Layer Encryption for extra security

📜 License
This project is open-source and available under the MIT License.

🤝 Contributing
Contributions are welcome! Feel free to fork this repository, submit issues, or create pull requests.

Fork the repo 🍴
Create your feature branch git checkout -b feature-name
Commit your changes git commit -m "Added a new feature"
Push to the branch git push origin feature-name
Open a Pull Request 📢
