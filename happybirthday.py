import webbrowser
import time

html_content = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>🎉 Birthday Surprise 🎉</title>
    <style>
        body {
            text-align: center;
            font-family: 'Comic Sans MS', cursive, sans-serif;
            background: linear-gradient(120deg, #ff9a9e, #fad0c4);
            color: white;
            margin: 0;
            padding: 0;
            overflow: hidden;
        }
        .container {
            position: relative;
            height: 100vh;
            display: flex;
            justify-content: center;
            align-items: center;
            flex-direction: column;
        }
        .gift-box {
            width: 150px;
            height: 150px;
            background: gold;
            position: relative;
            text-align: center;
            border-radius: 10px;
            cursor: pointer;
            transition: transform 0.5s;
            display: inline-block;
            margin: 10px;
        }
        .gift-box:hover {
            transform: scale(1.1);
        }
        .lid {
            width: 170px;
            height: 40px;
            background: darkred;
            position: absolute;
            top: -40px;
            left: -10px;
            border-radius: 10px 10px 0 0;
            transition: top 0.5s;
        }
        .open .lid {
            top: -100px;
        }
        .message {
            font-size: 24px;
            margin-top: 20px;
            opacity: 0;
            transition: opacity 1s;
        }
        .show-message {
            opacity: 1;
        }
        .confetti {
            position: absolute;
            width: 10px;
            height: 10px;
            background-color: #fff;
            opacity: 0.7;
            border-radius: 50%;
            animation: fall 3s linear infinite;
        }
        @keyframes fall {
            0% {
                transform: translateY(0);
            }
            100% {
                transform: translateY(100vh);
            }
        }
    </style>
</head>
<body>
    <div class="container">
        <h1>🎈 Click All the Gift Boxes to Reveal the Surprise! 🎁</h1>
        <div class="gift-box" onclick="revealGift(this, '🎂 A Delicious Cake! 🎂')">
            <div class="lid"></div>
            <p style="margin-top: 50px; font-weight: bold;">🎁</p>
        </div>
        <div class="gift-box" onclick="revealGift(this, '🎮 A Cool Video Game! 🎮')">
            <div class="lid"></div>
            <p style="margin-top: 50px; font-weight: bold;">🎁</p>
        </div>
        <div class="gift-box" onclick="revealGift(this, '🎧 A Pair of Headphones! 🎧')">
            <div class="lid"></div>
            <p style="margin-top: 50px; font-weight: bold;">🎁</p>
        </div>
        <div class="gift-box" onclick="revealGift(this, '🎉 Happy Birthday, Shashank Bhai! 🎉')">
            <div class="lid"></div>
            <p style="margin-top: 50px; font-weight: bold;">🎁</p>
        </div>
        <div class="message hidden" id="message"></div>
    </div>
    <script>
        let openedCount = 0;
        function revealGift(box, message) {
            if (!box.classList.contains('open')) {
                box.classList.add('open');
                setTimeout(() => {
                    document.getElementById('message').innerHTML = message;
                    document.getElementById('message').classList.remove('hidden');
                    document.getElementById('message').classList.add('show-message');
                    launchConfetti();
                }, 500);
                openedCount++;
            }
        }
        function launchConfetti() {
            for (let i = 0; i < 100; i++) {
                let confetti = document.createElement('div');
                confetti.className = 'confetti';
                confetti.style.left = Math.random() * 100 + 'vw';
                confetti.style.animationDuration = (Math.random() * 3 + 2) + 's';
                confetti.style.backgroundColor = `hsl(${Math.random() * 360}, 100%, 75%)`;
                document.body.appendChild(confetti);
                setTimeout(() => confetti.remove(), 5000);
            }
        }
    </script>
</body>
</html>
"""

# Save the HTML content to a file
html_file_path = "birthday_surprise.html"
with open(html_file_path, "w", encoding="utf-8") as file:
    file.write(html_content)

# Wait for a moment before opening
time.sleep(1)

# Open in Google Chrome
webbrowser.open(html_file_path)
