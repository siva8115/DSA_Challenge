import os
import json
import random
import smtplib
from email.mime.text import MIMEText

# ==========================
# Environment Variables
# ==========================
SENDER_EMAIL = os.environ["SENDER_EMAIL"]
RECEIVER_EMAIL = os.environ["RECEIVER_EMAIL"]
GMAIL_APP_PASSWORD = os.environ["GMAIL_APP_PASSWORD"]

# ==========================
# DSA Question Database
# ==========================

questions = [

    {
        "title": "Two Sum",
        "difficulty": "Easy 🟢",
        "category": "Arrays, Hash Map",
        "problem": "Given an array of integers nums and an integer target, return the indices of the two numbers such that they add up to target.",
        "link": "https://leetcode.com/problems/two-sum/"
    },

    {
        "title": "Best Time to Buy and Sell Stock",
        "difficulty": "Easy 🟢",
        "category": "Arrays",
        "problem": "Find the maximum profit you can achieve from buying and selling one stock.",
        "link": "https://leetcode.com/problems/best-time-to-buy-and-sell-stock/"
    },

    {
        "title": "Valid Parentheses",
        "difficulty": "Easy 🟢",
        "category": "Stack",
        "problem": "Determine whether the input string containing brackets is valid.",
        "link": "https://leetcode.com/problems/valid-parentheses/"
    },

    {
        "title": "Binary Search",
        "difficulty": "Easy 🟢",
        "category": "Binary Search",
        "problem": "Given a sorted array, search for the target value.",
        "link": "https://leetcode.com/problems/binary-search/"
    },

    {
        "title": "Merge Two Sorted Lists",
        "difficulty": "Easy 🟢",
        "category": "Linked List",
        "problem": "Merge two sorted linked lists into one sorted list.",
        "link": "https://leetcode.com/problems/merge-two-sorted-lists/"
    },

    {
        "title": "Maximum Subarray",
        "difficulty": "Medium 🟡",
        "category": "Dynamic Programming",
        "problem": "Find the contiguous subarray having the largest sum.",
        "link": "https://leetcode.com/problems/maximum-subarray/"
    },

    {
        "title": "Reverse Linked List",
        "difficulty": "Easy 🟢",
        "category": "Linked List",
        "problem": "Reverse a singly linked list.",
        "link": "https://leetcode.com/problems/reverse-linked-list/"
    },

    {
        "title": "Number of Islands",
        "difficulty": "Medium 🟡",
        "category": "Graph",
        "problem": "Count the number of islands in a 2D grid.",
        "link": "https://leetcode.com/problems/number-of-islands/"
    },

    {
        "title": "Flood Fill",
        "difficulty": "Easy 🟢",
        "category": "Graph",
        "problem": "Perform a flood fill on a given image.",
        "link": "https://leetcode.com/problems/flood-fill/"
    },

    {
        "title": "Merge Intervals",
        "difficulty": "Medium 🟡",
        "category": "Intervals",
        "problem": "Merge all overlapping intervals.",
        "link": "https://leetcode.com/problems/merge-intervals/"
    }

]

# ==========================
# Random Question
# ==========================

question = random.choice(questions)

# ==========================
# Email Sender
# ==========================

def send_email():

    subject = "🚀 Daily DSA Challenge"

    body = f"""
Good Morning! 🌞

Your Daily DSA Challenge is here.

--------------------------------------------

📌 Problem
{question['title']}

📊 Difficulty
{question['difficulty']}

📚 Category
{question['category']}

📝 Problem Statement

{question['problem']}

--------------------------------------------

🔗 Practice Here

{question['link']}

--------------------------------------------

🎯 Today's Goal

Solve this problem within 20-30 minutes without looking at the solution.

Happy Coding!

Keep Learning 🚀
"""

    email = MIMEText(body)

    email["Subject"] = subject
    email["From"] = SENDER_EMAIL
    email["To"] = RECEIVER_EMAIL

    with smtplib.SMTP("smtp.gmail.com", 587) as server:

        server.starttls()

        server.login(
            SENDER_EMAIL,
            GMAIL_APP_PASSWORD
        )

        server.sendmail(
            SENDER_EMAIL,
            RECEIVER_EMAIL,
            email.as_string()
        )

# ==========================
# Lambda Handler
# ==========================

def lambda_handler(event, context):

    try:

        send_email()

        return {
            "statusCode": 200,
            "body": json.dumps({
                "message": "Daily DSA Challenge Sent Successfully!",
                "question": question["title"]
            })
        }

    except Exception as e:

        print(str(e))

        return {
            "statusCode": 500,
            "body": json.dumps({
                "error": str(e)
            })
        }
